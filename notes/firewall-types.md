# Firewall Types (Sec+ Domain 3.2)

## The three firewall types

| Type | How it inspects | Awareness level |
|---|---|---|
| Packet-filtering | Checks headers only, source and dest IP, port | No context, can't tell if traffic is part of a legitimate ongoing session |
| Stateful | Tracks connection state, is this packet part of an already established session | Knows session context, blocks unsolicited or out of sequence packets |
| NGFW (Next-Gen Firewall) | Inspects actual application layer content, can identify the app itself | Full context, can tell apart legitimate traffic from malicious payload even if both use the same port |

## The distinction that mattered most

Packet-filtering vs stateful isn't about what they check, both look at headers. It's whether they remember. Packet-filtering evaluates each packet in isolation. Stateful maintains a connection table, so if a packet claims to be a response to an outbound request that was never actually sent, stateful catches that as spoofed, packet-filtering has no way to catch it since it never tracks session state at all.

## Scenarios I worked through

**Spoofed response scenario.** A packet claims to be a response to an outbound request that was never sent. Correctly identified packet-filtering as the type that would miss this (headers only, no session tracking) and stateful as the type that would catch it, since it cross references incoming packets against an actual connection table.

**Data exfiltration over port 443 scenario.** Stateful firewall allows outbound traffic on port 443 since it looks like a normal, properly established HTTPS session, but it's actually a compromised laptop exfiltrating data disguised as regular web traffic. Stateful lets it through because the session itself is legitimate looking, established properly, in sequence, it just has zero visibility into what the traffic actually contains. Upgrading to NGFW catches it because NGFW inspects the actual application layer content, not just port and session state, so it can tell the difference between real browsing and exfiltration even when both are using the same port. Got both parts of this right, correctly separated "session looks legitimate" from "content is legitimate" as two different things stateful can't distinguish between.

## Status

Domain 3.2 progress: device placement (IDS vs IPS), fail-open vs fail-closed, and firewall types (packet-filtering, stateful, NGFW) are all covered and solid. Remaining in 3.2: attack surface reduction, VPN, and a few smaller infrastructure topics.
