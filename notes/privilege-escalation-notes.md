# Privilege Escalation

Building on the persistence/backdoor stuff from before. This is the next piece of
the same attack chain I've been working through.

## What it actually means

Going from the access level you started with to a HIGHER one. In my Windows Event
Log scenario, the attacker went from just getting in (low privilege, basically just
a foothold) to creating an account that got added straight into Domain Admins. That
jump is privilege escalation.

## Two types

Vertical is going from lower privilege to HIGHER privilege. Regular user account
becoming an Administrator. This is what happened in my log scenario.

Horizontal is staying at the SAME privilege level, but getting access to a
different account or resource you shouldn't have. Like compromising one regular
employee's account, then using that foothold to snoop on a different regular
employee's files. Same tier, just wider scope, not actually "higher" access.

## How this is different from persistence (easy to blur these together)

Persistence means staying in the system long term, having a way back in even if
the original access point gets shut down.

Privilege escalation means increasing how MUCH access or control you have.

They're separate concepts but attackers usually chain them together, since a low
privilege backdoor isn't worth much. In my log scenario the attacker did both at
once. They created a new account (persistence) AND got it added to Domain Admins
(privilege escalation) in basically the same breath.

## Common ways attackers actually escalate privileges (concept level, not deep yet)

One common way is exploiting misconfigured permissions, where a system or file
that should've been admin only accidentally got left open to regular users.

Another is exploiting unpatched vulnerabilities that specifically let a low
privilege user trick the system into running something with higher privileges
than they should have.

There's also stealing credentials from a higher privileged session. If an admin
ever logs into a machine that's already compromised, their credentials could get
grabbed and reused by the attacker.

## Why Domain Admins specifically is the attacker's end goal

In a Windows or Active Directory setup, Domain Admins is basically the top tier.
Whoever has it can access every computer joined to that domain, not just one
machine. They can create, delete, or modify any user account, and get into
pretty much any file or system across the whole organization.

This is why real breaches often specifically talk about reaching "Domain Admin"
or "domain compromise" as the worst case scenario. It's close to total control
over the entire Windows side of a company. Once an attacker's there, basically
everything is potentially affected.

## The full attack chain, start to finish (from my log scenario)

It goes brute-force for initial access, then a successful login to svc_backup
for the foothold, then creating backup_admin2 for persistence, then adding that
account to Domain Admins for vertical privilege escalation, which together adds
up to full domain compromise.

Apparently this maps pretty closely onto stages in the actual MITRE ATT&CK
framework, which I haven't formally gotten into yet but will later. Good to know
I already built some real intuition for how these stages chain together before
even seeing the formal framework.
