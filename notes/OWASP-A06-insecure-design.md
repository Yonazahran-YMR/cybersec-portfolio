# OWASP A06: Insecure Design

Different kind of problem from A02 to A05. Those are usually implementation bugs, something coded or configured wrong. A06 is when the flaw exists even in a perfect implementation, because the design itself never accounted for the threat.

| Example | Why it's a problem |
|---|---|
| No rate limiting on a login endpoint | Design never considered brute force, even flawless code still allows unlimited attempts |
| Business logic flaw (e.g. applying a discount code unlimited times) | Not a bug, works exactly as coded, the logic itself is wrong |
| No threat modeling before building a payment flow | Nobody asked "how could this be abused" at design time |
| Trusting client-side validation as the only check | The design assumed the client would behave honestly |

The test: if this exact design were implemented with zero coding mistakes, would it still be exploitable? If yes, that's A06. The problem isn't in the code, it's in what the design allowed from the start.

Core defenses: threat modeling during design (asking "how would someone abuse this" before writing code), secure design patterns, limits and guardrails built into the business logic itself, not bolted on after.

## Scenario I worked through, and it's a real gap in my own project

My log parser's brute-force trigger fires after 5 failed logins from the same IP in 10 minutes. But an attacker could instead try 1 failed login from 100 different IPs (a botnet), spread across an hour, all targeting the same account. My current trigger never fires on that pattern.

This is A06, not a coding bug. The SQL and trigger logic work exactly as written, nothing's broken. The design only ever considered one attack pattern (many failures, one IP) and never accounted for the inverse (few failures per IP, many IPs, same target account). Flawless implementation, still exploitable, because the threat model behind the design was incomplete.

The real-world term for what the attacker's doing: credential stuffing / distributed brute force.

The fix isn't patching the trigger, it's redesigning the detection logic to track failures per target account across all source IPs, not just failures per source IP. Different dimension of detection entirely, which is why this is a design-level fix and not a bug fix.

## Next steps idea for the actual project

Add a second detection path alongside the existing IP-based trigger: aggregate failed logins by target account regardless of source IP, flag if a single account sees N failures across M distinct IPs in a given window. Worth scoping out as a real addition to the brute-force pipeline, not just theory.

## Next up

A07 Authentication Failures.
