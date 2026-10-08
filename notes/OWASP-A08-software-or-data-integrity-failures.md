A08: Software or Data Integrity Failures

The app trusts code or data without verifying it hasn't been tampered with. The missing step is an integrity check.

Example	Why it's a problem
Auto-update downloads and installs without verifying a signature	A swapped installer runs with full trust
Insecure deserialization (Java ObjectInputStream on untrusted data)	Attacker-crafted objects can run code during deserialization
CI/CD pipeline pulls artifacts that aren't signed or verified	Tampered build output ships to production
Third-party script loaded from a CDN with no Subresource Integrity (SRI) hash	If the CDN is compromised, your page runs the attacker's script

Core defenses: digital signatures and checksum verification on anything you download or deploy, SRI hashes for external scripts, never deserializing untrusted data, and signed, access-controlled CI/CD pipelines.

Quick way to separate it from A03: A03 asks whether the thing you pulled in is itself vulnerable or compromised. A08 asks whether you ever verified that what arrived is untampered.

