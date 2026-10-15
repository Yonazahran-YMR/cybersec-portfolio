# Investigation Data Sources

## The big idea

The analogy that clicked for me: investigating a break in at an office, where every data source is a different witness.

1. The door camera shows who came to the front door (firewall).
2. The alarm system report shows what looked suspicious (IDS/IPS).
3. The badge system shows who entered (OS security logs).
4. Each employee's desk activity shows what happened locally (endpoint logs).
5. The cash register shows what was done inside the business software (application logs).
6. A full audio recording of the hallway captures everything said (packet capture).
7. The guard's summary board shows the big picture (dashboard).

| Source | What it tells me | Watch out for |
|---|---|---|
| Firewall logs | Allowed and denied connections: source, destination, port, time | Shows connections, not content |
| IDS/IPS logs | Which signature or anomaly rule fired, what was blocked | Only detects what it has rules for |
| Network logs (router, switch, DNS, proxy, NetFlow) | Traffic patterns, DNS lookups, web requests, volume | Metadata only, never content |
| OS security logs | Logins, privilege use, account changes, process creation | Can be cleared by an admin level attacker |
| Endpoint logs (EDR, antivirus) | Process, file, and registry activity on the host | Only where the agent is installed |
| Application logs | Events inside the app: transactions, errors, user actions | Quality depends on what developers chose to log |
| Metadata | Data about data: file timestamps, author, email headers | Useful for timelines, can be forged |
| Vulnerability scans | Known weaknesses, hinting at the likely way in | A snapshot of a past moment |
| Packet capture | Full traffic content | Huge storage cost, unreadable if encrypted |
| Dashboards | Summarized, visual view of SIEM data | Good for triage, not evidence |

Two rules to keep. First, **correlate multiple sources**, because one source alone can mislead. Second, **timestamps must agree**. Logs from different systems only line up if clocks are synchronized (NTP) and time zones are consistent.

## Warm-up: what I got right and wrong

1. **500 Linux servers reporting process activity and file changes.** I said agent and gave the right tradeoff (richer data, but must be installed and maintained). But the question asked for a situation where agentless would win, and I gave a definition of agentless instead. The situations: devices that can't run software (routers, switches, printers, IoT, legacy systems), quick coverage when software can't be deployed yet, or locked down systems where installs aren't allowed. Also, process activity and file change monitoring are only visible from inside the host, so here an agent isn't just nicer, it's required. This is the third time a multi part question lost a part, so I'm counting the parts before I answer now.
2. **Order of volatility: RAM, disk, remote logs, backup tapes.** Correct (b, c, d, a). The sharper deciding factor is how quickly the data changes or disappears. RAM is lost the moment power is cut. Disk comes before remote logs because the attacker is on this machine and can alter its disk, while the logging server is separate. Backup tapes are offline and stable, so they go last.
3. **OWASP check.** A02 for the public bucket from an unchanged template default (my own setting wrong), and A06 for the stackable coupon codes. For A06 the deciding factor is that the code works exactly as designed, nobody modeled how the feature could be abused, so only redesign (abuse cases, discount limits) fixes it.

## The scenario

On Monday, finance reports that 300 customer records were downloaded from an internal web app by the account `jlee` at 02:14 on Saturday. jlee says they were asleep. Available data: firewall logs, DNS logs, the Windows Security log from the app server, the application log, EDR logs from jlee's laptop, NetFlow, the SIEM dashboard, and a full packet capture of the data center segment from Friday only.

My answers and the corrections:

1. **Login vs actions.** Windows Security log for who logged in and from which IP (I mentioned Event ID 4624 logon events), application log for what the account did inside the app. Correct. Two sources, two different questions, and I kept them apart.
2. **Data leaving the network.** NetFlow or firewall logs for volume without content, packet capture for exact payload, and HTTPS makes the capture unreadable. All correct, but I missed a trap in the scenario: the capture covers **Friday only**, and the download happened Saturday at 02:14. So even without encryption there'd be no payload to read for that event. I always need to check a source's time coverage against the event. Refinement on HTTPS: without TLS inspection or the session keys the payload is unreadable, but metadata stays visible (IPs, ports, sizes, timing, often the destination name), which is still useful.
3. **02:14 UTC in the firewall vs 09:14 in the app log.** I said time zone mismatch plus lack of clock synchronization, with UTC everywhere plus NTP as the control. Correct. The nuance I want to remember: the two timestamps describe the **same instant** (02:14 UTC is 09:14 at UTC+7), so nothing drifted. The problem is mixed time zone representation, and UTC standardization fixes that. NTP fixes a different problem, clocks that drift apart. Real environments need both, and a SIEM can normalize timestamps on ingest.
4. **SIEM dashboard says "no anomalies" for Saturday.** I said don't close the investigation, because dashboards only show what the rules and baselines were built to flag, so a low and slow event can pass under a threshold. Correct, and it ties back to the false negative idea from 4.4. One overclaim: I wrote that jlee's denial "confirms" credential theft or session hijacking. A denial is a **claim**, not confirmation. Other explanations are still open: stolen credentials, a hijacked session, malware on jlee's laptop, an insider using jlee's account, or jlee being wrong. The data settles it: source IP and device from the Security log, whether jlee's laptop was active that night in the EDR logs, MFA events, and where the 300 records went afterward.

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| Firewall, IDS/IPS, network logs | Connections and detections, metadata not content |
| OS and endpoint logs | Who logged in, what ran, on the host itself |
| Application logs | What happened inside the app, only as good as what devs logged |
| Packet capture | Full content, heavy, useless if encrypted, and limited by time coverage |
| Dashboard | Triage view, not evidence |
| Correlation | Never trust one source alone |
| Time | UTC plus NTP, or timelines don't line up |

## Still to do

Next is 4.7 Automation and Orchestration. After that: enterprise security upgrades (4.5), identity and access management (4.6), the missing incident response pieces (4.8), then the Domain 4 review quiz.
