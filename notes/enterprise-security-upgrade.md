# Enterprise Security Upgrades

## The big idea

The analogy I used: upgrading a building with a gate, guards, mail screening, document seals, exit bag checks, and a visitor desk. Each control guards a different door.

| Control | One line |
|---|---|
| Firewall | Rules checked top to bottom, first match wins, implicit deny at the end |
| IDS | Only detects and alerts, sits out of band |
| IPS | Sits inline and can block |
| Web filter, DNS filter | Block sites by category or reputation. DNS filtering stops the lookup of a bad domain before any connection happens |
| SPF | Which servers may send mail for my domain (the guest list) |
| DKIM | A signature proving the mail came from the domain and wasn't altered (the wax seal) |
| DMARC | Policy telling receivers what to do when SPF or DKIM fail: none, quarantine, or reject, plus reports (the doorman) |
| FIM | Hashes critical files and alerts when one changes |
| DLP | Stops sensitive data leaving through email, USB, or cloud upload |
| NAC | Checks a device's posture (patched, antivirus on) before it joins the network |
| EDR | Watches and responds on endpoints |
| XDR | EDR plus network, cloud, and email data |
| UBA | Baselines normal user behavior and flags deviations |
| OS security | GPO (central Windows settings), SELinux (mandatory access control on Linux) |
| Secure protocols | Replace Telnet with SSH, HTTP with HTTPS, FTP with SFTP |

## Warm-up: what I got right and wrong

1. **SOAR playbook that auto disables an account after one failed login alert.** I said the risk is DoS, which is right: an attacker can lock out legitimate users on purpose, and one failed login is a false positive trap. My fix, "implement a content aware trigger", was too vague because it doesn't say what changes. Concrete fixes: require a threshold and window (5 failures in 5 minutes), disable temporarily instead of permanently, and keep human approval for privileged accounts.
2. **Customer emails that support staff must read and reply to.** I said encrypt, correct. Better phrasing of the deciding factor: "I need the original back", instead of "so it can be decrypted".
3. **Reset handler that catches an exception and logs the user in anyway.** A10 Mishandling of Exceptional Conditions, because the app fails open. Correct.

## The scenario

1. **Attacker emails staff as the CEO from an outside server using my domain. Which control tells receivers to reject it?** I said DKIM, wrong. The correct answer is **DMARC**. The attacker's server isn't on my domain's allowed list, so SPF fails, and it can't produce my domain's signature, so DKIM fails. But SPF and DKIM only perform the checks. The control that tells receivers what to do when they fail is DMARC. Memory trick: SPF is the guest list, DKIM is the wax seal, DMARC is what the doorman does when either one fails.
2. **Employee copies the customer database to a USB drive.** DLP. Correct.
3. **Unpatched personal laptop plugs into the office network.** NAC. Correct.
4. **Someone quietly edits a system config file overnight.** I said OS security, wrong. The correct answer is **FIM**. OS security (GPO, SELinux) enforces settings, but it doesn't alert on a quiet edit. The deciding phrase was "quietly edits a file", which means detecting a change, and that's FIM. This is a "right area, wrong tool" slip.
5. **Which of IDS or IPS can stop an attack?** IPS, because it sits inline and blocks, while IDS only detects and alerts out of band. Correct, and my reasoning (inline vs out of band) was the right deciding factor.

## Quick recap for future me

| Situation | Control |
|---|---|
| Spoofed sender domain, receiver must reject | DMARC (backed by SPF and DKIM checks) |
| Data leaving on USB, email, or upload | DLP |
| Unpatched device joining the network | NAC |
| Quiet change to a critical file | FIM |
| Need to block an attack in line | IPS |
| Only alert on an attack | IDS |
| Bad domain lookup | DNS filter |
| Odd behavior of a normal user | UBA |

## Still to do

Next is 4.6 Identity and Access Management, then the missing incident response pieces (4.8), then the Domain 4 review quiz.
