# Automation and Orchestration

Theory notes. This one is a first pass, written before I tried the scenario. I'll come back tomorrow, answer the scenario questions at the bottom, and add my wrong answers and corrections to this file.

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

## Scenario to revisit tomorrow

A SOC gets 900 alerts a day. For every phishing alert, an analyst manually extracts the URL, checks its reputation, deletes the email from all mailboxes, blocks the sender, and opens a ticket. It takes about 25 minutes each.

Questions I need to answer tomorrow, all parts:

1. What tool category fixes this, and what's the difference between automation and orchestration?
2. Name two benefits.
3. The team proposes a playbook that auto isolates any host that triggers a malware alert. Name two risks.
4. Which actions would I keep behind human approval, and why?
5. A cloud bucket that becomes public gets flipped back to private automatically within a minute. Is that a preventive, detective, or corrective control, and what would a preventive version look like? (Watch my control type mistake here. The deciding factor is when the control acts relative to the incident.)

My answers and corrections go here tomorrow.

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
