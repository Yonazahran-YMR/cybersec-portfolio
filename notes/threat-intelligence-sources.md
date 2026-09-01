# Threat Intelligence Sources

Last piece of Domain 2. This ties straight back to the CTI Lifecycle from Domain 1 (direction, collection, processing, analysis, dissemination). Today was basically filling in what actually feeds the collection stage.

## The sources

| Source type | What it is | Example |
|---|---|---|
| OSINT | Publicly available info, no special access needed | Security blogs, news, social media, public breach reports |
| Closed or proprietary feeds | Paid threat intel subscriptions | Vendor curated commercial TI platforms |
| Vulnerability databases | Catalogs of known vulns | CVE (the naming standard) plus NVD (the scored database, adds CVSS severity) |
| Threat feeds | Real time streams of known bad indicators | IP blocklists, malicious domain lists, malware hash feeds |
| Information Sharing Centers | Industry specific collaborative sharing | ISACs, financial sector sharing threat data with other banks for example |
| Dark web monitoring | Tracking underground forums and marketplaces | Leaked credential dumps, stolen data for sale |
| AIS (Automated Indicator Sharing) | Machine speed sharing between orgs or government | STIX/TAXII protocols, structured format for automated exchange |

## The distinction that mattered most

CVE vs NVD. CVE is just the identifier or naming convention, like CVE-2024-1234. NVD is the enriched database that actually scores it with CVSS and adds detail. So CVE tells you what it is, NVD tells you how bad it is. This came up directly in my scenario and I got it right by naming both pieces separately instead of just saying "vulnerability database" as one blob.

## Scenario I worked through

A SOC analyst is investigating an alert. To check if a flagged IP is a known malicious C2 server, they cross reference it against a real time list of confirmed bad IPs from a commercial vendor. Separately they look up a CVE number found in the malware's exploit code to check its severity.

For the IP check, that's a threat feed, real time confirmed bad IP list. For the CVE severity lookup, that's the vulnerability database, specifically CVE giving the identifier and NVD giving the actual severity score. Got both right, no corrections needed this round.

## Status

Domain 2 is fully closed out now. Vuln types, scanning vs pen testing, security controls, malware types, IoCs, mitigation techniques, and threat intel sources are all done. Moving into Domain 3 (architecture, zero trust) next session with nothing left underneath it.
