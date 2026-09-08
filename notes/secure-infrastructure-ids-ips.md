# Secure Infrastructure: Device Placement, IDS/IPS, Fail-Open vs Fail-Closed (Sec+ Domain 3.2, part 1)

Started 3.2 today, secure infrastructure. Opened with a review scenario on containerization and IaC from last session (container escape identified correctly, but I trailed off into a question instead of committing to the actual distinction between "vulnerable dependency exploited" being a patch management problem, not something IaC is meant to catch, good reminder to state the category plainly instead of hedging).

## Device placement and security zones

Where a device physically sits in the network determines what it can see and control.

| Device | Placement logic | Function |
|---|---|---|
| Firewall | At zone boundaries, perimeter or between segments | Filters traffic based on rules |
| IDS | Out-of-band, monitors a copy of traffic | Detects and alerts only, doesn't block |
| IPS | In-line, sits directly in the traffic path | Detects and blocks in real time |
| Load balancer | In front of a server pool | Distributes traffic, also hides individual server exposure |

## The exam trap that mattered most

IDS vs IPS isn't about detection capability, it's about placement. The same detection engine can power both, the difference is IDS sits out-of-band (sees a copy, can't stop anything) and IPS sits in-line (sees the real traffic, can actually block it). This is basically the same pattern as PDP vs PEP again, one observes and decides, the other sits directly in the path and acts.

## Fail-open vs fail-closed

When a security device fails, does it default to allowing traffic through (fail-open, availability priority) or blocking it (fail-closed, security priority). This is a real design decision with real trade-offs, not just a technical toggle.

## Scenarios I worked through

**IDS/IPS identification.** One device in-line, inspects application layer content, drops malicious traffic in real time. Second device gets a mirrored copy, alerts the SOC but takes no action. Correctly named these IPS and IDS. Follow up asked which one poses more availability risk if it fails, I said IPS but for the wrong reason initially, I said "nothing will block traffic" which is actually a security consequence, not an availability one. The correct reasoning: IPS sits in-line, meaning all traffic physically has to pass through it. If it fails and is fail-closed (common default for IPS), all traffic just stops completely, that's the availability risk, a full outage, because the device sitting in the traffic's path became a wall. IDS by contrast has zero availability impact if it fails since it's only watching a copy, you just lose visibility.

**Hospital vs bank fail-open/fail-closed scenario.** Hospital's patient monitoring network configures its in-line IPS to fail-open, life-safety monitoring can't afford to get blocked. Bank's transaction system configures fail-closed instead, security over uptime, accepting the trade-off that they might go offline rather than let bad traffic through. Got the reasoning behind both choices right. The part I actually didn't know was the third question, what's the specific operational consequence if the bank's IPS crashes during business hours. Answer: since it's in-line, a fail-closed crash means it becomes a wall, nothing passes through, so the entire transaction processing system goes offline, no purchases, no transfers, no card payments tied to that system, during business hours. Real financial and reputational cost. Good lesson here, when unsure, reason from the mechanism (in-line means physical chokepoint) instead of just saying I don't know.

## Status

Domain 3.2 in progress. Device placement, IDS vs IPS, fail-open vs fail-closed covered. Firewall types (packet-filtering, stateful, NGFW) still ahead, along with the rest of secure infrastructure topics.
