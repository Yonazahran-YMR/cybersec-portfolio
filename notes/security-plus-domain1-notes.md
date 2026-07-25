# Security+ Domain 1 Notes

## CIA Triad
- **Confidentiality** : only authorized people can see data (keyword: exposed, leaked, unauthorized viewing)
- **Integrity** : data hasn't been tampered with (keyword: altered, corrupted, modified without detection)
- **Availability** : systems/data accessible when needed (keyword: down, inaccessible, offline, DoS)

## AAA Framework
- **Authentication** : proving who you are (password, biometrics, MFA)
- **Authorization** : what you're allowed to do once verified (permissions, access control)
- **Accounting** : logging what actually happened (audit trails, logs)

## Related principles
- **Least Privilege** : give users minimum access needed for their job, nothing more
- **Zero Trust** : never trust, always verify, no automatic trust even inside the network

## Practice scenarios covered
- Ransomware = primarily Availability (Confidentiality too if data is stolen/leaked - "double extortion")
- MITM altering data = Integrity
- Accidental data exposure = Confidentiality
- DDoS + data corruption = Availability + Integrity
