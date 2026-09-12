# Log Parser & IOC Detection Pipeline

This is my first real portfolio project. I wanted something that actually used my Java and SQL background instead of just doing another guided lab, so this grew out of a session where I was manually tracing a brute force to persistence attack chain in Windows event logs. Instead of just reading the logs and spotting the pattern myself, I decided to build the detection logic and see if I could get it to catch the same thing automatically.

## What it does

A Java parser reads a CSV of Windows style event logs (event_time, event_id, source_ip, account, hostname) and inserts each row into MySQL through JDBC. From there, a SQL trigger watches every insert and reacts to two patterns.

1. Brute force. If it sees 5 or more failed logons (event ID 4625) from the same source IP within a 10 minute window, it fires an alert.
2. Possible persistence. If an account that already has a brute force alert against it then shows up creating a new account (event ID 4720) within 30 minutes, that fires a second, higher severity alert. This mirrors the actual attack chain I was tracing by hand originally: brute force in, then create a new account to keep access.

Detection happens the moment the data lands, no manual review needed.

## Detection rules

| Technique | Name | What it catches |
|---|---|---|
| T1110 | Brute Force | 5+ failed logons (event 4625) from the same source IP within a 10 minute window |
| T1136 | Create Account | A new account (event 4720) created by an account that already has an active brute force alert, within 30 minutes, flagged as possible persistence |

## Stack

Java for parsing and JDBC, MySQL (running through XAMPP) for storage and the trigger logic, built and tested in VSCode.

## Bugs I hit (and actually learned something from)

I hit the same ArrayIndexOutOfBoundsException twice while building the parser, for two completely different reasons.

First time it was blank lines in the CSV throwing off the column count, easy fix, just skip empty lines.

Second time I got the exact same error but the cause was totally different. I added a debug print to see the raw line before it broke, and the output was garbled binary data with Excel internals mixed in. Turned out my "CSV" was actually an xlsx file that had just been renamed. Lesson that stuck with me: don't trust the file extension, verify the actual format when the error doesn't match what you'd expect.

Later on, while adding the persistence trigger, I ran into a correlation bug that was more interesting than a crash. My first version of the persistence check matched on source_ip only, and it ended up firing a false alert for an unrelated account (svc_backup) just because it shared an IP with the actual attacker's brute forced account (jdoe). The fix was correlating on the account itself instead of the IP, since the persistence pattern I actually care about is "the compromised account creates a new account," not "any account activity from that IP." Good reminder that picking the right correlation key matters as much as the detection logic itself.

I also learned the hard way that Excel will silently reformat date values in a CSV every time you save, even with the column set to Text format, so I stopped editing the CSV in Excel entirely and just edit it directly in VSCode now.

## Testing

Tested against a sample CSV with a crafted brute force pattern (5 failed logons from the same IP) mixed with normal traffic, plus a follow up account creation event from the same account, and a separate unrelated account creation event with no prior brute force. Result: the brute force alert fires once, the persistence alert fires only for the actually compromised account, and the unrelated account creation correctly produces no alert.

## Next up

- Password spraying detection: one failed attempt across many accounts from the same IP, a pattern my current brute force rule wouldn't catch since it only looks at repeated failures on a single account.
- Stress test against a much larger set of normal, non malicious traffic to check for false positives at scale.
