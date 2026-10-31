# Security Awareness

Theory notes.

## The big idea

Security awareness is basically fire drills. Nobody reads the evacuation plan for fun, so you run drills, watch who goes the wrong way, and repeat. This clicked for me because awareness training only counts if it changes behavior, so it needs practice and measurement, not just a one time lecture.

| Component | What it covers | Hook |
|---|---|---|
| Phishing campaigns | Simulated phishing emails to test and train users | The fire drill |
| Recognizing and responding | Spot suspicious messages, report them, don't click | Pull the alarm |
| Anomalous behavior | Risky (shortcuts), unexpected (odd actions), unintentional (honest mistakes) | Noticing smoke |
| User guidance | Policies and handbooks, situational awareness, insider threat, password management, removable media and cables, social engineering, operational security, remote and hybrid work | The safety manual |
| Reporting and monitoring | Initial reporting of incidents, plus recurring tracking over time | The incident log |
| Development and execution | Build content for the audience, deliver it on a schedule, often role based | The curriculum |
| Effectiveness | Measure with click rates, report rates, repeat offenders, then adjust | The drill scorecard |

Exam trap: a high training attendance rate proves people showed up, not that behavior changed. Effectiveness is measured by behavior (who clicks, who reports), which is why simulations exist.

## Warm-up: what I got right and wrong

1. Payment token the app must send back to the processor on every renewal. I said encrypt, "so it can be decrypted later, hash is one way." Correct, and this time I actually used the test. Tighter version: the deciding factor is that the app must send the original token back, and only encryption returns the original.
2. App installs updates but never checks the digital signature. I said A08, integrity never checked. Correct. I shortened the name though. The full name is A08 Software or Data Integrity Failures.
3. Pen tester given one standard employee account. I said partially known (gray box) and rules of engagement. Both parts answered, so counting the parts held again. The employee account is the visitor badge.

Recurring mistakes check: hash vs encrypt applied correctly, counting parts held for the second session in a row, and OWASP mixing stayed clean.

## The scenario

A company wants to know whether employees can actually spot phishing, not just whether they finished the annual training video. Security sends fake phishing emails to all staff and tracks who clicks and who reports. What is this activity called?

My answer: phishing campaign, because it tests whether employees really know what phishing is by simulating phishing emails. Right term, but my reason retold the scenario, so recurring mistake #1 showed up lightly. The full term is a simulated phishing campaign.

The deciding factor is: the company wants to measure behavior, not training completion. Fake emails plus tracking who clicks (click rate) and who reports (report rate) gives measurable evidence, while a training video only proves attendance. My test: am I measuring what people did, or whether they showed up?

Why the other options lose:

| Option | Why it's not the answer |
|---|---|
| Annual training video or quiz | Measures completion and recall, not real behavior under pressure |
| Policy acknowledgement | A signed statement that they read the rules, nothing tested |
| Awareness poster or newsletter | Passive guidance, no measurement |
| Real incident reporting | Reactive, waits for an actual attack instead of testing in advance |

Two details to tie together: the results feed the effectiveness loop (measure, then adjust training, for example extra coaching for repeat clickers). And a high report rate is arguably the best metric, since it shows users acting as a detection layer instead of just avoiding mistakes.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Simulated phishing campaign | Fake phishing emails to measure real behavior |
| Click rate vs report rate | Who fell for it vs who flagged it, report rate is the better sign |
| Attendance is not effectiveness | Completing training proves showing up, not changed behavior |
| Anomalous behavior types | Risky, unexpected, unintentional |
| Effectiveness loop | Measure, then adjust training |
| Hash vs encrypt | Need the original back? Yes encrypt, no hash |
| A08 | Software or Data Integrity Failures: integrity never verified |
| Gray box | Partially known, for example a standard user account |

## Still to do

1. Domain 5 review quiz
2. Mixed domain review
