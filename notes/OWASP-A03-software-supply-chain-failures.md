# OWASP A03: Software Supply Chain Failures

New as its own top-level category in 2025, used to be folded into "Vulnerable and Outdated Components." Covers anything that enters your app from outside your own codebase, libraries, frameworks, build tools, CI/CD pipelines, even the registries you pull packages from.

The simplest test I landed on: did you write the broken thing, or did you just import it? If you imported it, it's A03, not A02 (which is about your own settings).

| Example | Why it's a problem |
|---|---|
| Outdated library with a known CVE | Public exploit may already exist |
| Compromised build pipeline | Attacker injects malicious code before it ships |
| Typosquatted package (e.g. `reqeusts` instead of `requests`) | Developer installs malware by mistake |
| Unsigned/unverified dependencies | No way to confirm the package wasn't tampered with |
| Over-permissioned CI/CD credentials | One compromised pipeline step can reach everything |

This is the SolarWinds-style category, the vulnerability isn't in code I wrote, it's in something I trusted and pulled in.

Core defenses: dependency scanning (Dependabot, Snyk, OWASP Dependency-Check, all have free tiers), pinning versions instead of always pulling latest, verifying package signatures/checksums, and least privilege on build/CI credentials.

## Scenario I worked through

My Java log parser pulls in a third-party CSV parsing library from Maven Central. Six months later, a critical CVE drops for that exact version, arbitrary code execution when parsing a malformed file.

1. Category: A03, since the bug lives in code I imported, not code I wrote.
2. What a dependency scanner catches: not just "a newer version exists," but specifically "you're on version X, and version X has CVE-2026-whatever." It runs ideally in two places, locally while coding (catch it before committing) and again in CI (so nothing slips through even if the local check gets missed).
3. Updating the library to the patched version is close to patch management in spirit, but there's a real distinction. Domain 4 patch management is about infrastructure I control directly (OS, servers, my own deployed apps) on a schedule my team manages. Updating a dependency is dependency management / software composition management, I'm not patching my own code, I'm swapping in a newer version of someone else's code on their release schedule, not mine. On an exam question "patching" as an umbrella term is fine either way, but the reason A03 exists as its own category is that dependencies update far more often and unpredictably than OS patches, so they need their own tooling and tracking.

## Next up

A04 Cryptographic Failures.
