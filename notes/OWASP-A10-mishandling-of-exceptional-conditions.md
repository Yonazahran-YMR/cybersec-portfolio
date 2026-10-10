# A10: Mishandling of Exceptional Conditions

Theory notes. This is the last category of the 2025 list, and it's new this year.

## What it actually is

The simplest way I made sense of it: a vending machine. Normal use is easy. The interesting part is what happens when something unexpected shows up, like a jammed coin, a power cut mid purchase, or a weird coin. A good machine refuses the sale, gives the coin back, shows "out of order" and logs it. A bad machine does one of the things in the table below.

| Failure | In code | Vending machine version |
|---|---|---|
| Fails open | An error inside the auth check ends up granting access | A sensor error unlocks the door |
| Leaks internals | Stack trace, SQL error, file paths, versions shown to users | Back panel wiring shown on the screen |
| Half finished state | Payment taken, order never created, no rollback | Coin eaten, no snack |
| Resource exhaustion | Odd input or load eats memory or connections, no limits | Coin slot jammed until the machine hangs |
| Unhandled crash | Missing null check, uncaught exception kills the service | The whole machine dies |

The core fixes: catch exceptions where they happen, **fail closed** (deny on error), make multi step actions atomic with rollback, set resource limits, and show users a generic message while the details go to protected logs.

## Warm-up: what I got right and wrong

1. **Segment on an unpatchable server.** I said mitigation category is segment and control type is preventive, and explained that they're two different dimensions (what I did vs when it acts). Correct. The missing formal term: since patching isn't possible, the isolation is a **compensating control**. The vulnerability still exists, only the exposure shrank.
2. **Proving a disk image wasn't altered.** I said hash, which is right, but I wrote that hashing is "the only method" for integrity. That overclaims, because a digital signature also proves integrity (and adds who vouched for it). I also skipped the deciding factor again: I don't need the original back, I only need a fingerprint to compare. Hash at collection, write it in the chain of custody paperwork, recompute later. And the original hash has to be stored safely, otherwise an attacker could alter the image and recompute it.
3. **Public security question on a password reset.** I answered A04, but the right answer is **A06 Insecure Design**. A04 was Insecure Design in the 2021 list. In 2025, A04 is Cryptographic Failures. A numbering slip, not a concept slip, but it sits under my "mixing OWASP categories" pattern, so I'm writing it down. My A02 reasoning was right (A02 is about settings), but I didn't say why A06 fits: the code works as written and no setting is wrong. The control itself is flawed, so only a redesign fixes it.

## The scenario

An online store had three problems:

```java
// (a) access check
boolean isAllowed(User u, String page) {
    try {
        return permissionService.check(u, page);
    } catch (Exception e) {
        return true; // "don't block users if the service is down"
    }
}

// (b) checkout
chargeCard(order);         // succeeds
inventory.reserve(order);  // throws, nothing catches it
createOrder(order);        // never runs
```

(c) The uncaught exception from (b) shows the full stack trace to the user, including the database hostname and library versions. No debug flag is on.

An attacker floods the permission service until it times out, then walks into admin pages.

My answers: (a) fails open, (b) half finished state, (c) leaks internals. All correct.

For (a) I wrote the fix as `return false` in the catch block. Also correct, and I didn't flip fail open vs fail closed this time, which has been on my mistakes list for a while. Two things I want to keep:

1. Log the exception and alert on it. A silent `return false` hides an outage, and a permission service failing is exactly what A09 wants someone to see.
2. Fail closed isn't universal. A fire exit door fails open on purpose because human life outranks theft. The deciding factor: when the check itself breaks, which is worse, wrongly blocking or wrongly allowing? For access control, wrongly allowing is worse.

For (c), why is it A10 and not A02? Because no debug flag was left on. The code never handled the exception, so the default error page did the leaking. If it had been a debug flag, that would be A02.

## Where I hedged: the transaction question

For (b), I answered "database transaction?" with a question mark. The concept was right, I just didn't commit. The property is **atomicity**, the A in ACID: all steps commit together or none do. In JDBC that's `setAutoCommit(false)`, then `commit()` on success and `rollback()` in the catch block.

The part that makes this a real exam style trap: the card charge talks to an outside payment gateway, and a database rollback can't undo it. Two standard answers:

| Approach | Idea |
|---|---|
| Reorder | Reserve inventory and create the order inside the transaction first, charge the card last |
| Compensating action | If a later step fails, issue a refund to undo the charge |

## Boundaries with other categories

1. A10 vs A09: A10 is how the code behaves when something unexpected happens. A09 is whether anyone sees it.
2. A10 vs A02 for verbose errors: the root cause decides. Debug flag left on is A02. Code that never handles the exception is A10.

## Quick recap for future me

| Failure | Fix |
|---|---|
| Fails open | Fail closed, deny on error |
| Leaks internals | Generic user message, details to logs |
| Half finished state | Atomic transactions, rollback or compensation |
| Resource exhaustion | Limits, timeouts, rate limiting |
| Unhandled crash | Catch exceptions, validate input |

That closes OWASP Top 10:2025 on the theory side. Next is going back to the Domain 4 topics I haven't covered yet, starting with alerting and monitoring.
