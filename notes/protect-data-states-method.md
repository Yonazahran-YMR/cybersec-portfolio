# Protect Data: Data States & Protection Methods (Sec+ Domain 3.3, part 1)

Starting 3.3 tonight. Opened with a review scenario on attack surface reduction vs hardening from last session, mostly right but I picked hardening when attack surface reduction was the sharper term. The distinction to remember, closing a door that shouldn't be open at all is attack surface reduction, reinforcing a door that stays open (like removing default creds on a service you're keeping) is hardening. Same pattern as before, landing in the right neighborhood but not always picking the most specific term.

## Data states

Data exists in one of three states, and the protection method depends on which one.

| State | What it means | Common protection |
|---|---|---|
| Data at rest | Stored, not moving (database, disk, backup) | Encryption (disk or file level), access controls |
| Data in transit | Moving across a network | TLS/HTTPS, VPN, encrypted tunnels |
| Data in use | Actively being processed or read in memory | Hardest to protect, encryption doesn't help here since the app needs to read it in plaintext to actually use it, secure enclaves or memory level protections are the real answer |

## Data protection methods

| Method | What it does | Reversible? |
|---|---|---|
| Encryption | Scrambles data with a key, only someone with the key can read it | Yes, by design |
| Hashing | One-way transform, produces a fixed fingerprint | No, already knew this from the crypto notes |
| Masking | Hides part of the data visually (like showing ****-1234 for a card number), underlying data may still exist in full elsewhere | Data isn't actually altered, just obscured in display or output |
| Tokenization | Replaces sensitive data with a non-sensitive substitute token, real data stored separately in a secure vault, token is meaningless without that vault | Reversible only by looking up the vault, the token itself carries zero information on its own |

## The trap that matters most

Masking vs tokenization. Both "hide" sensitive data but in different ways. Masking just obscures the display, the real data still sits in the same record, just shown partially, and can sometimes be reverse engineered from context. Tokenization actually replaces the real data with something else entirely and stores the real value somewhere separate and restricted, the token itself carries no extractable information at all.

## Scenario in progress (pick up next session)

Payment processor scenario. Database stores a random 16 digit string that means nothing on its own for each transaction, actual card number lives in a separate restricted vault, only specific authorized systems can map the string back. Separately, a customer service rep's screen shows the card number as 4532-****-****-1234.

Questions to answer next time: what technique protects the database stored value and what makes it different from just visually hiding the number, and what technique is the rep's screen using, plus the specific risk of that technique compared to the first one, tied to where the real data actually lives.

## Status

Domain 3.3 in progress. Data states and protection methods (encryption, hashing, masking, tokenization) covered conceptually, scenario application still pending. Data classification and sovereignty not yet touched.
