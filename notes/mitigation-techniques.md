# Mitigation Techniques

This session was about the response side of Domain 2. I already knew the vuln types (misconfig, unpatched, default creds, legacy, human) from before, today was learning what you actually do about each one.

## The techniques

| Technique | What it does | Ties to |
|---|---|---|
| Hardening | Reduce attack surface, disable unused services and ports, remove default accounts, apply secure baselines | Fixes misconfiguration and default or weak creds |
| Patch management | Scheduled patching cadence, critical or emergency patches go out of band, routine stuff on a normal cycle | Fixes unpatched vulns, zero days can't be patched by definition until a fix exists |
| Segmentation | Isolate systems or zones, VLANs, air gapping, jump boxes, so a compromise doesn't spread laterally | Also an architecture pattern, but here it's specifically a mitigation |
| Compensating controls | Alternative control when the real fix isn't possible | The answer for legacy systems that can't be patched, isolate and monitor instead |
| Least privilege / access control | Limit blast radius by limiting what an account can touch | Ties back to AAA |
| Monitoring / config enforcement | Detect drift from the secure baseline over time | Detective control |

Big thing that clicked for me, all of this sits under one bucket in the risk treatment framework I already knew (accept, mitigate, transfer, avoid). Hardening, patching, segmentation, all of it is just the specific toolbox for executing "mitigate." Before that was just a word in a table, now I actually have the techniques behind it.

## Scenarios I worked through

**Legacy ICS scenario.** Old industrial control system, unsupported OS, vendor no longer patches it. Security team puts it on an isolated VLAN with no internet access, restricted to two authorized engineers. I got the vuln type right (legacy system) but first answer for the mitigation was wrong, I said MFA which wasn't even in the scenario. Correct answer is segmentation (isolated VLAN, no internet) combined with least privilege (two engineers only), together that's a compensating control since patching isn't possible. Good lesson here, answer from the exact nouns and actions actually described in the scenario, don't reach for a control that just sounds security related in general.

**Exposed RDP scenario.** SOC audit finds RDP exposed to the internet on a finance server, using the default admin account, password never changed since setup. Two vuln types here, misconfiguration (RDP shouldn't be internet facing) and default credentials. For mitigation I said hardening fixes the misconfig and segmentation isolates the system, both correct, but the refinement was that hardening actually covers both vuln types here, not just misconfig, since renaming or disabling the default account and forcing a password change is also a hardening action. Takeaway, one technique can close more than one gap, don't force a strict one to one mapping between vuln type and fix.

## Status

Domain 2 mitigation techniques done. Threat intel sources is the last piece left before Domain 2 is fully closed out.
