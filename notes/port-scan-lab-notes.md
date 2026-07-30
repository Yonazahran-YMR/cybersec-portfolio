## Objective
Generate and analyze a real port scan to understand how this attack pattern appears in raw packet captures, and correlate attacker-tool output (nmap) with defender-visible network evidence (Wireshark).

<img width="1912" height="940" alt="image" src="https://github.com/user-attachments/assets/67bd9bb0-29c8-4abe-8ddc-9e77ba68b67a" />

Locally scanning port using Wireshark and nmap.
Adapter used: Npcap Loopback Adapter

cmd: nmap -sS 127.0.0.1

Output: Source: 127.0.0.1, Same source port: 62072
        Destination: 127.0.0.1
        info: 62072 -> 445 [SYN]
              62072 -> 8888 [SYN]
              62072 -> 5900 [SYN]
              62072 -> 139 [SYN]
              62072 -> 8080 [SYN]
              . . . (Continue to dozens more ports) . . .
                
One source port (62072) sending SYN packets to a huge list of different destination ports
445, 8888, 5900, 139, 8080, 1723, 143, 21, 995, 23, 993, 111, 113, 110, 256, 53, 1720, 443, 22, 554, 135, 587, 3306, 25, 80, 3389, 1112, 1287, 1099, 8994, 43, 1801, 6101...

a rapid-fire SYN packets to many ports from one source, all within the same second (17.69... timestamps barely moving)

There are some with two exceptions at packets 4 and 49 and 54 (showing [SYN,ACK] replies):
445 -> 62072 [SYN,ACK]
135 -> 62072 [SYN,ACK]
3306 -> 62072 [SYN,ACK]
This means ports 445 (SMB), 135 (RPC), and 3306 (MySQL) on this machine are actually open/listening. nmap found real open services and everything else that got no reply is closed/filtered.
             
Findings:
- Observed what called as SYN Flood to many ports
- found 3 open services

What those 3 Open ports actually means:
445 SMB (Windows FIle Sharing Protocol. Notoriously the vector for EternalBlue/WannaCry ransomware in 2017)
135 msrpc (Windows Remote Procedure Call, used for internal Windows service communication)
3306 MySQL

Security Revelance:
If this were real external attacker scanning a machine and finding 445 (SMB) and 135 (RPC) would be a red flag. These are classic lateral movement and exploitation targets on Windows Networks. This is exactly why:
- Firewalls block inbound 445/135 from the internet by defauly on properly configured networks
- SOC Analysts immediately investigate any external scan that finds these ports open
- "Attack Surface Reduction" (closing unnecessary open ports) is a core defensive practice
