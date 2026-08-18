# Log Analysis Basics - Brute Force vs Spoofing

Getting into actual SOC-style work now instead of just theory. This is apparently
what Tier 1 analysts actually spend most of their time doing, not packet captures,
just staring at logs.

## Brute-force vs spoofing (these are NOT the same thing)

Got this mixed up at first, worth writing down clearly so I don't forget again.

**Brute-force** = about volume/repetition. Attacker tries the SAME target account
over and over, rapid attempts, hoping one guess eventually works.
```
admin login attempt from 203.0.113.5 - FAILED
admin login attempt from 203.0.113.5 - FAILED
... (47 times) ...
```

**Spoofing** = about faking identity, completely different thing. Log looks totally
normal on the surface (a SUCCESSFUL login even), but the identity behind it is
faked or stolen.
```
Login SUCCESSFUL for 'shiori_finance' from IP 10.0.0.15 (internal)
```
except Shiori's badge logs show she wasn't even in the building, and her VPN
wasn't active. Someone's using her actual credentials, or spoofing her session.

The big lesson here: brute-force is LOUD and obvious in logs (tons of failures).
Spoofing/credential theft is QUIET, looks completely legitimate on its own. You'd
only catch spoofing by cross-referencing multiple log sources together (login logs
+ badge access + VPN logs), not from one log type alone. This is basically why real
investigation means correlating sources, not just reading one system in isolation.

## Log analysis exercise

Went through a sample log:
```
09:14:02  Login SUCCESS  user: jsmith      IP: 10.0.0.22   (internal)
09:14:15  Login SUCCESS  user: mgarcia     IP: 10.0.0.45   (internal)
09:15:01  Login FAILED   user: admin       IP: 185.220.101.7  (external)
09:15:02  Login FAILED   user: admin       IP: 185.220.101.7  (external)
09:15:03  Login FAILED   user: admin       IP: 185.220.101.7  (external)
09:15:04  Login FAILED   user: admin       IP: 185.220.101.7  (external)
09:15:05  Login FAILED   user: administrator  IP: 185.220.101.7  (external)
09:15:06  Login FAILED   user: root        IP: 185.220.101.7  (external)
09:22:14  Login SUCCESS  user: tlee        IP: 10.0.0.19   (internal)
```

Normal stuff: internal IPs, successful logins, spread out over time - regular
employees just logging in.

Suspicious stuff: external IP, rapid-fire failures, all within seconds of each other.

## Targeted vs generic/scripted attacks

Noticed the usernames being tried weren't a real specific person, it was generic
admin-type names (admin, administrator, root). This actually matters:

- Targeted brute-force = attacker knows a specific real person's account exists,
  focuses everything there (like the "sarah_finance" example)
- Generic/scripted attack = attacker has no idea what real accounts exist, just
  throws common default names at the system hoping something sticks

This second type is apparently extremely common in the wild - bots constantly
scanning the internet trying admin/administrator/root/test/guest against any
exposed login page, completely untargeted, just opportunistic.

Also worth checking source IPs like this against threat intel/reputation feeds
eventually, ties back to the CTI lifecycle stuff from earlier notes.

## What a SOC analyst would actually do about this

Immediate action: block the offending IP at the firewall. This is the direct,
right-now response that actually stops the attacker mid-attack.

Follow-up (soon after, not instant): check if the admin/administrator/root
accounts even exist for real, verify they've got strong passwords, turn on MFA
if it's not already required.

Longer-term fix: this kind of pattern (many failed logins, same source, short
timeframe) should ideally be caught automatically, not by a human staring at logs.
A SIEM rule that auto-flags or auto-blocks after say 5 failed attempts within 60
seconds would catch this without needing someone to manually notice it. Basically
automating the exact thing I just did by eye.

## Takeaway for myself
Don't assume "all attempts failed so it's fine" - failed attempts now doesn't
mean failed forever, especially against generic account names that might actually
exist somewhere with a weak password. Early blocking buys time to actually go
check and fix the underlying weakness before it becomes a real breach.
