# Ports and Protocols

Theory notes.

## The big idea

An IP address is the building, the port is the apartment door number, and the protocol is the language spoken behind that door. This clicked for me because it explains how one server can run a website, SSH, and a database at once: same building, different doors.

TCP vs UDP:

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None |
| Reliability | Acknowledged, ordered, retransmits | Best effort |
| Speed | Slower | Faster |
| Hook | Registered mail | A postcard |
| Typical use | Web, email, SSH | DNS queries, DHCP, streaming, NTP |

Ports to know:

| Port | Protocol | Secure? |
|---|---|---|
| 20/21 | FTP | No |
| 22 | SSH, SFTP, SCP | Yes |
| 23 | Telnet | No |
| 25 | SMTP | No |
| 53 | DNS | No (UDP normally, TCP for large replies and zone transfers) |
| 67/68 | DHCP | n/a |
| 80 | HTTP | No |
| 110 / 143 | POP3 / IMAP | No |
| 389 | LDAP | No |
| 443 | HTTPS | Yes |
| 445 | SMB | n/a (common attack target) |
| 465 / 587 | SMTP secure | Yes |
| 636 | LDAPS | Yes |
| 993 / 995 | IMAPS / POP3S | Yes |
| 3306 | MySQL | n/a |
| 3389 | RDP | n/a |

Insecure to secure swaps:

| Insecure | Replace with |
|---|---|
| Telnet (23) | SSH (22) |
| FTP (21) | SFTP (22) or FTPS |
| HTTP (80) | HTTPS (443) |
| LDAP (389) | LDAPS (636) |
| POP3 / IMAP | POP3S / IMAPS (995 / 993) |

Exam trap: the port number alone proves nothing. Malware can run on any port, and a web server can listen on 8080. The port tells me the expected service, not the actual one.

## Warm-up: what I got right and wrong

1. /27 usable hosts. I said 30, because /27 has 32 total and 2 are for the network and broadcast addresses. Correct, and I named both of the 2. The old "minus 2" mistake is gone.
2. Frame from Router 1 to Router 2, what stays and what changes. I said the IP stays and the MAC is rewritten for the next hop. Correct, but my Why was thin. The reason: a MAC only identifies a device on its local segment, so each router builds a new frame for the next segment.
3. App crashes on an unhandled null and prints a stack trace, which OWASP 2025 category? I said A10 Mishandling of Exceptional Condition, and the number was right. My Why drifted, though. The name is Exceptional Conditions (plural), and the deciding factor is that the code never handles the failure. The stack trace leak is a consequence, not the category test.

## The scenario

An admin manages a Linux server remotely using Telnet, so credentials and commands cross the network in plaintext. I need an encrypted remote command line replacement. Which protocol and which port?

My answer: SSH on port 22, because it encrypts the whole session. Correct, and all 3 parts were answered (protocol, port, Why). I had a stray "and the Standard" at the end of my reason that wasn't clear, so I'm dropping it. The strong version is the contrast: Telnet sends credentials and commands in plaintext, so anyone sniffing the network can read them. SSH encrypts the whole session and also authenticates the server with host keys, with optional key based login instead of passwords.

Why the other options lose:

| Option | Why it's not the answer |
|---|---|
| HTTPS (443) | Encrypted, but it's web traffic, not a remote command line |
| RDP (3389) | Remote desktop (graphical), mainly Windows, not a command line |
| SFTP or SCP (22) | File transfer built on SSH. Same port, different job |
| FTP (21) | Plaintext file transfer, wrong job and not encrypted |

Detail worth keeping: SSH, SFTP, and SCP all share port 22. If the question says "secure file transfer on port 22", that's SFTP. If it says "encrypted remote command line", that's SSH.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| TCP vs UDP | Registered mail (handshake, reliable) vs postcard (fast, no guarantee) |
| Port 22 | SSH, SFTP, SCP |
| Port 23 vs 22 | Telnet plaintext, replaced by SSH |
| Port 80 vs 443 | HTTP plaintext, HTTPS encrypted |
| Port 389 vs 636 | LDAP plaintext, LDAPS encrypted |
| Port 3389 | RDP, remote desktop |
| Port 445 | SMB, a common attack target |
| Port alone proves nothing | It shows the expected service, not the actual one |

## Still to do

1. DNS
2. TLS handshake
