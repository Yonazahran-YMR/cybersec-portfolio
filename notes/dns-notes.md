# DNS Notes

## Core Facts
- DNS = Domain Name System — translates domain names (e.g., example.com) into IP addresses
- Operates at **OSI Layer 7 (Application)** — even though it resolves Layer 3 (IP) addresses
- Runs over **UDP port 53** by default (not TCP) — UDP chosen for speed, since DNS lookups happen constantly and don't need TCP's handshake overhead
- TCP fallback only used for large responses (zone transfers, DNSSEC) — rare exception

## Query/Response Structure
- Each query has a **transaction ID** (e.g., 0x41ad)
- Response must match the same transaction ID to be considered valid
- Mismatched transaction ID = potential **DNS spoofing/cache poisoning** indicator

## CNAME Chains
- CNAME = "Canonical Name" — DNS alias pointing to another hostname
- Example seen in capture: `www.facebook.com → CNAME → star-mini.c10r.facebook.com → A 57.144.192.1`
- Used for: load balancing, CDN routing (geographic distribution), infrastructure flexibility (backend changes without affecting client-facing domain)

## Security Implications
- **DNS tunneling**: attackers encode stolen data into DNS queries to exfiltrate data, since DNS traffic is less scrutinized than HTTP
- **DNS spoofing/cache poisoning**: attacker injects a fake response with a matching transaction ID before the real server replies, redirecting victim to malicious IP
- **Defense**: forcing all DNS through an approved internal resolver, blocking outbound UDP 53 to unauthorized external servers
