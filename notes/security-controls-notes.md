# Security Controls

Realized I never actually wrote these down even though I covered them a while back.
Better late than never.

## The 5 types

Preventive: stops something before it happens. Firewall blocking known bad IPs, MFA
requirement, forcing DNS through an approved resolver instead of letting anything
external through.

Detective: notices/flags that something already happened. IDS alerting on a port
scan, SIEM flagging unusual DNS volume, log analysis catching a brute force pattern.
This is basically what I've been practicing this whole time with the log reading
exercises.

Corrective: fixes or limits damage after something already happened. Restoring
from backup, patching a vulnerability after a breach already occurred, disabling
a compromised account.

Deterrent: discourages an attack without actually technically stopping it. Things
like "security cameras in use" signs, warning banners on login screens. Doesn't
physically block anything, just makes an attacker think twice or go somewhere easier.

Compensating: an alternative control used when the ideal/primary control isn't
possible. Classic example was the Windows 7 hospital scenario, can't patch the OS
because medical devices aren't certified for anything newer, so instead you isolate
it on its own subnet, restrict access hard, and monitor it more closely than usual.

## Why you need more than one type (defense in depth)

Never rely on just one control type, because any single control can fail, get
bypassed, or be misconfigured. Real defense stacks these together:

Preventive stops most stuff from getting in.
If something gets past that, Detective catches it happening.
If damage already occurred, Corrective limits/fixes it.

This layered approach is called defense in depth. The DNS tunneling example from
earlier is a good real case of this: preventive control blocks unauthorized DNS
resolvers, detective control (entropy/volume analysis) catches anything that
still slips through.

## Residual risk

Even with every layer stacked together, there's always some risk left over that no
control fully addresses. This is called residual risk. Security isn't about hitting
zero risk, that's not actually achievable, it's about getting risk down to an
acceptable level and having a plan ready for when something inevitably gets through
anyway.

This connects to threat hunting too, since automated detection has blind spots by
definition (it only catches what it's programmed to catch), someone has to
proactively go looking for what got past everything else.

## Applying this to service accounts 

Was asked what detective controls would look different for service accounts
compared to regular human accounts. Working through this:

Service accounts run 24/7 automated tasks, so normal login time patterns don't
apply the way they do for humans. But they SHOULD still have a predictable
pattern, just a different one. A backup service account probably always logs in
from the same specific internal server, at roughly the same scheduled times, doing
the same repetitive task.

So detective monitoring for service accounts should probably flag things like:
- login from an unexpected IP or location (should never be external if it's only
  meant to run internally)
- login at a time outside its normal scheduled window
- unusual volume or type of activity compared to its normal repetitive baseline
- any interactive login at all, if the account is only supposed to run automated
  non-interactive tasks

Basically the baseline is different from a human account, but a real baseline
still exists. The mistake would be assuming "it's automated so any activity is
normal," when really it should be even MORE predictable than a human, which
means deviations should actually be easier to catch if you're watching for the
right things.
