# Windows Event Logs & Incident Response Basics

Going deeper into log analysis tonight, this time actual Windows Event IDs instead
of generic login logs. This is apparently one of THE most common things SOC
analysts work with day to day.

## Key Event IDs to know

| Event ID | Meaning |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4720 | New user account created |
| 4728 | User added to a security-enabled group (like Administrators) |

## Reading a full attack sequence

Was given this pattern to interpret:
```
4625, 4625, 4625, 4625, 4625  (multiple failed logons)
4624                          (a successful logon right after)
4720                          (a new user account created)
4728                          (that new account added to Administrators)
```

First part was easy, this is a successful brute-force (repeated fails then a
success matches the pattern from earlier logs practice). What I didn't get right
away was why an attacker would bother creating a whole new account after already
getting in.

## Why attackers create a new account after breaking in (persistence)

Makes sense once explained. If they just keep using the account they brute-forced
into, that's risky for THEM:
- the real account owner might notice something's off and get IT to lock it down
- the compromised account could get flagged, password reset, disabled

So instead they create a completely new account (usually give it admin rights too)
as a backdoor that doesn't depend on the original stolen credentials staying valid.
Even if the original compromised account gets fixed, they've still got a separate
way back in.

Analogy that made it click: someone picks your front door lock to get in, then
once inside, cuts themselves a spare key and hides it somewhere. Changing the front
door lock afterward doesn't help if they've already got that spare key stashed.

This is a real named technique called persistence, apparently a core stage in
actual attacker methodology (MITRE ATT&CK framework, haven't gotten into that
formally yet but it's coming up in CySA+ later).

## Why this sequence is way more dangerous than brute-force alone

Just brute-force by itself: bad, but blocking the IP / resetting the password
basically closes it off.

Brute-force + new admin account created: even if you fix the ORIGINAL compromised
account, the attacker still has a completely separate, fully privileged way back
in that you might not even know exists yet.

## What actual incident response looks like for this scenario

Worked through this mostly on my own before getting confirmation, so writing it
out fully:

**Immediate containment:**
- block the attacker's IP
- disable/delete the newly created admin account
- force password reset on the originally compromised account too

**Investigation - since they had full admin access, assume the worst until proven
otherwise:**
- check for OTHER new accounts they might've created, not just the one you spotted
- check for other group membership changes (more 4728 events)
- check what files/systems they actually accessed with admin rights
- check if they installed anything (malware, remote access tools, scheduled tasks -
  another common persistence method besides new accounts)
- check if they disabled any security tools (antivirus, logging) to cover their tracks

The mindset here: full admin access means they COULD have done anything an admin
can do, until investigation proves otherwise. Can't assume the damage is limited
to just the first thing you noticed.

**Final step - documentation/report:**
This is technically called "Lessons Learned" or Post-Incident Review in the actual
IR lifecycle (Identification -> Containment -> Eradication -> Recovery -> Lessons
Learned). The report should cover:
- full timeline of what happened
- how they got in (weak password, brute-forceable, no lockout policy)
- what they did once inside
- how it was contained
- root cause
- recommendations going forward (mandatory lockout after N failed attempts, MFA,
  etc - this would count as a Mitigate action from the risk management stuff I
  learned earlier)

This report step is basically the "Disseminate" stage from the CTI lifecycle -
turning what happened into something actionable for the future, not just closing
the ticket and moving on.

## Takeaway for myself
Ended up basically reasoning through most of the real IR lifecycle on my own before
getting it confirmed - detection, containment, investigation, documentation. Good
sign the earlier stuff (brute force patterns, security controls, risk treatment) is
actually sticking and connecting together, not just memorized separately.
