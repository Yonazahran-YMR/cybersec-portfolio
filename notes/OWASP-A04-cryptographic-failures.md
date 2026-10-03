# OWASP A04: Cryptographic Failures

Sensitive data isn't properly protected with encryption, or encryption/hashing gets used wrong. Covers data at rest (stored) and data in transit (moving across a network).

| Example | Why it's a problem |
|---|---|
| Passwords stored in plaintext or weak hashing (MD5, SHA1) | Trivial to crack if the database leaks |
| Sensitive data sent over HTTP instead of HTTPS | Anyone on the network path can read it |
| Hardcoded encryption keys in source code | Key leaks the moment code leaks |
| Using outdated algorithms (DES, RC4) | Known weaknesses, crackable with modern hardware |
| Missing encryption for sensitive fields in a database (SSNs, credit cards) | Breach exposes raw sensitive data directly |

Core defenses: strong hashing for passwords specifically (bcrypt, Argon2, never a plain hash function), TLS everywhere for data in transit, proper key management (keys stored separately from the data they protect, rotated, never hardcoded), and encrypting sensitive fields at rest.

## Hashing vs encryption, the distinction that actually matters

Not the same thing, and the difference is about whether you ever need the original value back.

Hashing is one-way. Use it when you only ever need to verify a value, never retrieve it, passwords being the classic case. You don't decrypt a stored password to check a login, you hash what the user typed and compare hashes.

Encryption is two-way. Use it when you need the original value back later, a stored credit card number you have to submit to a processor, for example.

## Scenario I worked through

My log parser stores Windows event log data in MySQL, no passwords, just log records. Does it need encryption, hashing, both, or neither?

My first answer was "neither, it's just logs," which was the wrong test. The right test isn't "is it logs," it's "if this database leaked, is there anything here an attacker could misuse." Windows event logs (4624/4625) include usernames, source IPs, hostnames, mildly sensitive, not critical. So the honest answer: encryption at rest is a nice-to-have for defense in depth, not a hard requirement at this stage, since nothing highly sensitive is stored yet. Hashing doesn't apply at all, there's nothing here that only needs verification instead of retrieval.

## Follow-up: admin password for a future dashboard

If the project added an admin login, that password would get hashed. I initially said "hash it because it's a high privilege account," which was the wrong reasoning, privilege level has nothing to do with it. Every password gets hashed, admin or not, for the same reason: you never need the original value back, only a comparison. Encryption would be wrong here since it's reversible, if someone got the key, every plaintext password would be exposed. Hashing with bcrypt/Argon2 means even a full database leak doesn't hand over usable passwords directly, each one has to be cracked individually and slowly.

Rule to remember: it's not about privilege level, it's about whether the original value ever needs to come back. Need it back later (credit card, SSN) -> encrypt. Only ever need to verify (passwords) -> hash.

## Next up

A05 Injection.
