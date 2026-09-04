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