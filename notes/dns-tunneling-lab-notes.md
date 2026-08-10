# DNS Tunneling - What Suspicious DNS Traffic Actually Looks Like

<img width="1915" height="940" alt="Screenshot 2026-08-10 183021" src="https://github.com/user-attachments/assets/4d6d7270-f1cc-4407-a603-12c392c3201b" />

Follow-up to my earlier DNS capture notes. This time instead of just looking at normal
DNS resolution, I wanted to see what an unusual/suspicious pattern looks like, since
tunneling was something I only knew about in theory before this.

## What I did

Generated a burst of DNS queries myself using a simple loop in cmd:
```
for /L %i in (1,1,20) do nslookup test%i.example.com
```

Captured it in Wireshark on my Ethernet interface, filtered with `dns`.

## What showed up

Got a clean sequence like:
```
test3.example.com
test4.example.com
test5.example.com
test6.example.com
```
Each one queried for both A and AAAA records back to back, resolving through
elliott.ns.cloudflare.com (so example.com runs through Cloudflare's nameservers,
interesting to notice).

## Two red flags a SOC analyst would actually look for

**1. Behavior/volume** - queries firing every few seconds, sustained, same base domain
over and over. A real person browsing doesn't generate DNS lookups like this. Sequential
naming like test3/test4/test5/test6 is also a giveaway on its own - real browsing
doesn't produce clean incrementing subdomains, that's a scripted pattern.

**2. Content** - in a real DNS tunneling attack, the subdomains wouldn't be readable
words like "test3" - they'd look like random gibberish, e.g.
`k8f3jx92h7f2.attacker.com`. My test capture used clean names, so this part wasn't
demonstrated directly, but it's the second half of the picture.

## Why the subdomains look like gibberish (this took me a while to actually get)

Wasn't obvious to me at first why attackers would use random-looking strings - I
initially thought it was some kind of stealth trick. It's not. It's just a side effect
of how the technique works.

DNS tunneling works by smuggling stolen data out through DNS queries, because DNS
(port 53) is usually trusted/lightly inspected compared to normal web traffic. Since a
DNS query can't carry huge chunks of data, the attacker has to chop the stolen data
into small pieces and encode each piece (usually Base64) into a subdomain name, then
send it out as a stream of individual queries.

The "gibberish" is literally just encoded fragments of real data, not an intentional
disguise choice. Attacker's own server on the other end (which they control) decodes it
back into the original data.

Simple analogy that made it click for me: imagine smuggling documents out of a building
through a mail slot guards barely check. Can't fit a whole document through at once, so
you chop it up, encode it, and drop pieces through repeatedly. The pieces look like
gibberish because you're seeing scrambled fragments out of context, not because someone
tried to make them "look mysterious."

## Detection - behavior AND content together

Neither signal alone is fully reliable on its own:
- High volume alone could just be a busy legit service doing lots of lookups
- Weird-looking subdomain alone could be a one-off fluke

But volume + randomness together (same domain, rapid repeated queries, high-entropy
subdomains) is a strong combined signal. This is why real detection tools use layered
analysis instead of single-indicator alerts - entropy scoring, query volume thresholds,
and domain reputation combined, not just one check.

## Attacker evasion tradeoffs (worth remembering)

Attackers trying to dodge detection have to trade something off every time:
- Mixing readable words into the encoded subdomain lowers entropy score, but also
  cuts down how much actual data fits per query
- Spreading queries out over hours instead of bursting them dodges volume-based
  detection, but slows the whole exfiltration down
- Using a domain that just LOOKS legit (typosquatting like "cloudflare-cache.net")
  can fool a human skimming logs, but won't fool automated entropy scanning

No single evasion trick beats every detection method at once - that's the whole point
of using multiple layers of detection instead of relying on one.
