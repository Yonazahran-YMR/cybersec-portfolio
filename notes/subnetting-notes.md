# Subnetting & CIDR Notes

## Core Concept
- IPv4 address = 32 bits total (4 octets × 8 bits)
- CIDR (/24, /25, etc.) = how many bits are locked as "network," rest are free for hosts
- Free bits determine subnet size: 2^(free bits) = total addresses

## Key Table
| CIDR | Free bits | Total addresses (2x2x2x...) | Usable hosts  |
|------|-----------|-----------------|--------------|
| /24  |     8     |     256         |     254      |
| /25  |     7     |     128         |     126      |
| /26  |     6     |     64          |     62       |
| /27  |     5     |     32          |     30       |
| /28  |     4     |     16          |     14       |

## Formulas
- Total addresses = 2^(free bits)
- Usable hosts = Total addresses - 2 (network (front)+ broadcast(rear))
- Broadcast address = Network address + (block size - 1)

## Finding which subnet an IP belongs to
1. Calculate floor/block size from CIDR
2. List floor boundaries (0 to size-1, size to size×2-1, etc.)
3. Find which floor range contains the target IP's last octet
4. That floor's start = network address, end = broadcast address

## Below /24
- /24 and smaller (/25-/32): subdividing within ONE octet (256 baseline)
- Below /24 (/16, /8, etc.): multiple octets become free
  - /16 = 2 octets free = 65,536 addresses
  - /8 = 3 octets free = 16,777,216 addresses

## Security relevance
Subnetting enables network segmentation: isolating traffic between departments/zones (e.g., Guest WiFi vs Engineering). Malware in one subnet can't directly reach another without passing through a router/firewall enforcing rules.
