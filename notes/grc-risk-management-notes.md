# Risk Management Basics

Starting to actually get into GRC content now. First real concept: risk management,
and it's less abstract than I expected.

## The core formula

Risk = Likelihood x Impact

Likelihood - how probable is it that a threat actually exploits a vulnerability
Impact - if it happens, how bad is the damage (financial, legal, reputational, 
operational)

Risk isn't binary, it's not "safe or unsafe", it's a spectrum based on these two
things multiplied together. Something can be high likelihood but low impact (annoying
but not a big deal), or low likelihood but catastrophic impact (rare but devastating),
and everything in between.

## The risk management process, 4 steps

1. Identify : find the assets, threats, and vulnerabilities (this is literally
   everything I already covered with threat actors and vulnerability types, just
   applied differently now)
2. Analyze : figure out likelihood and impact for each risk found
3. Evaluate : compare against what the company considers acceptable (risk appetite)
4. Treat : decide what to actually do about it

## The 4 treatment options

- Accept : risk is low enough, or fixing it costs more than it's worth, just live
  with it
- Mitigate : reduce likelihood or impact, doesn't eliminate the risk entirely. This
  is where basically everything I already learned plugs in - patching, MFA,
  monitoring, preventive/detective controls, all of that IS mitigation
- Transfer : shift the risk to someone else, usually insurance or outsourcing
- Avoid : eliminate the risk entirely by just not doing the risky thing at all

## Important lesson: transfer alone isn't enough for known, fixable problems

Went through a scenario where a company had a known SQL injection vulnerability and
just bought cyber insurance instead of fixing it. Thought this was risky because it
"relies on someone external" but the real issue is more specific than that.

Insurance only softens the IMPACT side if something goes wrong. It does nothing to
the LIKELIHOOD, the vulnerability is still sitting there, still exploitable, nothing
changed. Insurance also often requires you to already be following reasonable
security practices, so if a company gets breached through a KNOWN vulnerability they
never bothered to patch, the insurer could argue negligence and deny the claim
entirely.

Real answer: don't use Transfer as a replacement for Mitigate when something is
actually fixable. Use them together instead, patch what you can, keep insurance
for the stuff you genuinely can't eliminate.

## Compensating controls example (connects back to legacy systems notes)

Scenario: company has a critical vulnerability in their payment system, but the real
fix needs a costly infrastructure overhaul and 6 months of dev time. Can't just leave
it exposed that whole time, so in the meantime they:
- restrict system access to only 3 authorized employees
- add extra monitoring/logging on that system
- require MFA for anyone accessing it
- start planning the actual overhaul as the long-term fix

This is Mitigate, reducing risk while the real permanent fix gets built. Same idea
as the Windows 7 hospital example from earlier (legacy systems that can't just be
patched need layered temporary protections instead of just accepting full risk and
waiting).

## Takeaway for myself
This is basically the actual job, not just labeling something as risky, but making
a real judgment call on what to do about it right now vs long term, and being able to
explain that reasoning clearly to people who'd want to know why a known problem isn't
just being ignored.
