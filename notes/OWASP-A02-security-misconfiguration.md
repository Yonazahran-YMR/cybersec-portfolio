# OWASP A02: Security Misconfiguration

Jumped from #5 in 2021 to #2 in 2025. Makes sense given the cloud direction I'm heading, most cloud breaches trace back to this category.

Secure software, deployed with unsafe settings. The code itself isn't the problem, the configuration around it is.

| Example | Why it's a problem |
|---|---|
| Default credentials left in place | Public knowledge, first thing attackers try |
| Unnecessary services or ports enabled | Larger attack surface |
| Verbose error messages or stack traces | Leaks versions, paths, internals |
| Public cloud storage bucket | Data exposed with no exploit needed |
| Missing security headers | Browser side protections never switch on |
| Directory listing enabled | Attackers browse files directly |

Core fixes: repeatable hardening baselines (CIS Benchmarks), removing unused features, automated config scanning to catch drift.

## Scenario I worked through

Production web app throws an unhandled error, shows the full stack trace including framework version and a database connection string.

Categories this touches: A02 (primary, verbose error output is a misconfiguration) and A10 Mishandling of Exceptional Conditions (the app fails unsafely by leaking sensitive info in the error).

I initially guessed the fix was patching, but that's wrong. Nothing here is a known vulnerability being exploited, it's a setting that should never have been on in production. The fix is hardening: disable stack traces/debug mode in production config, use generic error messages, log details server side instead of showing them to the user.

I also mixed up which category covers an outdated framework with a known CVE. My guess was A06 Insecure Design, wrong. It's actually A03 Software Supply Chain Failures, which replaced and broadened "Vulnerable and Outdated Components" from 2021. A06:2025 Insecure Design is a different thing entirely, flaws baked into the architecture itself (no threat modeling, no rate limiting by design, business logic flaws), not an outdated library.

## Cheat sheet for telling these apart

Ask: is the problem the code/design itself, or something installed/deployed around it?

| If the problem is... | Category |
|---|---|
| The app's own logic/architecture never accounted for this case | A06 Insecure Design |
| A setting was left wrong (debug mode on, default password, verbose errors) | A02 Security Misconfiguration |
| A third-party thing (library, framework, dependency, build tool) is outdated or compromised | A03 Software Supply Chain Failures |
| The app crashes or errors in a way that leaks info or skips checks | A10 Mishandling of Exceptional Conditions |

Quick way to split A02 vs A03 specifically, since those two get confused most: A02 is "we configured our own thing wrong." A03 is "something we didn't write ourselves is the problem." Debug mode left on is misconfig, my own setting. Old jQuery version with a known CVE is supply chain, someone else's code.
