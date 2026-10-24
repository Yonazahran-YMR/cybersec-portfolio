# Security Governance

Theory notes. This is the first chunk of Domain 5 (Security Program Management and Oversight), which is about 20% of the exam. It's exam content for me, and a good chance to practice reading wording carefully.

## The big idea

The analogy that worked: a city. Laws set what's required (policy). Building codes set exact measurable specs (standard). Instruction manuals set the steps (procedure). Neighbor tips are advice you can ignore (guideline).

| Document | Deciding factor | Example |
|---|---|---|
| Policy | High level, mandatory, set by management, says **what** and **why** | Acceptable use policy |
| Standard | Specific, mandatory, measurable, says **how much or which one** | Passwords at least 14 characters, AES 256 |
| Procedure | Step by step instructions, says **how to do it** | Steps to onboard a new user |
| Guideline | Recommended, **optional** | Tips for choosing a good passphrase |

| Role | One line |
|---|---|
| Owner | Accountable for the data, decides its classification |
| Controller | Decides why and how personal data is processed |
| Processor | Processes data on behalf of the controller |
| Custodian | Does the day to day protection, like backups and access |

Also on the exam: external considerations (regulatory, legal, industry, local, national, global), plus monitoring and revision, because policies have to be reviewed regularly.

## Warm-up: what I got right and wrong

1. **Which of SPF, DKIM, or DMARC proves an email wasn't altered in transit.** I described DMARC (the policy that says what to do when SPF or DKIM fail, with reports), but the question asked which one *proves* integrity. That's **DKIM**, a signature on the message. My own wording was the clue: DMARC is a policy, so it doesn't prove anything itself. This is the email trio slip again. The guest list is SPF, the wax seal is DKIM, the doorman is DMARC. Rule of thumb: "which one **proves**" means DKIM, "which one **decides what happens**" means DMARC.
2. **Critical system file quietly edited overnight.** FIM, correct, but I wrote that it alerts "when no one changes" the file, which says the opposite. The right wording: it alerts when a file changes **unexpectedly**, meaning its hash no longer matches the stored baseline.
3. **Production app showing stack traces because a debug flag was left on.** A02, correct, and my reason (the developer config was never switched off before shipping) is the right deciding factor. But the question had a second part, why not A10, and I skipped it. The answer: A10 means the code never handles a failure, while here the code is fine and a setting was left on. Multi part questions keep losing a part, so I count the parts before sending.

## The scenario

The CISO publishes a rule that all company laptops must use full disk encryption with AES 256. Which governance document is this?

I said **standard**, because it's specific, mandatory, measurable, and says how much or which one, and AES 256 is the specific part. Correct, and the reasoning tied to the scenario.

The exam trap I want to remember is how the same topic changes document type with the wording:

| Wording | Document |
|---|---|
| "Company data must be encrypted" | Policy |
| "Laptops must use AES 256 full disk encryption" | Standard |
| "Steps to enable BitLocker on a laptop" | Procedure |
| "Consider encrypting personal USB drives" | Guideline |

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| Policy | What and why, mandatory, high level |
| Standard | Specific and measurable, mandatory |
| Procedure | Step by step how to |
| Guideline | Optional advice |
| Owner | Accountable, classifies the data |
| Controller | Decides why and how personal data is processed |
| Processor | Processes data for the controller |
| Custodian | Day to day protection |

## Still to do

The roles weren't tested in the scenario, so they come up in the next warm-up. Next chunk is 5.2 Risk Management, the heaviest one in Domain 5, which may take two sessions. After that: third party risk (5.3), compliance and privacy (5.4), audits and assessments (5.5), and security awareness (5.6).
