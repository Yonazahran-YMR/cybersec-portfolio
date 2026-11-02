# Encapsulation and PDUs

Theory notes.

## The big idea

Encapsulation is like sending a gift by courier. The gift goes in a box (Layer 4), the box gets a shipping label with the destination city (Layer 3), then it goes on a courier truck that only knows the next depot (Layer 2). Every handler reads only its own label, and the receiver unwraps layer by layer. This clicked for me because it explains why a router can forward my traffic without ever caring what's inside the box.

The sending side wraps (encapsulation), the receiving side unwraps (decapsulation).

| OSI layer | PDU name | Address it uses | Hook |
|---|---|---|---|
| 7, 6, 5 | Data | None | The gift |
| 4 Transport | Segment (TCP) or Datagram (UDP) | Port | The box number |
| 3 Network | Packet | IP address | The city label |
| 2 Data Link | Frame | MAC address | The next depot only |
| 1 Physical | Bits | None | The road |

TCP/IP model, which is what real networks use:

| TCP/IP layer | Matches OSI |
|---|---|
| Application | 5, 6, 7 |
| Transport | 4 |
| Internet | 3 |
| Network Access | 1, 2 |

Exam trap: IP addresses stay the same end to end (ignoring NAT), but MAC addresses change at every hop, because a MAC only matters on the local network segment.

## Warm-up: what I got right and wrong

1. List the 7 OSI layers in order. I wrote Physical, Data Link, Network, Transport, Session, Presentation, Application. Correct. All I knew about networking before this was the OSI layers, so this is my base.
2. Firewall blocks TCP port 3389 from any source, which layer? I said Layer 4, Transport, port based filtering. Correct. A port number lives in the TCP or UDP header, so port filtering is Layer 4. The old L3 vs L4 mistake didn't show up.
3. Database backup that must be restorable to the exact original data, hash or encrypt? I said encrypt, because hash is one way. Correct. Tighter reason: the backup must return the original data, and only encryption does that.

## The scenario

A laptop sends a request to a web server on another network, passing through two routers. At each hop, which address is rewritten, the MAC or the IP?

My answer: destination MAC, IP stays the same end to end, MAC changes because it only matters on the local segment. Mostly correct. My reason was exactly right, but I missed that both the source and destination MAC are rewritten at every hop.

Why both MACs change: the router receives the frame, strips the Layer 2 header (decapsulation), reads the destination IP, picks the next hop, then builds a new frame. The new source MAC is the router's own outgoing interface, and the new destination MAC is the next hop's interface, found with ARP. The IP packet inside is untouched.

Per hop view:

| Segment | Source MAC | Destination MAC | Source IP | Destination IP |
|---|---|---|---|---|
| Laptop to Router 1 | Laptop | Router 1 | Laptop | Server |
| Router 1 to Router 2 | Router 1 | Router 2 | Laptop | Server |
| Router 2 to Server | Router 2 | Server | Laptop | Server |

My test to remember: the MAC columns change every row, the IP columns never change.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Encapsulation | Sender wraps layer by layer, receiver unwraps |
| PDU names | Data, segment or datagram, packet, frame, bits |
| Layer 4 | Ports, TCP or UDP |
| Layer 3 | IP addresses, packets, routers |
| Layer 2 | MAC addresses, frames, switches |
| IP across hops | Stays the same end to end (ignoring NAT) |
| MAC across hops | Both source and destination rewritten at every hop |
| Hash vs encrypt | Need the original back? Yes encrypt, no hash |

## Still to do

1. IP addressing and subnetting (this is where my old "usable hosts minus 2" mistake lives)
2. Ports and protocols
3. DNS
4. TLS handshake
