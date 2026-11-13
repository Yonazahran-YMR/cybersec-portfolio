# Cloud Security: Logging and Monitoring

Theory notes.

## The big idea

Cloud logging and monitoring is like a building with cameras and a security office. The cameras record everything that happens (logging). A guard watches the screens (monitoring). An alarm bell rings when something matches a rule (alerting). A central security office collects the footage from every camera and connects the dots (SIEM). This clicked for me because each piece answers a different question: what happened, is anything wrong right now, and who needs to know.

| Building | Cloud | Meaning |
|---|---|---|
| Cameras recording | Logging | Record events as they happen |
| Guard watching screens | Monitoring | Watch logs and metrics continuously |
| Alarm bell | Alerting | Notify when a rule matches |
| Central security office | SIEM | Collect logs from many sources and correlate them |

Logging is a detective control. It finds what happened, it doesn't stop it. I mixed up control types before, so I keep this one straight: detective finds, preventive stops, corrective fixes.

Which log answers which question:

| Question | Log type | AWS | Azure |
|---|---|---|---|
| Who did what? (API calls, console actions) | Audit log | CloudTrail | Activity Log |
| How is it performing? Alarms and metrics | Monitoring | CloudWatch | Azure Monitor |
| Who talked to whom? (source, destination, port, allow or deny) | Flow logs | VPC Flow Logs | NSG Flow Logs |
| Is there suspicious behavior? | Threat detection | GuardDuty | Defender for Cloud |
| Did a config drift from the rule? | Config tracking | AWS Config | Azure Policy |

Quick split: audit log is who, flow log is network metadata, monitoring is health and alarms.

The log pipeline:

1. Source produces the event
2. Collect it
3. Send it to a central, separate location
4. Protect its integrity
5. Analyze and alert
6. Retain it long enough

Exam traps:

1. Flow logs record metadata (IPs, ports, bytes), not the packet content.
2. Logs kept only on the compromised system can be wiped by the attacker. Send them to a central, restricted, remote location. This is also why remote logs rank above backups in the order of volatility.
3. Logging without alerting is A09, Security Logging and Alerting Failures. Nobody reads the logs, so the breach goes unnoticed.
4. Shared responsibility: the provider runs the platform, but I must turn on and configure logging for my own resources. Some logs are off by default.
5. Retention has to be long enough for compliance and investigations.

## Warm-up: what I got right and wrong

This warm-up had 3 questions, one cloud IAM, one recurring mistake on volatility, and one on OWASP 2025.

1. Cloud IAM, explicit allow plus explicit deny on the same action. I said access denied, deny overrides all allow. Correct. The formal term is explicit deny. Full order: implicit deny by default, explicit deny beats everything, then explicit allow.
2. Order of volatility. I said RAM and running processes, disk, remote logs, backups. Correct. The reason: the most volatile data disappears first, so I collect it first.
3. OWASP 2025, two cases. (a) An imported library with a known vulnerability is A03, Software Supply Chain Failures. I wrote "Software supply chain failures" correctly, so the full name is locked in. (b) A login flow with no attempt limit because nobody planned for abuse is A06, Insecure Design. Correct. It's not A02, because no setting was wrong, the design never accounted for it.

All parts counted, none skipped.

## The scenario

A security team finds that a storage bucket was changed to public yesterday. Nobody knows which account made the change. Which log source should the team check first, and why?

My answer: the audit log, because it tracks administrative changes and captures identity and context. Flow logs are connection and network metadata, so they show traffic, not configuration changes. Correct, with the contrast present.

Sharper version for the exam: the audit log is CloudTrail on AWS and Activity Log on Azure. A bucket change is a management plane API call, and the audit log records every one with 4 fields: who (identity), what (action), when (timestamp), and from where (source IP). Flow logs only show IPs, ports, and bytes, so they can't tell me which account changed a setting.

How I pick the right source on the exam:

| If the question asks | Pick |
|---|---|
| Who changed this setting? | Audit log |
| Was this resource exposed to the internet traffic wise? | Flow logs |
| Did the config drift from the rule? | Config tracking (AWS Config, Azure Policy) |
| Is the service healthy, did a threshold break? | Monitoring |

Making the bucket private again is a corrective control. Finding the change in the log was the detective control.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Logging, monitoring, alerting | Record, watch, notify |
| Logging control type | Detective, it finds and doesn't stop |
| Who made a change | Audit log: CloudTrail or Activity Log |
| Audit log fields | Who, what, when, from where |
| Flow logs | Network metadata only, never packet content |
| Monitoring | CloudWatch or Azure Monitor, health and alarms |
| Threat detection | GuardDuty or Defender for Cloud |
| Config drift | AWS Config or Azure Policy |
| Where logs go | Central, remote, protected, never only on the compromised host |
| Logs but nobody alerts | A09, Security Logging and Alerting Failures |
| Shared responsibility | I turn on and configure logging for my own resources |

## Still to do

1. Network isolation in the cloud
2. Cloud misconfiguration
3. AI and LLM security
4. Later: Security+ gap closers (acronyms, performance based questions)
