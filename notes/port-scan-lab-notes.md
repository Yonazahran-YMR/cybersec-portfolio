# Port Scan Lab (nmap + Wireshark Correlation)

## Objective
Generate a real port scan and analyze it at the packet level to understand how this attack pattern appears in raw traffic, then correlate attacker-tool output (nmap) with defender-visible network evidence (Wireshark).

## Setup
- **Tool used:** nmap
- **Capture tool:** Wireshark
- **Adapter used:** Npcap Loopback Adapter
- **Command:** `nmap -sS 127.0.0.1`
- **Target:** localhost (self-scan, safe/controlled environment)

## What the Capture Showed

One source port (`62072`) sent SYN packets to a large number of different destination ports on `127.0.0.1`, all within roughly the same second:

```
62072 → 445   [SYN]
62072 → 8888  [SYN]
62072 → 5900  [SYN]
62072 → 139   [SYN]
62072 → 8080  [SYN]
62072 → 1723  [SYN]
62072 → 143   [SYN]
62072 → 21    [SYN]
... (continues to dozens more ports)
```

**Pattern identified:** rapid-fire SYN packets from one source to many ports, timestamps barely moving.

## Open Ports Found

Three ports replied with `[SYN, ACK]`, confirming they were open/listening:

```
445  → 62072  [SYN, ACK]
135  → 62072  [SYN, ACK]
3306 → 62072  [SYN, ACK]
```

Every other port received no reply is closed or filtered. This matched nmap's own summary output exactly (445, 135, 3306 listed as open), confirming the same event was correctly observed from both the attacker's tool (nmap) and the defender's packet-level view (Wireshark).

## What These Open Ports Mean

| Port | Service | Notes |
|------|---------|-------|
| 445  | SMB (Windows File Sharing) | Notorious vector for EternalBlue/WannaCry ransomware (2017) |
| 135  | MSRPC | Windows Remote Procedure Call, internal Windows service communication |
| 3306 | MySQL | Local database service |

## Security Relevance

If this were an external attacker scanning a real target instead of a local self-scan, finding **445 (SMB)** and **135 (RPC)** open would be a major red flag. These are classic lateral movement and exploitation targets on Windows networks. This is why:

- Firewalls block inbound 445/135 from the internet by default on properly configured networks
- SOC analysts immediately investigate any external scan that finds these ports open
- **Attack Surface Reduction** (closing unnecessary open ports) is a core defensive practice

## Key Takeaway

A real port scan generates far too many packets to read line-by-line. The actual skill is recognizing the *pattern* (one source, rapid SYNs, many destination ports, mostly no replies) rather than manually inspecting every packet. In production environments, this pattern is what SIEM/IDS tools are built to auto-detect and alert on.
