# Custom Log Parser & IOC Detection Pipeline

First real portfolio project, and it's the one I'm most excited about since it uses my Java and SQL background directly instead of just doing another guided lab. The idea was to take the brute force to persistence attack chain I traced by hand back in my log analysis session and actually build the detection logic myself instead of relying on someone else's SIEM.

## What it does

Takes a CSV of Windows style event logs (event_time, event_id, source_ip, account, hostname), parses it in Java, and inserts each row into a MySQL database. A SQL trigger watches every insert into the events table and automatically flags a brute force pattern, five or more failed logons (event ID 4625) from the same source IP within a 10 minute window, into a separate alerts table. No manual log review needed, the detection happens the moment the data lands.

## Stack

Java for parsing and JDBC, MySQL (via XAMPP) for storage and the trigger logic. Built and tested in VSCode with the Java Extension Pack and the mysql-connector-j driver.

## Schema

```sql
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_time DATETIME NOT NULL,
    event_id INT NOT NULL,
    source_ip VARCHAR(45),
    account VARCHAR(100),
    hostname VARCHAR(100)
);

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    triggered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    alert_type VARCHAR(100),
    related_account VARCHAR(100),
    related_ip VARCHAR(45),
    details TEXT
);
```

## The trigger

```sql
DELIMITER $$

CREATE TRIGGER trg_brute_force
AFTER INSERT ON events
FOR EACH ROW
BEGIN
    DECLARE fail_count INT;

    IF NEW.event_id = 4625 THEN
        SELECT COUNT(*) INTO fail_count
        FROM events
        WHERE event_id = 4625
          AND source_ip = NEW.source_ip
          AND event_time >= (NEW.event_time - INTERVAL 10 MINUTE)
          AND event_time <= NEW.event_time;

        IF fail_count >= 5 THEN
            INSERT INTO alerts (alert_type, related_account, related_ip, details)
            VALUES ('Brute Force Suspected', NEW.account, NEW.source_ip,
                    CONCAT(fail_count, ' failed logons in 10 min window'));
        END IF;
    END IF;
END$$

DELIMITER ;
```

This is basically the exact logic I was doing manually with the 4624/4625/4720/4728 event ID chain, just automated as a database side effect now instead of me eyeballing timestamps.

## Bugs I ran into (and this is honestly the part worth documenting most)

First run threw an ArrayIndexOutOfBoundsException on a blank line in the CSV, an easy fix, just skip empty lines before splitting.

Second run threw the same error again, but this time it wasn't blank lines. I added a debug print right before the split to log the raw line before it crashed, and the output was garbled binary data with recognizable Excel internals buried in it (workbook.xml showed up in the noise). Turned out my CSV wasn't actually a CSV, it was an xlsx file that got renamed with a .csv extension instead of properly exported. Re-saved it through File > Save As with the actual CSV format selected in Excel, and that fixed it.

That debugging process taught me more than the actual coding did honestly. The lesson that stuck: don't trust a file extension, verify the actual file format when something's failing in a way that doesn't match the error you'd expect.

## Result

Ran the parser against a 10 row sample CSV containing a crafted brute force pattern (5 failed logons from the same IP within a few minutes, mixed with normal traffic as noise). All 10 events inserted successfully, and the trigger fired exactly as expected: one row in the alerts table, alert_type "Brute Force Suspected," correctly flagging the account and source IP with the specific fail count in the details field.

## What's next

Planning to extend this with chained detection, if an alert already exists for an account or IP and a new 4720 (new account creation) event follows shortly after, fire a higher severity alert for possible persistence. That would mirror the full attack chain (brute force, foothold, persistence, priv esc) I traced manually, not just the first step. Also want to stress test it against a larger set of normal, non-malicious traffic to make sure it doesn't false positive on legitimate logon patterns.
