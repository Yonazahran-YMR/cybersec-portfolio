# Vulnerability Types & Assessment

## Vulnerability Types
| Type | Description | Example |
|---|---|---|
| Zero-day | Unknown to vendor, no patch exists | Flaw discovered/exploited before anyone knows |
| Unpatched | Known flaw, patch EXISTS but not applied | Old CVE, ignored update |
| Misconfiguration | System set up incorrectly | Public cloud storage bucket |
| Weak/default credentials | Never changed from factory default | IoT admin/admin |
| Legacy systems | Outdated, no longer supported | Windows 7 on medical devices |
| Human vulnerability | People susceptible to social engineering | Phishing victims |

## Zero-day vs Unpatched — Timeline Matters
- Classification depends on STATE AT TIME OF EXPLOITATION, not discovery
- Day 0 (discovered, no patch) = zero-day
- Day 2 (patch released) = no longer zero-day
- Day 21 (exploited, patch was available but not applied) = UNPATCHED

## Vulnerability Scanning vs Penetration Testing
| | Vulnerability Scanning | Penetration Testing |
|---|---|---|
| Method | Automated tool vs known CVE database | Human actively attempts exploitation |
| Depth | Surface-level, potential risks | Deep, proves real exploitability |
| Output | List of possible vulnerabilities (may include false positives) | Proof-of-concept, real impact |
| Example tools | Nessus, OpenVAS, Qualys | Metasploit, Burp Suite |

Key phrase: "identifies/flags without attempting to exploit" = scanning.
"Actively attempts to exploit" = pen testing.

## Distinguishing Test: Phishing vs Supply Chain vs Insider Threat
- Phishing: individual directly deceived via fake message
- Supply chain: attacker breaches a TRUSTED THIRD PARTY first, pivots through that trust
- Insider threat: person WITH legitimate access acts on their own — no third party deceived
