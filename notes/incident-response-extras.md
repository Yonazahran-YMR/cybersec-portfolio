# Incident Response Extras

Theory notes. This covers the IR pieces that sit around PICERL: training, testing, root cause analysis, and threat hunting. It closes the last gap in my Domain 4 theory.

## The big idea

The analogy that worked for me: a fire department. Training is drills for the crew. A tabletop is walking the plan on a map in a meeting room. A simulation is a live drill. Root cause analysis is the investigator working out why the fire started. Threat hunting is an inspector checking buildings for hazards before any alarm rings.

| Concept | One line |
|---|---|
| IR training | People know their roles and the procedure before an incident |
| Tabletop exercise | Discussion based walkthrough of a scenario, no systems touched |
| Simulation | Hands on practice, like a phishing campaign or a staged attack |
| Root cause analysis | Find the underlying reason an incident happened, so the fix prevents a repeat. Feeds lessons learned |
| Threat hunting | Proactive, hypothesis driven search for threats that evaded detection, without waiting for an alert |
| Legal hold | Legal order to preserve relevant data, so nothing gets deleted |
| E-discovery | Collecting digital evidence for legal cases |

Two distinctions to keep:

1. Root cause analysis fixes the **cause**, while eradication removes the **current threat**.
2. Threat hunting starts **without an alert**, while detection starts **with one**.

## Warm-up: what I got right and wrong

1. **Photo printing app reads a user's cloud photos without seeing the cloud password.** I said OAuth, correct, but my reasoning was just "limited access". The fuller version: OAuth is delegated **authorization**, so the app gets limited access without the user's password. SAML would be about proving who someone is.
2. **Compromised laptop still powered on, what to collect first.** I said RAM, correct. My reason, "it will be gone after recovering", wasn't quite it. RAM is lost when power is cut or the machine reboots, and a live attacker can change it while I work. That's the order of volatility factor.
3. **Installer integrity check, nothing ever needs to be recovered.** I said hash, correct, but my reason was "it's one way", which describes hashing instead of the deciding factor. This is my recurring hash vs encrypt pattern. The factor is: nothing ever needs the original back, and I only need a fingerprint to compare. Extra: if an attacker can swap both the installer and its published hash, the check proves nothing, which is why vendors also use **digital signatures**.

## The scenario

A company contained a breach, restored its servers, and reset all passwords. Six weeks later, an attacker got in through the same unpatched web server in the same way. Which activity was most likely skipped?

I said root cause analysis, because the same vulnerability was never patched after the first breach, so the attacker could use the same way in. Correct, and the reasoning was good. To finish the sentence the way an exam wants it: the team removed the **symptoms** (restored servers, reset passwords) but never found **how the attacker got in**, so the cause was never fixed.

Two additions:

1. RCA feeds the **lessons learned** phase of PICERL, which is where the fix and process changes get recorded.
2. A tabletop exercise would also have helped, because walking the plan would have exposed the missing "find the entry point" step.

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| Training | People know their roles before an incident |
| Tabletop | Discussion only, no systems touched |
| Simulation | Hands on practice |
| Root cause analysis | Fix the cause, not just the symptoms |
| Threat hunting | Proactive search with no alert |
| Legal hold | Preserve data, don't delete |
| E-discovery | Collect digital evidence for legal use |

## Still to do

All Domain 4 theory is now covered. Next is the Domain 4 review quiz, which will also show gaps in the 4.1 mobile, wireless, and sandboxing topics. After that I move on to Domain 5 for the exam.
