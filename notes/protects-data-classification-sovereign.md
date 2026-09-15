# Protect Data: Masking/Tokenization Application, Classification, Sovereignty (Sec+ Domain 3.3)

This closes 3.3. Picked up the payment processor scenario I left unfinished last time, then covered data classification and data sovereignty to close the domain out.

## Finishing the tokenization/masking scenario

Payment processor stores a random 16 digit string per transaction, means nothing on its own, actual card number lives in a separate restricted vault, only specific authorized systems can map the string back. Correctly identified this as tokenization, and explained why it's different from just hiding the number visually, the token carries zero information on its own, only meaningful by looking it up in the vault.

Second part, customer service rep's screen shows the card as 4532-****-****-1234. Correctly identified this as masking, data isn't actually altered, only the display is obscured. The part I needed to work through more was the actual risk compared to tokenization. Got there in the end: with tokenization, a database breach only gets an attacker a meaningless random string, the real number lives elsewhere. With masking, the full real card number still sits in that same record or system, just not shown on screen, so a breach that reaches the underlying data instead of just the display layer exposes the real number fully intact. The core distinction, tokenization removes the sensitive data from that location entirely, masking only controls what's displayed, not what's stored.

## Data classification

Organizing data by sensitivity level so protection effort actually scales to what matters.

| Level | Meaning | Example |
|---|---|---|
| Public | No harm if disclosed | Marketing materials, published job listings |
| Internal/Private | Not for public release, limited harm if leaked | Internal memos, org charts |
| Confidential | Real harm if disclosed | Customer PII, financial records |
| Restricted/Top Secret | Severe harm, tightest access controls | Trade secrets, classified government data |

Why this matters practically, you don't apply the same protection uniformly to everything, that wastes resources on low value data and can under protect high value data. Classification is what tells you where to actually spend the mitigation effort from Domain 2, hardening and encryption should scale with classification level, not get applied blindly everywhere.

## Data sovereignty

The legal principle that data is subject to the laws of the country where it's physically stored or collected, regardless of where the company is headquartered. This is why a company storing EU customer data on a US based cloud server can trigger conflicting legal obligations (GDPR vs US law), and why companies specifically pick cloud regions for legal compliance reasons, not just latency.

## Scenario I worked through

Healthcare company classifies patient medical records as highest sensitivity tier (encryption at rest, strict access logging, MFA required), while their public About Us page needs none of that. Correctly named data classification as the concept driving the difference, confidential vs public, tied to who should and shouldn't have access to each.

Second part, same company expanding into the EU, deciding between storing EU patient data on existing US servers or spinning up an EU specific cloud region. Correctly named data sovereignty and defined it precisely, matching the actual legal principle.

## Status

Domain 3.3 (protect data) is now fully closed. Covered: data states (rest, transit, use), protection methods (encryption, hashing, masking, tokenization), data classification, and data sovereignty.

Only Domain 3.4 (resilience and recovery) remains to fully close Domain 3, covering high availability, backups, RTO/RPO, and site considerations.
