# Threat Actors & Attack Vectors

## Threat Actor Types
| Type | Motivation | Skill/Resources |
|---|---|---|
| Nation-state / APT | Espionage, geopolitical advantage | Very high (funded, patient, custom tools) |
| Organized crime | Financial gain (ransom, extortion, fraud) | High (professional, resourced) |
| Hacktivist | Ideological/political statement | Varies |
| Insider threat | Revenge, financial, negligence | High access (already inside), skill varies |
| Script kiddie | Notoriety, thrill | Low (uses existing tools) |
| Hacker for hire | Paid, no personal motive | Varies, often narrower job scope |

## Key Classifier: Motivation > Sophistication
- Skill level alone does NOT determine actor type — both nation-states and organized crime can be highly sophisticated
- Always identify the "why" first:
  - Money/extortion → Organized Crime
  - Espionage/strategic data theft → Nation-state
  - Ideology/political → Hacktivist
  - Revenge + existing access → Insider Threat

## Cyber Threat Intelligence (CTI) Lifecycle
1. Identify the most critical cyberthreats (Direction)
2. Collect threat information (Collection)
3. Process the information (Processing)
4. Analyze and look for IoCs (Analysis)
5. Disseminate the information (Dissemination)

## DAD Triad (attacker-side mirror of CIA Triad)
| CIA | DAD |
|---|---|
| Confidentiality | Disclosure |
| Integrity | Alteration |
| Availability | Denial |

## Attack Vectors (started, continue next session)
- Phishing — deceptive email/message
- Unpatched vulnerabilities — exploiting known CVEs
- Supply chain — compromising trusted third-party vendor
- Removable media — infected USB drops
- Default credentials — factory passwords never changed
- Social engineering — broader than phishing, manipulates human psychology directly (e.g., vishing/phone-based pretexting)
