# Risk Management

Theory notes. This is the heaviest chunk of Domain 5, so it's split in two. Part 1 (strategies, risk terms, and the formulas) is below. Part 2 (business impact analysis, risk analysis, and reporting) gets added to this same file in the next session.

## Part 1: The big idea

The analogy that worked: driving to work in a storm. I can cancel the trip (avoid), buy insurance (transfer), put on better tires (mitigate), or just go (accept).

| Strategy | Deciding factor |
|---|---|
| Avoid | Stop the risky activity entirely |
| Transfer | Shift the impact to another party: insurance, outsourcing, contract |
| Mitigate | Reduce likelihood or impact with controls |
| Accept | Knowingly live with it, with sign off from the risk owner |

| Term | One line |
|---|---|
| Risk | Likelihood times impact |
| Inherent risk | Before any controls |
| Residual risk | What remains after controls |
| Risk appetite | How much risk the organization is willing to pursue overall |
| Risk tolerance | How far it can deviate from that before it's unacceptable |
| Risk register | List of risks with owner, score, and chosen treatment |
| Qualitative | Ratings like high, medium, low |
| Quantitative | Dollar values |

## The formulas

| Formula | Meaning |
|---|---|
| Risk = Likelihood x Impact | The general idea behind every risk score |
| SLE = Asset Value (AV) x Exposure Factor (EF) | The loss from one incident |
| ARO | How many times per year the incident is expected to happen |
| ALE = SLE x ARO | The expected loss per year |

Using the numbers: a control is worth buying if its **yearly cost is less than the ALE it removes**. If the control only reduces the loss, compare the ALE before and after against the control's yearly cost.

## Warm-up: what I got right and wrong

1. **Cloud provider handling a retailer's customer data only on the retailer's instructions.** Processor, correct, because it acts only on instructions. The retailer, who decides why and how the data is used, is the controller.
2. **Six ordered steps to revoke a departed employee's access.** Procedure, correct: ordered steps for a task.
3. **Online store keeping a card number so it can charge it again next month.** Encrypt, correct, but I worded the factor as "so they can decrypt it". Tighter: the store **needs the original back** to charge the card again. That's the same yes or no test I keep drilling for hash vs encrypt, so I should say it that way.

## The scenario

A company's server is worth $200,000. A flood would destroy 50% of its value, and floods are expected once every 5 years. What is the ALE?

My work, all correct:

1. **SLE** = $200,000 x 0.50 = $100,000
2. **ARO** = 1 flood every 5 years = 1/5 = 0.20 per year
3. **ALE** = $100,000 x 0.20 = $20,000

How the exam uses the number: if a control costs less than $20,000 per year and removes most of that loss, it's worth buying. If it costs more than the ALE it removes, accepting or transferring (insurance) can be the better call.

Two traps to remember:

1. **ARO is per year.** "Twice a year" means ARO = 2, not 0.5.
2. If a control only reduces the loss, compare the ALE before and after against the control's yearly cost.

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| Avoid, transfer, mitigate, accept | Stop it, shift it, reduce it, live with it |
| Inherent vs residual | Before controls vs after controls |
| Appetite vs tolerance | How much I'll pursue vs how far I can deviate |
| SLE | AV x EF, the loss from one incident |
| ARO | Incidents per year |
| ALE | SLE x ARO, expected yearly loss |
| Control worth it? | Yearly cost less than the ALE it removes |

## Part 2 (to be added next session)

Business impact analysis (RTO, RPO, MTTR, MTBF), risk analysis, and risk reporting. My answers and corrections will go in here.

## Still to do

After 5.2: third party risk (5.3), compliance and privacy (5.4), audits and assessments (5.5), and security awareness (5.6).
