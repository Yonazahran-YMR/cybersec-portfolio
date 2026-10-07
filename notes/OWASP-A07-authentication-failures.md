# OWASP A07: Authentication Failures

Failures in verifying identity, weak login mechanisms, broken session handling, or credential management done wrong. Different from A01, which is about authorization (what you can do once logged in). A07 is about the login process itself.

| Example | Why it's a problem |
|---|---|
| No rate limiting on login attempts | Allows brute force |
| Weak password policy (no minimum complexity) | Easier to guess or crack |
| Session tokens that don't expire or rotate | Stolen token stays valid indefinitely |
| Predictable session IDs | Attacker can guess a valid session without stealing anything |
| No MFA on sensitive accounts | Single factor compromise is enough |
| Credentials sent or stored insecurely | Overlaps with A04, but the failure here is specifically in the auth flow |

Core defenses: MFA, strong password policies, account lockout or rate limiting after failed attempts, secure session management (random high-entropy tokens, expiration, rotation after login), never rolling your own crypto for auth.

## Scenario I worked through

A web app issues a session token right after the correct password is entered, but before MFA is verified. An attacker steals that pre-MFA token and uses it to access the account, skipping MFA entirely, since the session already looks authenticated.

I got the category right (A07) but the reasoning wrong twice. I first said it was about the token not rotating or expiring, that's not it, this has nothing to do with rotation. Then I guessed rate limiting on the login endpoint, also wrong, there's no brute forcing happening here, the attacker got the token some other way (theft, interception), not by guessing passwords.

The actual flaw: session/auth state gets granted too early in the flow. The session is marked authenticated the moment the password is correct, before the second factor is even checked. The attacker doesn't need to beat MFA, they just need to grab a token that was never supposed to count as a full login yet.

The fix: the session should sit in a "pending MFA" state after password verification, not a fully authenticated one. It only gets elevated to a real authenticated session after MFA succeeds. If MFA fails or never completes, the pending token should be useless for actually accessing anything.

Mental model that made it click: a building with a keycard door, then a security guard checking ID behind it. If the keycard reader lets you into the main lobby before the guard checks anything, stealing the keycard alone is enough to get in. The guard only matters as a real second check if the door stays locked until they're done.

## Next up

A08 Software or Data Integrity Failures.
