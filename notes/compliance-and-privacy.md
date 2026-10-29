# Compliance and Privacy

Theory notes.

## The big idea

Compliance is like the health inspector for a restaurant. There are rules, someone checks, and failing costs real money. Privacy is the customer's recipe card: it belongs to them, and I only get to use it for the purpose they agreed to. This clicked for me because it splits cleanly into "prove I follow the rules" (compliance) and "whose data is this and who decides what happens to it" (privacy).

| Concept | What it is |
|---|---|
| Compliance reporting | Internal (to management) and external (to regulators, auditors) proof that I meet the rules |
| Compliance monitoring | Due diligence and due care, attestation and acknowledgement (people sign that they follow policy), internal and external checks, automation |
| Consequences of non compliance | Fines, sanctions, license loss, contractual penalties, reputational damage, loss of business |

Common regulations and standards:

| Law or standard | Protects | Memory hook |
|---|---|---|
| GDPR | Personal data of EU residents, wherever the company is | The EU's privacy bill of rights |
| HIPAA | Health information (US) | The doctor's vault |
| PCI DSS | Payment card data | The card network's house rules (industry standard, not a law) |
| SOX | Accuracy of public company financial reporting (US) | The honest accountant |
| GLBA | Customer financial data at banks and financial firms (US) | The bank's secrecy rule |
| FERPA | Student education records (US) | The school file |

Local note for me: Indonesia's own law is UU PDP (Law 27 of 2022), same idea as GDPR.

Privacy roles:

| Role | Meaning | Hook |
|---|---|---|
| Data subject | The person the data is about | Owner of the recipe card |
| Data controller | Decides why and how personal data is processed | The restaurant owner |
| Data processor | Processes data on the controller's behalf and instructions | The cook following orders |
| Data owner and data steward | Internal roles: accountable for the data vs managing its day to day quality | Boss vs caretaker |

Also worth knowing: right to be forgotten (erasure), data inventory, retention limits. The controller stays accountable even when a processor handles the data.

Exam trap: the law that applies follows whose data it is (where the data subject lives), not where my company sits.

## Warm-up: what I got right and wrong

1. Vendor delivering one project under an existing master contract. I said SOW and gave a decent reason, but the question had 3 parts and I only answered 1. I never named the master document, which is the MSA (the umbrella). That's my recurring mistake of skipping parts of multi part questions. My factor also just restated the scenario. Better: the deciding factor is that the scope is limited to one project, while the MSA governs the whole relationship.
2. Email control that says what to do when a message fails checks and sends reports. I said DMARC with the none, quarantine, reject policies plus reports. Correct, it's the doorman.
3. Order of volatility: RAM and running processes, disk, remote logs, backups. Correct, and it finally feels solid.

## The scenario

A retail company collects customer emails and decides which promotions to send. It hires an email marketing SaaS vendor that sends the campaigns on the company's instructions. Under GDPR terms, what role does the vendor hold?

My answer: data processor, because the vendor follows the retail company's instructions on which promotions to send. Right role, but my reason mostly retold the scenario and skipped the formal terms.

The deciding factor is: the vendor does not decide the purpose and means of processing (why the data is used and how). The retail company decides both, so the company is the data controller and the vendor is the data processor acting on its behalf. My test: who decides why the data is processed? That party is the controller.

Two things to tie together:

| Point | Why it matters |
|---|---|
| Controller stays accountable | If the vendor leaks the emails, the retail company still answers to the regulator. Hiring a processor doesn't hand off responsibility. |
| Data Processing Agreement (DPA) | The contract GDPR requires between controller and processor. It links straight back to 5.3: a third party agreement plus a right to audit. |

Why the other options lose: data subject is the customer the emails belong to. Data owner and data steward are internal roles inside one organization, not a relationship between two companies.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| GDPR scope | Follows the data subject's location, not the company's |
| HIPAA / GLBA / FERPA / SOX | Health / financial customers / students / public company finances |
| PCI DSS | Card data, an industry standard, not a law |
| Controller vs processor | Controller decides why and how, processor follows instructions |
| Accountability | The controller stays accountable even with a processor |
| DPA | The required contract between controller and processor |
| MSA vs SOW | MSA is the umbrella, SOW is one project's scope |
| Multi part questions | Count the parts before answering |

## Still to do

1. 5.5 Audits and assessments
2. 5.6 Security awareness
3. Domain 5 review quiz
4. Mixed domain review
