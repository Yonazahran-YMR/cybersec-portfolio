# OWASP A08: Software or Data Integrity Failures

The app trusts code or data without verifying it hasn't been tampered with. The missing piece is always an integrity check.

| Example | Why it's a problem |
|---|---|
| Auto-update downloads and installs without verifying a signature | A swapped installer runs with full trust |
| Insecure deserialization (Java `ObjectInputStream` on untrusted data) | Attacker-crafted objects can run code during deserialization |
| CI/CD pipeline pulls artifacts that aren't signed or verified | Tampered build output ships to production |
| Third-party script loaded from a CDN with no Subresource Integrity (SRI) hash | If the CDN is compromised, the page runs the attacker's script |

Core defenses: digital signatures and checksum verification on anything downloaded or deployed, SRI hashes for external scripts, never deserializing untrusted data, and signed, access-controlled CI/CD pipelines.

## A03 vs A08, the split that finally clicked

They overlap a lot in real incidents, so the trick is which failure I'm naming.

| Category | The question it asks |
|---|---|
| A03 | Is the thing I pulled in vulnerable or compromised? |
| A08 | Did I ever verify that what arrived is untampered? |

Exam shortcut: if the answer to "what would have stopped this?" is a signature or an integrity check, it's A08.

## Scenario I worked through

A desktop app checks for updates, downloads the installer from the vendor's server, and runs it automatically. An attacker compromises the download server and swaps in a malicious installer.

1. The check that would reject the swapped file is digital signature verification. I said "cryptographic check," right direction but missing the formal term. The vendor signs the installer with a private key, and the app verifies that signature against the vendor's public key before running anything. A swapped file can't carry a valid signature. A published checksum comparison is the lighter version of the same idea, but a signature is stronger because an attacker who controls the server could replace the checksum too.
2. It's A08, not A03. I guessed A03 because the compromised vendor server feels like supply chain, and it's a fair instinct since real incidents often touch both. But the flaw this scenario is built around is that the app ran the file with zero verification. That missing check is what makes it A08.

## Review slips from this round

1. The A07 flaw: I said the fix was "authenticate after the second factor," which is right, but missed the term. After the password step the session should sit in a pending MFA state, not an authenticated one.
2. Hash vs encrypt, third time I've landed on the right action with the wrong reason. Sensitivity only decides whether a field needs protection. Retrieval decides the method. Need the original back later (SSN to display) means encrypt. Only ever compare it (password) means hash. Also, the SSN gets encrypted, decrypting is what happens later when it's read.

## Next up

A09 Security Logging and Alerting Failures.
