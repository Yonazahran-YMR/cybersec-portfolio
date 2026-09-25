# Domain 4: Security Operations

## Session 4: Digital Forensics Basics

### Chain of custody

Documented record of who handled evidence, when, and what they did with it. Every transfer gets logged, collector to analyst to storage, no gaps. If chain of custody breaks, evidence can become inadmissible in legal proceedings, and this matters even outside courtrooms since internal investigations and compliance audits care too.

### Order of volatility

When collecting evidence, grab the most volatile (fastest to disappear) data first.

| Order | Data type |
|---|---|
| 1 | CPU registers and cache |
| 2 | RAM |
| 3 | Network state / active connections |
| 4 | Running processes |
| 5 | Disk data |
| 6 | Logs |
| 7 | Archived / backup data |

Reasoning: RAM contents vanish on reboot, disk data survives. If disk imaging happens first and the system reboots or crashes mid-process, RAM evidence is lost permanently, and RAM often holds what disk imaging can't get anyway, running malware, decrypted data, active network connections.

### Scenario: compromised server, still powered on

First responder wants to immediately pull the power cable to "preserve state." Wrong move, pulling power destroys everything volatile instantly, RAM, active network connections, running processes, all gone.

Correct sequence: with the system still running, capture in order, CPU registers/cache, then RAM (memory dump via forensic tool), then network connections and state, then running processes, then disk imaging, then logs, then archived data. System only gets powered down after volatile evidence is captured.

The "pull the cable" instinct is a classic exam distractor, feels like preserving state but actually destroys the most valuable, hardest-to-recover evidence first.

### Domain 4 status

Closes out the core of Domain 4: security operations, vulnerability management, IR lifecycle, and forensics.

### Next up

OWASP Top 10.
