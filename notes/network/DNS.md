# DNS

Theory notes.

## The big idea

DNS is the internet's phone book. I know the name (example.com), the network needs the number (the IP address), and a resolver does the lookup for me. This clicked for me because every attack here is just someone messing with the phone book: forging an entry, copying the whole book, or smuggling notes through the requests.

Resolution flow, what happens when I type a name:

| Step | Who | What it does |
|---|---|---|
| 1 | Local cache and stub resolver on my device | Checks if it already knows the answer |
| 2 | Recursive resolver (my ISP, or 8.8.8.8) | Does the hunting for me, and caches the result |
| 3 | Root server | Points to the right TLD server (.com, .id) |
| 4 | TLD server | Points to the domain's authoritative server |
| 5 | Authoritative server | Holds the real record and gives the final answer |

Record types:

| Record | Maps | Hook |
|---|---|---|
| A | Name to IPv4 | The street address |
| AAAA | Name to IPv6 | The longer street address |
| CNAME | Name to another name (alias) | A nickname |
| MX | Domain to its mail server | The post office |
| NS | Domain to its authoritative name servers | Who to ask |
| PTR | IP to name (reverse lookup) | Reverse phone book |
| TXT | Free text, used for SPF, DKIM, DMARC | The notes field |
| SOA | Zone admin info, serial number | The zone's ID card |

Port 53 uses UDP for normal queries and TCP for large replies and zone transfers.

Attacks and defenses:

| Item | What it is | Hook |
|---|---|---|
| Cache poisoning | Forged records injected into a resolver's cache, so users get sent to the attacker's IP | A fake page in the phone book |
| DNSSEC | Digitally signs DNS records so resolvers verify authenticity and integrity | The wax seal on each entry |
| DoH and DoT | Encrypt the query between client and resolver, giving privacy | A sealed envelope |
| DNS tunneling | Data hidden inside DNS queries to exfiltrate or run C2 | Smuggling notes inside phone book requests |
| Zone transfer (AXFR) | Copies a whole zone, so restrict it to authorized servers | Handing out the full phone book |
| DNS sinkhole | Returns a fake or blocked answer for malicious domains | A dead end for known bad addresses |

Exam trap: DoH and DoT encrypt the path, DNSSEC proves the answer is genuine. Encryption does not stop a forged record. Only signatures do.

## Warm-up: what I got right and wrong

1. Smallest subnet for 100 devices. I said /25, with 128 total and 126 usable. Correct. One fix: /24 also fits 100 hosts, it just isn't the smallest that fits, so "too many" should have been "wastes addresses." Fast check: 100 + 2 = 102, next power of 2 is 128, so 7 host bits and 32 minus 7 = /25.
2. Secure replacement for plaintext LDAP. I said LDAPS on port 636, because it encrypts traffic between client and server. Correct, and all 3 parts were answered.
3. The email "guest list" control. I said SPF, and contrasted DKIM (signature for integrity) and DMARC (policy for failures plus reports). Correct. The email trio is solid now.

## The scenario

An attacker injects a forged A record into a company's DNS resolver, so users who type the bank's domain land on the attacker's server. The company wants the resolver to verify that answers really come from the authoritative server and weren't altered. Which control?

My answer: DNSSEC, because it adds cryptographic signatures to DNS records so the resolver can verify the answer is authentic and not altered. Correct, and both parts were answered.

The contrast that wins exam questions: DoH and DoT encrypt the query between client and resolver, so they give privacy. They don't prove the answer is genuine. A forged record delivered over an encrypted channel is still forged. Only signatures (DNSSEC) prove authenticity and integrity.

Why the other options lose:

| Option | Why it's not the answer |
|---|---|
| DoH or DoT | Protects the path (privacy), can't verify the answer |
| DNS sinkhole | Blocks known bad domains, doesn't validate records |
| Restricting zone transfers | Stops copying the whole zone, unrelated to forged answers |
| Short TTL | Shrinks how long poison lasts, doesn't prevent it |

Connection to my old test: DNSSEC uses signatures, which prove who sent it and that it wasn't changed, but they don't hide the content. Records are still readable by anyone. That's integrity and authenticity, not confidentiality.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Resolution order | Cache, recursive resolver, root, TLD, authoritative |
| A / AAAA | Name to IPv4 / IPv6 |
| MX / NS / PTR | Mail server / name servers / reverse lookup |
| TXT | Where SPF, DKIM, DMARC live |
| Port 53 | UDP for queries, TCP for large replies and zone transfers |
| Cache poisoning | Forged record sits in the resolver's cache |
| DNSSEC | Signatures give authenticity and integrity |
| DoH and DoT | Encryption gives privacy, not authenticity |

## Still to do

1. TLS handshake
