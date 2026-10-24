# Security Alerting and Monitoring

The analogy that worked for me was an airport security control room. Cameras and sensors all over the airport are the **log sources**. Every feed goes into one room, which is **log aggregation**, usually a SIEM. Operators write rules that connect events across feeds, which is **correlation**. When a rule matches, an **alert** fires. A guard responds and maybe isolates a gate, which is **quarantine**. If the alarm goes off for every passenger's belt buckle, the guards stop reacting, and fixing that is **alert tuning**. Old footage gets kept for investigations, which is **archiving**.

| Concept | Meaning |
|---|---|
| Log aggregation | Collect logs from many sources into one searchable place |
| SIEM | Aggregates, correlates, alerts, and reports on those logs |
| Alert tuning | Adjust rules and thresholds to cut false positives without creating false negatives |
| Quarantine | Isolate a flagged system or file so it can't spread, while keeping it for analysis |
| Archiving | Keep old logs for compliance and later investigations |
| Agent | Software on the endpoint that collects and sends data. Richer data, but must be installed and maintained |
| Agentless | Collects remotely (syslog, WMI, API) with nothing installed. Easier to deploy, shallower data |
| SNMP trap | A network device pushes a message to the monitoring station when something happens, instead of waiting to be polled |
| NetFlow | Metadata about traffic flows: who talked to whom, how much, when. Never the content |
| SCAP | A standard way to automatically check systems against security baselines and known vulnerabilities, using benchmarks like CIS and DISA STIG |

The tradeoff I need to remember: a **false positive** is a harmless event flagged as an attack. A **false negative** is a real attack that goes unflagged. Tune too little and analysts drown, tune too hard and attacks slip through.

## Warm-up: what I got right and wrong

1. **API key to a third party.** I said encrypt, because the backend needs the original back to send it. Correct. Something I'm adding for my cloud goal: encryption is only as strong as where the key lives. The real answer is a secrets manager (AWS Secrets Manager, Azure Key Vault), not an encrypted value with the key sitting next to it in the same config file.
2. **Badge reader losing its database connection.** I said fail closed and that the deciding factor is security vs human safety. Right, but the question had two parts and I only answered one. The missing half: a stairwell or emergency exit door should fail **open**, because people trapped during a fire or power loss costs more than an unlocked door. The sharper deciding factor is what the wrong failure costs. Physical security calls these **fail secure** (stays locked) and **fail safe** (unlocks for life safety). Fail closed applies to entry, and exiting the server room should still work mechanically.
3. **OWASP check.** A10 for the stack trace on a database timeout (no debug flag, so not A02), and A09 for 5,000 failed logins with no alert. Both correct. One precision point: credential stuffing replays leaked username and password pairs, while brute force guesses. The prompt didn't say which, so I shouldn't claim a specific one without evidence.

## The scenario

A company has 200 laptops, 10 servers, a firewall, and a router. Its SIEM gets 2 million events a day and creates 900 alerts a day. About 95% are false positives, mostly "failed login" alerts for mistyped passwords. Analysts started ignoring the queue, and last Tuesday a real alert got missed.

My answers and the corrections:

1. **Problem and fix.** I said tune the alert, adjust rules and thresholds to cut false positives without creating false negatives, and that tuning too aggressively lets attacks through. Right, but I didn't name the problem. It's **alert fatigue**: analysts drown in false positives and start ignoring the queue, which is exactly how Tuesday's real alert got missed. This is my "right action, missing formal term" pattern again. Good tuning means adjusting thresholds and scope (say 5 failed logins in 5 minutes per account instead of every single failure), not disabling the rule, and reviewing the tuned rules regularly.
2. **Router that can't run extra software.** I said agentless, which is right, but the question also asked which protocol lets it push a message when an interface goes down, and I skipped that half. The answer is **SNMP trap**. The device pushes the message when an event happens instead of waiting to be polled. That's the second time today a multi part question got half an answer, so I need to check that every part has a line before I send.
3. **Which host sent 40 GB to an unknown IP at 3 AM, without packet contents.** NetFlow, correct. My reasoning was missing: it records flow metadata (source, destination, volume, time) and never the content, which is exactly what the question asked for. A packet capture would give content, but at that volume it's heavy and not needed to find the host.
4. **Laptop with a confirmed malware alert.** I said isolate it. Right action, but I skipped why you don't just wipe it. Three reasons: wiping destroys evidence, so I lose how the malware got in and whether other machines are affected (root cause analysis). It breaks the forensic process I already know: keep it powered on so RAM survives (order of volatility), image it, then eradicate and recover. And containment comes before eradication in PICERL, so wiping first skips a phase. Isolating is **quarantine** plus **containment**.

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| SIEM | Aggregate, correlate, alert, report |
| Alert fatigue | Too many false positives, real alerts get ignored |
| Tuning | Cut false positives without creating false negatives |
| Agent vs agentless | Rich data but installed, vs easy but shallower |
| SNMP trap | Device pushes the alert, no polling |
| NetFlow | Who talked to whom, how much, never content |
| SCAP | Automated checks against baselines and known vulnerabilities |
| Quarantine | Isolate, keep for analysis, don't destroy |

## Still to do

Investigation Data Sources, which reads the data a SIEM collects. 
