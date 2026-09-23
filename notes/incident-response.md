# Domain 4: Security Operations

## Session 3: Incident Response

### The IR lifecycle (NIST SP 800-61)

1. **Preparation**: before anything happens, IR plan, playbooks, tools, trained team, communication chains.
2. **Detection and analysis**: alert fires, analyst confirms it's a real incident (not a false positive) and scopes it, what's affected, how bad.
3. **Containment**: stop the bleeding. Short-term (isolate the host) vs long-term (patch, rebuild) containment are distinct steps.
4. **Eradication**: remove the actual threat, malware, backdoor, compromised account.
5. **Recovery**: bring systems back online, monitor closely for recurrence.
6. **Post-incident activity**: lessons learned meeting, update playbooks. This is the step orgs skip most and shouldn't.

### Scenario: EDR alert, C2 beaconing

An EDR alert fires for a workstation running an unrecognized process with C2-like beaconing behavior. Analyst confirms it's malicious and isolates the host from the network immediately, before knowing how the malware got in or whether it's spread elsewhere.

Stage: containment, specifically short-term containment. Isolate now, figure out root cause and full remediation later. The point of short-term containment is stopping the bleeding fast without waiting to fully understand the incident first.

Next question after isolating: scope, could this have spread laterally before isolation happened. That's the usual segue from containment into eradication, confirming everything's caught before starting cleanup.

### Mistake to watch for

Mixed up two separate Sec+ taxonomies on a review question: control types (preventive/detective/corrective/compensating/deterrent) vs risk-mitigation strategy categories (patch management, hardening, segmentation, transfer, acceptance). Both valid concepts, but they answer different questions, don't cross-apply them.

### Next up

Eradication and recovery, plus the PICERL vs NIST framework naming distinction.
