# Audits and Assessments

Theory notes.

## The big idea

An audit is an inspector with a checklist. An assessment is a health checkup that tells me how I'm doing. A penetration test is hiring someone to actually try breaking in. This clicked for me because the three answer different questions: "do I follow the rules," "how healthy am I," and "can someone really get in."

Audit and assessment types:

| Type | What it is | Hook |
|---|---|---|
| Internal audit | Own staff or audit committee checks compliance with policy | Checking my own homework |
| Self assessment | Team scores itself against a framework | Grading myself |
| External audit | Independent party, often required by regulators or customers | A stranger grades me |
| Regulatory examination | Government or industry body inspects | The official inspector |
| Attestation | Formal statement from an auditor (or signed by management) that controls exist and work | The signed certificate |

Penetration test environment types (how much the tester knows going in):

| Type | Tester knowledge | Hook |
|---|---|---|
| Known environment (white box) | Full: diagrams, source, credentials | Given the blueprints |
| Partially known (gray box) | Some, for example a user account | Given a visitor badge |
| Unknown environment (black box) | Nothing but a target name | A real outsider |

Reconnaissance: passive means no direct contact with the target (OSINT, public records), active means interacting with it (port scans, probing). Other test flavors: physical, offensive (red), defensive (blue), integrated (both together).

Exam trap: rules of engagement and written authorization come before testing starts. Without them, it's an attack.

## Warm-up: what I got right and wrong

1. Legacy server that can't be patched, isolated on a restricted segment. I said segmentation. That's the mitigation category (the technique), but the formal term the exam wants is compensating control. This is my recurring mistake #4, mitigation category vs the term. The deciding factor is that the primary fix (patching) is impossible, so a substitute control covers the gap. My reason also just retold the scenario.
2. App crashes on an unhandled null and dumps a stack trace. I said A10 but wrote the name wrong ("Unexception Conditional"). The correct name is A10 Mishandling of Exceptional Conditions. The deciding factor is that the code never handles a failure. Good news: I stayed on 2025 numbering, no 2021 slip this time.
3. GDPR role that decides why and how data is processed, plus the required contract. I said data controller and DPA. Correct on both parts, so counting the parts worked.

## The scenario

A company hires a penetration tester and gives only the company name and one public IP range. No diagrams, no credentials, nothing else. Which environment type is this?

My answer: unknown environment (black box), because the company gives nothing beyond a public IP range any outsider could find. Correct, and I gave both names. My reason retold the scenario though, so recurring mistake #1 showed up lightly.

The deciding factor is: the tester starts with no prior knowledge of the internal environment (no diagrams, source, or credentials), which simulates a real outside attacker. My test: how much does the tester know going in? Nothing internal means unknown environment.

Why the other options lose:

| Option | Why it's not the answer |
|---|---|
| Known environment (white box) | Would include diagrams, source, or credentials |
| Partially known (gray box) | Would include something like a low privilege user account |

One nuance I want to remember: a company name and an IP range are just the scope, the target definition. Every test needs a scope, so receiving one doesn't make it partially known. That's a common distractor. Scope and authorization live in the rules of engagement, which must be agreed in writing before testing starts.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Internal vs external audit | Own staff vs independent party |
| Attestation | Formal signed statement that controls exist and work |
| White / gray / black box | Known / partially known / unknown environment |
| Scope is not knowledge | A target and IP range doesn't make it gray box |
| Passive vs active recon | No contact with target vs interacting with it |
| Rules of engagement | Written authorization and scope before testing, or it's an attack |
| Compensating control | Substitute control when the primary fix (patching) is impossible |
| A10 | Mishandling of Exceptional Conditions: code never handles a failure |

## Still to do

1. 5.6 Security awareness
2. Domain 5 review quiz
3. Mixed domain review
