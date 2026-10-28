# Third Party Risk

Theory notes.

## The big idea

Third party risk is like hiring a contractor and handing them a house key. If their crew is sloppy or loses the key, it becomes my breach. So I vet them before hiring, put the rules in writing, and keep checking after they start. This clicked for me because it's just three phases: before, during, after.

| Phase | What happens | Examples |
|---|---|---|
| Before (due diligence) | Vet the vendor before signing | Security questionnaires, independent assessments (SOC 2 report, ISO 27001 cert), supply chain analysis, pen test evidence |
| During (agreements) | Put expectations in writing | SLA, MSA, SOW, NDA, MOU/MOA, BPA, right to audit clause |
| After (monitoring) | Keep verifying | Right to audit, ongoing vendor assessments, rules of engagement for any testing |

Agreement types, each with the hook I'm using to remember it:

| Term | What it is | Memory hook |
|---|---|---|
| SLA | Measurable service levels (uptime, response time) plus penalties | The scoreboard |
| MSA | Master terms for the overall relationship, future work orders sit under it | The umbrella |
| SOW | Scope, deliverables, deadlines for one specific project | The job ticket |
| NDA | Confidentiality of shared information | The vow of silence |
| MOU/MOA | Statement of shared intent, non binding (MOU) or binding (MOA), often no money | The handshake |
| BPA | Partnership terms: who contributes, who profits, who shares liability | The business marriage |
| Right to audit clause | Lets me inspect the vendor's controls after signing | The inspection pass |

Exam trap I want to remember: a SOC 2 report or ISO certificate is evidence from one point in time. Continuous assurance comes from contract language plus monitoring.

## Warm-up: what I got right and wrong

1. Login verification, hash or encrypt? I said encrypt because I figured the password has to be decrypted to check it. Wrong, and it's my biggest repeat mistake. The test is "do I need the original value back?" For login I never do. I hash what the user types and compare it to the stored hash. So it's hash, ideally salted with a slow algorithm like bcrypt.
2. Open source library with a known vulnerability, which OWASP 2025 category? I said A08. Wrong. The deciding factor is an imported component that is vulnerable, so it's A03 Software Supply Chain Failures. A08 is when integrity is never verified. My quick fix: A02 is my own setting wrong, A03 is their thing I imported, A08 is integrity never checked.
3. SLE $20,000, once every 4 years. ARO is 1/4 = 0.25 and ALE is $20,000 x 0.25 = $5,000. Got this one right.

## The scenario

A payroll SaaS vendor will store employee SSNs. Legal wants contract language that lets us verify the vendor's controls after signing.

My answer: right to audit clause, "so we can verify the vendor's controls." Right term, but my reason just restated the scenario. That's my recurring mistake of not naming the deciding factor.

The deciding factor is: the need is verification after signing, and only a contract clause gives me enforceable access to inspect the vendor on demand. Anything the vendor hands me at onboarding is a snapshot.

Why the other options lose:

| Option | Why it's not the answer |
|---|---|
| SOC 2 report or ISO 27001 cert | Due diligence evidence from one moment, not enforceable access later |
| SLA | Measures service levels like uptime, not whether security controls exist |
| NDA | Protects confidentiality, doesn't let me inspect anything |
| SOW | Scopes one project's deliverables, says nothing about oversight |

Rule of thumb: before signing is due diligence, in the contract is right to audit, after signing is ongoing monitoring. Match the verb in the scenario ("verify after") to the phase.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Three phases | Before is due diligence, during is agreements, after is monitoring |
| Right to audit | The clause that lets me verify controls after signing |
| SOC 2 / ISO 27001 | Point in time evidence, not ongoing assurance |
| SLA vs SOW | SLA is service levels, SOW is one project's scope |
| MSA | Umbrella terms, work orders sit under it |
| MOU vs MOA | MOU non binding, MOA binding |
| Hash vs encrypt | Need the original back? Yes encrypt, no hash |
| A03 vs A08 | A03 is an imported vulnerable thing, A08 is integrity never verified |

## Still to do

1. 5.4 Compliance and privacy
2. 5.5 Audits and assessments
3. 5.6 Security awareness
4. Domain 5 review quiz
5. Mixed domain review
