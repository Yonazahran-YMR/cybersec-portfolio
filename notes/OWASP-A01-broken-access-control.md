# A01: Broken Access Control

Authentication answers "who are you." Access control answers "what are you allowed to do." A01 is what happens when the second check is missing or can be bypassed. It's #1 on both the 2021 and 2025 lists, and SSRF got folded into this category in 2025.

## Types

| Type | What it looks like |
|---|---|
| Horizontal privilege escalation | User A accesses User B's data (same privilege level) |
| Vertical privilege escalation | Regular user reaches admin functions |
| IDOR (Insecure Direct Object Reference) | Changing an ID in a URL or request to reach someone else's object |
| Forced browsing | Guessing hidden URLs like /admin that have no access check |
| Tampering | Editing a cookie, JWT, or hidden form field to change your role |

## Core defenses

1. Deny by default.
2. Enforce checks server side on every request, never trust the client.
3. Apply least privilege.

## Scenario I worked through

A logged in customer views their invoice at `/invoices?id=1042`, changes it to `id=1043`, and sees another customer's invoice.

1. It's an IDOR.
2. It's horizontal escalation. What made it click for me: same privilege level, different owner. If the attacker had gained admin rights instead, that would be vertical.
3. The fix lives on the server. I said "check every request," but that was too vague. The real check is object level authorization: the server looks up who owns invoice 1043 and compares that to the logged in user from the server side session. If they don't match, deny. The user ID or role can never come from the client.

One trap: swapping sequential IDs for random ones (UUIDs) does not fix IDOR. It only makes guessing harder. The missing authorization check is still the flaw.

## Review slip worth remembering

Order of volatility, I put disk image before RAM and running processes. Correct order is RAM, running processes, disk image, then logs. Disk is less volatile, so it comes later, even though imaging the disk first feels like the natural instinct.

## Next up

A02 Security Misconfiguration.
