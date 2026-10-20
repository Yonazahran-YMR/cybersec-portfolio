# Automation and Orchestration 

## The big idea

The analogy that makes this click for me: a factory. **Automation** is one robot arm doing one job without a human, like welding the same joint all day. **Orchestration** is the control system that coordinates all the robot arms, conveyor belts, and sensors into one production line. Automation does a task. Orchestration connects many automated tasks, across many tools, into a workflow.

In security, the product category that does this is **SOAR** (Security Orchestration, Automation, and Response). A SIEM tells me something happened. A SOAR runs the response steps, following a **playbook** (the written workflow of what to do for a given alert type).

This connects to things I already know. 4.4 gave me alert fatigue (900 alerts a day, 95% false positives), and SOAR is a main way to cut the manual work on those alerts. A02 misconfiguration shows up here too, because automation can enforce a secure baseline on every system instead of trusting humans to remember.

## Use cases

| Use case | What it looks like |
|---|---|
| User provisioning | New hire gets accounts and access automatically from HR data, and a leaver gets everything removed the same way |
| Resource provisioning | Spinning up servers or cloud resources from templates (infrastructure as code) so every one starts hardened |
| Guard rails | Automatic limits that stop risky actions, like blocking creation of a public storage bucket |
| Security groups | Automatically adjusting network rules |
| Ticket creation | An alert opens a ticket with the context already filled in |
| Escalation | Automatically paging a human when severity passes a threshold |
| Enabling and disabling services or access | Automatically disabling a compromised account or turning off an unused service |
| Continuous integration and testing | Security tests run on every code change in the pipeline |
| Integrations and APIs | Tools talk to each other (SIEM, firewall, EDR, ticketing) without a person copying data between them |

## Benefits

| Benefit | Why it matters |
|---|---|
| Efficiency and time saving | Analysts stop doing repetitive work |
| Enforcing baselines | Every system gets the same secure config |
| Standard infrastructure configuration | Less drift and fewer one off mistakes |
| Scaling securely | Growth doesn't require proportionally more people |
| Reaction time | A response in seconds instead of minutes or hours |
| Workforce multiplier | The same team covers more |
| Employee retention | People spend time on interesting work instead of burnout level repetition |

## Risks and other considerations

| Risk | What goes wrong |
|---|---|
| Complexity | Workflows across many tools get hard to understand and debug |
| Cost | Tools, integration work, and staff skills aren't free |
| Single point of failure | If the automation or orchestration platform breaks, everything that depends on it stops |
| Technical debt | Old scripts and playbooks nobody maintains or documents |
| Ongoing supportability | Someone has to keep it updated as tools and APIs change |

Two more risks I want to remember that tie back to earlier topics:

1. **Automation at scale amplifies mistakes.** A bad rule that auto isolates hosts can take down many legitimate systems in seconds. That's a false positive with a bigger blast radius.
2. **Fail open vs fail closed applies to automation too (A10).** When an automated action errors out halfway, what state does it leave things in? Atomic steps and rollback matter here as well.

A practical rule: keep a **human approval step** for high impact actions (isolating a production server, disabling an executive account) and fully automate low risk, high volume ones (enriching an alert, opening a ticket).

## Warm-up: what I got right and wrong

1. **Control types.** SIEM rule flagging a login from two countries is detective, a firewall rule blocking traffic is preventive, restoring a server from backup after ransomware is corrective. All correct, with the right deciding factor: when the control acts relative to the incident. This was on my recurring mistakes list and it held.
2. **One time password reset token.** I said hash, because the service only compares and nobody needs the original back. Correct. A nuance to keep: the token is long and random, so a fast hash like SHA 256 is fine. Slow hashes (bcrypt, Argon2) are for human chosen passwords, which are guessable.
3. **OWASP check.** Item 2 (update downloaded without verifying the signature) is A08 and item 3 (regular user opens an admin page by editing the URL) is A01, both correct. Item 1 I got wrong. I said A05:2021 Security Misconfiguration for a raw SQL error shown because nothing catches the exception. Two problems. First, I was answering in the 2021 list, and my track is the 2025 list, where Security Misconfiguration is A02. Second, and more important, the category itself: the deciding phrase was "because nothing catches the exception". No setting is wrong and no debug flag is on, so the code never handled the failure and the default error page leaked the details. That's **A10 Mishandling of Exceptional Conditions**, which is new in 2025 and has no 2021 equivalent, so it's easy to miss. The test: a setting I changed or left at default means A02, code that never handles a failure means A10.

## The scenario

A SOC gets 900 alerts a day. For every phishing alert, an analyst manually extracts the URL, checks its reputation, deletes the email from all mailboxes, blocks the sender, and opens a ticket. It takes about 25 minutes each.

Questions, all parts:

1. What tool category fixes this, and what's the difference between automation and orchestration?
2. Name two benefits.
3. The team proposes a playbook that auto isolates any host that triggers a malware alert. Name two risks.
4. Which actions would I keep behind human approval, and why?
5. A cloud bucket that becomes public gets flipped back to private automatically within a minute. Is that a preventive, detective, or corrective control, and what would a preventive version look like? (Watch my control type mistake here. The deciding factor is when the control acts relative to the incident.)

My answers and the corrections:

1. **Tool category and the difference.** I said SOAR, automation executes individual repetitive tasks without a human, orchestration connects multiple tools and workflows into one coordinated pipeline. Correct. The term I didn't use: the written response steps SOAR follows for each alert type are called a **playbook**. I'd want that word in an interview.
2. **Two benefits.** I only gave one (efficiency and time saving). The question asked for two, so this is the fifth time a multi part question lost a part. New habit: number the lines the question asks for before sending. Good second ones for this scenario: faster reaction time (25 minutes per alert drops to seconds), consistency (every phishing alert gets the same steps), or workforce multiplier (the same team covers 900 alerts a day).
3. **Risks of a playbook that auto isolates any host with a malware alert.** I said complexity and single point of failure. Those are real 4.7 risks, but I answered the general question instead of this specific proposal. The risks that matter here:
   1. False positives with a big blast radius. One bad detection rule isolates many legitimate hosts in seconds, possibly including critical servers. Automation amplifies mistakes.
   2. Attackers can abuse it. If they can trigger malware alerts on purpose, they turn my own response into a denial of service.
   Single point of failure fits a different angle (if the SOAR platform fails, the playbook stops), so I keep it for the general question and answer the one asked.
4. **What stays behind human approval.** I said isolating critical production servers, wiping or reimaging endpoints, and disabling core admin accounts, because false positives there cause outages or lockouts. Correct, and the deciding factor is the right one: high impact actions get a human check. Low risk, high volume steps (enriching an alert, opening a ticket, checking URL reputation) get fully automated.
5. **Bucket flipped back to private within a minute.** I said corrective, and a preventive version would be an AWS Service Control Policy, the S3 Block Public Access account setting, or an Infrastructure as Code policy check that stops the bucket from ever becoming public. Correct, and I applied the control type taxonomy well. The gap: corrective doesn't undo what already happened. The bucket was public for up to a minute, so the follow up is to **check access logs** for anyone who read it in that window. The whole flow is actually three controls: detecting the public bucket is detective, the auto flip is corrective, and the SCP is preventive.

## Quick recap for future me

| Concept | One line to remember |
|---|---|
| Automation | One task done without a human |
| Orchestration | Many automated tasks and tools coordinated into one workflow |
| SOAR | The tool category, runs playbooks in response to alerts |
| Playbook | Written workflow of response steps for an alert type |
| Main benefits | Speed, consistency, scale, less burnout |
| Main risks | Complexity, cost, single point of failure, technical debt, amplified mistakes |
| Human approval | Keep it for high impact actions |

## Still to do

After this: enterprise security upgrades (4.5), identity and access management (4.6), the missing incident response pieces (4.8), then the Domain 4 review quiz.
