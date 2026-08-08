# Cryptography Basics

Notes from studying encryption fundamentals - symmetric/asymmetric, hashing, salting.

## Symmetric vs Asymmetric

**Symmetric encryption** - one key does both jobs, encrypts and decrypts. Fast, but you've got
a problem: both sides need the exact same secret key. So how do you send that key over safely
in the first place without someone intercepting it? That's the "key distribution problem."

Used for: encrypting big chunks of data, disk encryption. Algorithms: AES, DES.

**Asymmetric encryption** - two keys, a pair. Public key + private key.
- Public key can go out to literally anyone, no risk
- Private key never leaves your hands
- Anyone can encrypt something using your public key, but only YOUR private key can decrypt it

This solves the key distribution problem since you never have to secretly share anything -
the public key being public is fine by design.

Slower than symmetric though, so not great for encrypting large amounts of data directly.
Algorithms: RSA, ECC.

## Why HTTPS uses both (hybrid model)

This clicked for me because I'd already seen TLS traffic in my Wireshark captures without
really knowing what was happening underneath.

Browser and server use asymmetric encryption first, just to securely agree on a shared secret
key. Once they've got that shared key, they switch over to symmetric encryption for the actual
page data, since it's way faster for bulk transfer.

So: asymmetric solves the "how do we agree on a secret safely" problem, symmetric handles the
"okay now let's move data fast" part.

## Hashing - different thing entirely

Encryption is reversible (if you have the key). Hashing is NOT reversible, period, that's the
whole point.

Hashing = integrity check. Encryption = confidentiality.

Example: downloading a file, site gives you a SHA-256 checksum. You hash the file yourself
after download, compare against theirs. Match = file wasn't corrupted/tampered with. No match
= something changed.

## Why passwords get hashed, not encrypted

If passwords were encrypted, whoever steals the database + finds the key can decrypt
literally everyone's password. One key = the whole thing falls apart if it leaks.

With hashing there's no key to steal in the first place. Nobody, not even the company, can
reverse a hash back into the original password. It's mathematically a one-way street.

How login actually works:
```
set password -> gets hashed -> stored hash saved (plaintext never stored anywhere)
login attempt -> input gets hashed -> compared against stored hash
match -> login works
```
System never "decrypts" anything, it just re-hashes and compares.

## Salting

Problem: if two people use the same password, plain hashing gives them the exact same hash.
Attacker with a precomputed table of common hashes (rainbow table) could crack both instantly.

Salting = tack on a random unique string to each password before hashing, so identical
passwords end up with completely different hashes.

```
userA: "password123" + salt(random) -> unique hash
userB: "password123" + salt(different random) -> different hash
```

Even if the passwords match, the stored hashes don't.

Even with salted hashes though, an attacker isn't fully blocked - they can still brute force
or run dictionary attacks (try tons of guesses, hash each with that user's specific salt, check
for a match). Just way slower and more expensive than a rainbow table shortcut.

This is also why algorithms made specifically for password hashing (bcrypt, Argon2) are built
to be intentionally SLOW - unlike something like SHA-256 which is fast on purpose for file
integrity checks. Slower hashing = brute forcing takes way longer = real protection.

## Quick recap for myself
- Symmetric = 1 key, fast, key-sharing problem
- Asymmetric = 2 keys (public/private), solves key-sharing, slower
- HTTPS = uses both (asymmetric to exchange, symmetric for actual data)
- Hashing = one-way, for integrity, not confidentiality
- Passwords = always hashed, never encrypted
- Salting = stops rainbow tables, forces attacker into brute force instead
