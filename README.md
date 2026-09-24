# Cybersecurity Journey

Documenting my path in cybersecurity from zero to professional (Blue Team/SOC focus).

## Background

Started from pre-5th-semester IT. Java, SQL, data mining foundation. Pivoting into
cybersecurity with a hands-on, lab-first approach.

## Roadmap note

Briefly considered pivoting to GRC after a rough burnout stretch. Looked into it
seriously (job market data, work-life balance, SOC to GRC mobility) but decided to
stay on the SOC/Blue Team track for now. GRC is still a real option later, once I
have actual technical credibility built up, since going SOC to GRC later is a much
easier move than the other way around. Just not the priority right now.

After finishing Security+, plan is to pivot toward Cloud Security Engineer rather
than going straight into BTL1, based on job market and salary data. BTL1 isn't
dropped forever, just deprioritized behind a cloud cert track (likely AWS Security
Specialty or AZ-500) once Security+ is done.

## Roadmap

- Phase 0-1: Networking fundamentals (done)
- Phase 2: SOC Analyst skills (current focus)
- Phase 3: Cloud security cert track (AWS/Azure) after Security+
- Phase 4: BTL1, deprioritized but not ruled out
- Phase 5: Specialize into Cloud Security Engineer, or GRC later once technical
credibility is built

## Certifications

### Target (main goal)

- 🔲 CompTIA Security+ (Domains 1-3 done, Domain 4 remaining)
- 🔲 Cloud security cert (AWS Security Specialty or AZ-500), decision pending
- 🔲 BTL1 (Security Blue Team Level 1), deprioritized

### Free supplements (in progress, no cost)

- 🔲 Google Cybersecurity Professional Certificate (Coursera, requesting campus access)
- 🔲 Google Cloud Cybersecurity Professional Certificate (Coursera, queued for after Security+)

## Progress Log

- ✅ Networking Fundamentals
  * ✅ Packet structure, protocols, OSI model (L2 MAC, L3 IP, L4 ports, L7 HTTP/DNS)
  * ✅ TCP handshake/teardown, SYN/ACK/FIN/RST flags
  * ✅ DNS query/response, transaction IDs, CNAME chains, security implications
  * ✅ Subnetting/CIDR: floor math, network/broadcast calculation
- ✅ Security+ Domain 1: CIA Triad, AAA Framework, Threat Actors, CTI Lifecycle, DAD Triad, Attack Vectors
- ✅ Security+ Domain 2 (fully closed)
  * ✅ Vulnerability Types, Zero-day vs Unpatched, Vulnerability Scanning vs Pen Testing
  * ✅ Insider Threat subtypes, Phishing/Supply Chain/Insider distinction refined
  * ✅ Security Controls: preventive/detective/corrective/deterrent/compensating, defense in depth, residual risk
  * ✅ Malware types by behavior (virus, worm, trojan, ransomware, rootkit, keylogger, spyware, logic bomb, bot/botnet)
  * ✅ Indicators of Compromise (account, network, host, application based)
  * ✅ Mitigation techniques (hardening, patch management, segmentation, compensating controls, least privilege, monitoring)
  * ✅ Threat intel sources (OSINT, closed feeds, vulnerability databases, threat feeds, ISACs, dark web monitoring, AIS/STIX/TAXII)
- ✅ Cryptography: symmetric/asymmetric encryption, hashing, salting
- ✅ Hands-on: DNS tunneling pattern simulation and detection reasoning
- ✅ Hands-on: Windows Event ID log analysis (4624/4625/4720/4728), full attack chain
brute-force to domain compromise
- ✅ Briefly explored GRC fundamentals: Risk = Likelihood x Impact, 4 treatment options
(accept/mitigate/transfer/avoid) - keeping these notes since they're still useful
context even on the SOC track
- ✅ **Security+ Domain 3 (fully closed)**
  * ✅ 3.1 Architecture Models: Zero Trust (Control/Data Plane, PDP/PEP, implicit trust), segmentation types (network, micro, DMZ, jump box), cloud shared responsibility (IaaS/PaaS/SaaS), deployment models (on-prem, hybrid, SDN, SD-WAN, SASE), IaC/serverless/microservices/containerization
  * ✅ 3.2 Secure Infrastructure: device placement, IDS vs IPS, fail-open vs fail-closed, firewall types (packet-filtering, stateful, NGFW), VPN types, attack surface reduction, proxy (forward/reverse), WAF, UTM
  * ✅ 3.3 Protect Data: data states (rest/transit/use), protection methods (encryption, hashing, masking, tokenization), data classification, data sovereignty
  * ✅ 3.4 Resilience & Recovery: RTO/RPO, high availability/redundancy, site types (hot/warm/cold), backup types (full/incremental/differential)
- 🔲 Security+ Domain 4 (Security Operations), not yet started
- 🔲 CompTIA Security+ prep

## Portfolio Projects

- ✅ **Log Parser & IOC Detection Pipeline** (`projects/log-parser-ioc-pipeline/`)
Java + MySQL pipeline that parses log data and auto-flags brute-force patterns via
a SQL trigger, mirrors the Windows Event ID attack chain I traced by hand earlier.
Full write-up, schema, trigger, and sample data in the project folder.

## Next Focus

- Hands-on session applying Domain 3 concepts (segmentation, Zero Trust, firewalls) practically, since it's been theory-heavy for a while
- Security+ Domain 4 (Security Operations) after that
- Requesting campus Coursera access, starting Google Cybersecurity Professional Certificate alongside current study
- Applying for SOC Analyst / Security Analyst internships next semester
- Working toward legitimate bug bounty hunting (HackerOne/Intigriti) as a longer-term goal

## Tools Used

Wireshark, VirtualBox, TryHackMe (free tier), Professor Messer Videos, LetsDefend (free tier), MySQL/XAMPP, Java (VSCode)

## About

Documenting my personal path from zero in cybersecurity.
