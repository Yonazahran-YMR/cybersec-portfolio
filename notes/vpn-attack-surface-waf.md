# VPN, Attack Surface, Proxy/WAF/UTM (Sec+ Domain 3.2 close-out)

This closes out 3.2. Opened with a review on firewall types from last session (NGFW vs stateful confidence question, both parts correct), then covered VPN types and attack surface, then proxy/WAF/UTM to finish out the domain.

## VPN types

VPN is an encrypted tunnel between endpoints over an untrusted network like the internet.

| Type | What it connects | Use case |
|---|---|---|
| Site-to-site | Two networks, like branch office to HQ | Always-on, no individual user action needed |
| Client-to-site (remote access) | One user's device to a network | Remote employee connecting in |
| Full tunnel | All of the user's traffic routes through the VPN | More secure, but slower, more bandwidth on the company's end |
| Split tunnel | Only traffic destined for the company goes through VPN, rest goes direct to internet | Faster, less company bandwidth, but exposes the user's other traffic outside the encrypted tunnel |

The trap here, split tunnel's tradeoff isn't about connection quality, it's about what's actually protected. If the user's device gets compromised through the unprotected part of split tunnel traffic, that compromised device still has an open path straight into the company network through the tunnel itself. The VPN encrypting company traffic doesn't stop a bad actor already sitting on the device.

## Attack surface

The sum of every point an attacker could potentially get in, open ports, exposed services, user accounts, endpoints, APIs. Attack surface reduction means actively shrinking that list, closing unused ports, removing unnecessary services, disabling unused accounts. Ties straight back to hardening from Domain 2.

## Proxy, WAF, UTM

| Concept | What it does | Key distinction |
|---|---|---|
| Proxy server | Sits between user and destination, forwards requests on their behalf | Forward proxy protects and filters outbound user traffic (company blocking social media for example). Reverse proxy sits in front of servers, protects inbound traffic to them, hides real server IPs, load balances |
| WAF (Web Application Firewall) | Filters HTTP/HTTPS traffic to web apps specifically, looks for attack patterns like SQL injection and XSS in the actual request content | Narrower than NGFW, purpose built for web app layer attacks, not general traffic |
| UTM (Unified Threat Management) | All-in-one appliance, bundles firewall, antivirus, IDS/IPS, content filtering into one box | Convenience and cost play for smaller orgs, single point of management, but also a single point of failure |

WAF vs NGFW distinction that mattered, both inspect content, but WAF is purpose built specifically for web application attacks (SQLi, XSS, patterns targeting how web apps process input), while NGFW is broader, general application identification across many protocols, not just HTTP.

## Scenarios I worked through

**Split tunnel compromise scenario.** Remote employee on split tunnel VPN gets malware through unencrypted, unmonitored home traffic, malware then rides the VPN connection into the company file server. Correctly identified split tunnel as the cause, since it only protects company bound traffic, not the user's other traffic where the malware actually got in. Follow up asked what would have prevented it, said full tunnel correctly but only restated the definition instead of walking the actual mechanism. Correction: full tunnel means the malicious ad traffic would also route through the company's own security controls (firewall, IDS/IPS), so it likely gets caught before ever infecting the laptop in the first place, no infected device, no way to abuse the VPN connection afterward. Lesson here, trace the full cause and effect chain, not just state the definition of the fix.

**Exposed FTP port scenario.** Public web server has 12 open ports including an old, forgotten FTP service on port 21 with default admin creds. Attacker bypasses a fully configured full tunnel VPN entirely by just going straight for the exposed FTP port. Correctly reasoned the VPN had zero relevant role here since it protects a completely separate access path. Correctly named the fix actions (close unused ports, remove default credentials) but didn't name the actual technique term, attack surface reduction (closing the port removes the entry point) combined with hardening (removing default creds). Pattern worth watching, I keep landing on the right action but not always naming the formal term behind it, worth practicing "what is this called" as a reflex, since the actual exam asks for the term, not a description.

**WAF and reverse proxy scenario.** SQL injection attempt against a login form gets blocked by an appliance inspecting actual HTTP request content, that's WAF, correctly named with the right reasoning (SQLi pattern recognition, not generic firewall). Separately, the real server IP is hidden behind an appliance that forwards requests to it, correctly identified as reverse proxy, right direction and right reasoning (sits in front of servers, hides real IP, protects inbound traffic).

## Status

Domain 3.2 (secure infrastructure) is now fully closed. Covered across sessions: device placement and IDS vs IPS, fail-open vs fail-closed, firewall types (packet-filtering, stateful, NGFW), VPN types (site-to-site, client-to-site, full tunnel, split tunnel), attack surface reduction, and proxy/WAF/UTM.

Only 3.3 (protect data: data states, encryption, masking, tokenization, classification) and 3.4 (resilience and recovery: high availability, backups, RTO/RPO) remain in Domain 3.
