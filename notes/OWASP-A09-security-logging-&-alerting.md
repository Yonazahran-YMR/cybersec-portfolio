# A09 Security Logging and Alerting Failures

These are my notes from the A09 session. Theory only, no lab yet.

## The big idea

The analogy that made this click for me was a shop with CCTV. There are three different ways the CCTV can fail you:

1. No cameras where the safe is (not logging the right events).
2. Cameras exist, but the recordings sit in an unlocked drawer the thief can empty (logs not protected).
3. Cameras record fine, but nobody watches the feed and no alarm goes off (no alerting or response).

A09 covers all of those, plus a fourth one I wouldn't have thought of at first: the camera footage accidentally showing the safe combination (logs leaking sensitive data).

| Failure | What it looks like |
|---|---|
| Not logging the right events | Failed logins, access control denials, and high value actions never get recorded |
| Logs not protected | Stored only on the same host, so an attacker can edit or delete them (an integrity problem) |
| No alerting or response | Logs exist, but there are no thresholds, no alarms, and nobody reviewing them |
| Logs leaking data | Passwords, tokens, or card numbers written in plain text into the log |

The 2025 name says "Alerting" on purpose. A log nobody acts on is just storage. Real breaches often run for weeks or months before anyone notices, and this category is basically why.

## Warm-up slip: hash vs encrypt (again)

This is my recurring mistake and it showed up in the review questions before A09 even started. The question was a login system confirming a password, and a billing system showing the last 4 digits of a card on a receipt.

I answered "hash" for the receipt because it "needs to show the last 4 digits." That's backwards, and I also only answered one of the two parts.

The deciding factor is always the same: **do I need the original value back?**

| System | Answer | Why |
|---|---|---|
| Login | Hash | It only compares the typed password against the stored hash. It never needs the original back. |
| Receipt | Encrypt | It has to show the real digits, so it needs the original back. A hash can't give digits back. |

"It needs to show digits" is a yes to "do I need the original back?", so that means encrypt. I picked the right kind of question to ask, I just flipped the result. Next time I'll say the factor out loud first, then pick.

## What I got right in the warm-up

Order of volatility was d, b, a, c (RAM, then processes and connections, then disk, then remote logs). My reasoning was thin though. The fuller version: RAM goes first because it's lost the second power is cut or the box reboots, and a live attacker can change it while I work. Processes and network connections live in RAM, so they come right after. Remote syslog goes last because it's on a different machine and changes the slowest.

OWASP category check also went fine: A03 for the vulnerable JSON library nobody updated, A08 for the dependency pulled without checking signature or hash, A02 for the admin console left on the default password. The phrases that keep them apart for me are "imported thing is vulnerable" (A03), "never verified integrity" (A08), and "my own setting is wrong" (A02).

## The scenario

A web app writes failed logins to a text file on the same server. Over a weekend an attacker runs 40,000 password guesses, gets into an admin account, and deletes the log file before leaving. Monday comes and nobody knows until a customer complains.

My answers:

1. Two A09 failures: no alerting or response, and logs not protected.
2. Fixes: a SIEM that flags brute force patterns and alerts the security team, and real time log forwarding to a centralized, write once log server separate from the app server.
3. An alert that fires after 20 failed logins in 5 minutes is a **detective** control. It flags the attack but doesn't block it (preventive) or repair anything (corrective).

All three were correct. A few things I want to remember that sharpened my answers:

1. The SIEM rule needs a threshold and a window, and a person has to own the alert. A SIEM nobody triages is the "cameras with nobody watching" failure all over again.
2. Real time forwarding matters because the attacker can only delete what's still on the box. Anything already shipped off the server survives. Write once storage adds integrity on top of that.
3. The attacker had admin rights and deleted the log. A mature setup alerts on **log deletion or logging service stoppage**, because covering tracks is a classic move.

## Control type clarification

I've struggled with preventive vs detective vs corrective before, so this one felt good to get right. One extension that helped: if the same alert also triggers an automatic account lockout, the alert is still detective, but the lockout is a separate control that acts as preventive or corrective. The alert and the action it triggers are two different controls.

## Category boundary: A09 vs A07

The 40,000 guesses actually working points to **A07 Authentication Failures**, since there was no rate limiting or lockout. The story contains both categories. A09 is about the visibility and response around the attack, not the weak login itself. So: A07 is why the attacker got in, A09 is why nobody noticed.

## Quick recap for future me

1. Four A09 failures: missing events, unprotected logs, no alerting or response, sensitive data in logs.
2. A log with no alert is storage, not defense.
3. Ship logs off the host in real time, ideally to write once storage.
4. Alert on log deletion and logging service stoppage.
5. Alert is detective. What it triggers is a separate control.
6. Hash vs encrypt: do I need the original back? Yes means encrypt, no means hash.

## Still to do

Next up is A10 Mishandling of Exceptional Conditions. The Domain 4 review quiz is still parked until I ask for it.
