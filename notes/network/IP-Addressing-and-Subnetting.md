# IP Addressing and Subnetting

Theory notes.

## The big idea

An IP address is like a street address. The network portion is the street name and the host portion is the house number. The subnet mask or CIDR prefix just tells me where the street name ends. This clicked for me because subnetting is really only one question: how many bits are locked to the network, and how many are left for hosts?

Core rules:

| Rule | Detail |
|---|---|
| IPv4 | 32 bits, written as 4 octets (0 to 255 each) |
| CIDR /n | The first n bits are the network, the rest are hosts |
| Host bits | 32 minus n |
| Total addresses | 2 to the power of host bits |
| Usable hosts | Total minus 2: the first address is the network ID, the last is the broadcast |

Cheat table (all in the last octet):

| CIDR | Mask | Total | Usable |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /30 | 255.255.255.252 | 4 | 2 |

Special ranges to know:

| Range | Meaning |
|---|---|
| 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 | Private (RFC 1918), not routed on the internet |
| 127.0.0.0/8 | Loopback, my own machine |
| 169.254.0.0/16 | APIPA, a self assigned address when DHCP fails |

Exam trap: check whether the question says "usable" or "total". Usable always subtracts 2. This is my old mistake, so I read that word before calculating.

## Warm-up: what I got right and wrong

1. PDU at Layer 2 and its address type. I said frame and MAC address, which is correct. My Why was "MAC changes at every hop," but that's a result, not the reason. The reason is that a MAC only identifies a device on its own local segment, and the router strips the frame and builds a new one for the next segment.
2. What changes when a router forwards a packet. I said both MACs, with the source becoming the router's outgoing interface and the destination becoming the next hop. Correct, and the IPs stay the same.
3. Firewall blocking a known malicious IP before any connection. I said preventive, correct. Tighter Why: it acts before the connection happens. Detective would alert after, corrective would fix after. My control type mistake didn't show up this time.

## The scenario

A new VLAN needs to hold 50 devices, and I want the smallest subnet that fits all of them. Which prefix?

My answer: /26, because it has 64 total with 62 usable and is the smallest subnet that fits 50. Correct. I used usable (62), not total (64), so the old "minus 2" mistake didn't show up.

One wording fix for myself: a bigger prefix number means a smaller subnet, because more bits are locked to the network and fewer are left for hosts. My logic was right, but I need to double check which direction I mean when I say "smaller" or "bigger."

The elimination:

| Prefix | Usable hosts | Fits 50? | Verdict |
|---|---|---|---|
| /27 | 30 | No | Too small |
| /26 | 62 | Yes | Smallest that fits |
| /25 | 126 | Yes | Fits, but wastes addresses |

Fast method for any "fit N hosts" question: add 2 to N, find the next power of 2 that covers it (50 + 2 = 52, next power of 2 is 64), so host bits = 6 and prefix = 32 minus 6 = /26.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| CIDR /n | First n bits are network, the rest are hosts |
| Total addresses | 2 to the power of host bits |
| Usable hosts | Total minus 2 (network ID and broadcast) |
| Bigger prefix number | Smaller subnet |
| Fit N hosts | Add 2 to N, round up to a power of 2, prefix = 32 minus host bits |
| Private ranges | 10/8, 172.16/12, 192.168/16 |
| 169.254.x.x | APIPA, DHCP failed |
| MAC scope | Only meaningful on its own local segment |

## Still to do

1. Ports and protocols
2. DNS
3. TLS handshake
