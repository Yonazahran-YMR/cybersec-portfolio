# The TLS Handshake

Theory notes.

## The big idea

TLS is like meeting a stranger who claims to be my bank. First I check their ID (the certificate), then we agree on a secret code word using a method nobody listening can copy (the key exchange), then we chat in that code (fast symmetric encryption). This clicked for me because the two kinds of crypto aren't rivals, they're a team with two different jobs.

Two kinds of crypto, two jobs:

| Type | Job in TLS | Speed | Hook |
|---|---|---|---|
| Asymmetric (certificates, key exchange) | Prove identity and agree on a shared secret | Slow | The ID check |
| Symmetric (AES) | Encrypt the actual data | Fast | The code word |

TLS 1.3 handshake, simplified:

| Step | Who | What happens |
|---|---|---|
| 1 | Client | ClientHello: supported versions, cipher suites, key share |
| 2 | Server | ServerHello: chosen cipher suite, its key share |
| 3 | Server | Sends its certificate and proves it owns the private key |
| 4 | Both | Each side computes the same session key (ephemeral Diffie-Hellman) |
| 5 | Both | Finished messages, then all data is encrypted with the symmetric session key |

Certificate checks the client performs:

| Check | Question it answers |
|---|---|
| Chain of trust | Does it lead to a root CA my device trusts? |
| Validity dates | Is it expired or not yet valid? |
| Name match | Does the domain match the certificate's CN or SAN? |
| Revocation | Was it revoked? (CRL or OCSP) |

Other terms to know:

| Term | Meaning |
|---|---|
| Forward secrecy | Ephemeral keys per session, so a stolen server key can't decrypt old recorded traffic |
| mTLS | Mutual TLS: the client also presents a certificate |
| SSL, TLS 1.0, 1.1 | Deprecated, don't use |

Exam trap: a valid certificate proves identity (I'm talking to that domain), not that the site is safe or honest. Phishing sites can have valid certificates too.

## Warm-up: what I got right and wrong

1. Does DoH stop a forged DNS record, and which control does? I said no, DNSSEC, because DoH only encrypts the channel between my device and the resolver and doesn't verify the record itself. Correct, all 3 parts answered. DoH protects the path, DNSSEC proves the answer is genuine.
2. Usable hosts in a /28. I said 14, from 16 total minus the network and broadcast addresses. Correct. The usable vs total mistake feels gone now.
3. Password reset token that nobody ever needs to read back. I said hash, because I don't need the original back. Correct, that's the test applied right.

## The scenario

A user connects to a bank over HTTPS. The handshake finishes and the browser starts sending account data. Which type of encryption protects the bulk of that data, and why is it used instead of the other one?

My answer: symmetric, because it's faster than asymmetric, which makes it ideal for transferring data in real time once the connection is secured. Correct, both parts answered.

The two types work as a team:

| Stage | Type | Job |
|---|---|---|
| Handshake | Asymmetric (certificate, key exchange) | Prove the server's identity and agree on a shared session key |
| Data transfer | Symmetric (AES) | Encrypt the actual traffic with that session key |

Asymmetric solves the problem symmetric can't: two strangers agreeing on a secret over a public network. Symmetric then does the heavy lifting because it's far faster and cheaper on CPU. Asymmetric is too slow and heavy for streaming large amounts of data, so TLS only uses it briefly at the start.

One wording fix for myself: "once the connection is secured" is the right idea, but the term is the symmetric session key. It's ephemeral (new for every session), which gives forward secrecy.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Asymmetric in TLS | Identity and key exchange, slow, only at the start |
| Symmetric in TLS | Bulk data encryption with the session key, fast |
| Session key | Ephemeral, new every session |
| Forward secrecy | Stolen server key can't decrypt old recorded traffic |
| Certificate checks | Chain of trust, dates, name match, revocation |
| Valid certificate | Proves identity, not that the site is safe |
| mTLS | Client presents a certificate too |
| Deprecated | SSL, TLS 1.0, TLS 1.1 |

## Still to do

1. Networking quick quiz covering all five topics
2. Decide the next theory block (cloud security foundations, or Security+ gap closers)
