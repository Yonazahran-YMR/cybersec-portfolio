# Cloud Architecture & Network Deployment Models (Sec+ Domain 3)

Continuing Domain 3.1, architecture models. Today was cloud shared responsibility and then network infrastructure/deployment models.

## Shared responsibility model

Cloud security splits between provider and customer, and where the line falls depends on the service model.

| Model | Provider handles | Customer handles |
|---|---|---|
| IaaS | Physical hardware, hypervisor, network | OS, patching, apps, data, access control |
| PaaS | + OS, runtime | App code, data, access control |
| SaaS | Almost everything (app, OS, infra) | Data, user access/config only |

The trap here, and this is worth remembering, "the cloud is secure" does not mean "I have no responsibility." Even in SaaS you're always on the hook for data and access management. Most real world cloud breaches, think S3 bucket leaks, are customer side misconfig, not the provider failing at their job.

This connects straight back to least privilege and access control from Domain 2. The provider secures the building, you still have to lock your own office door.

Worked through a scenario on this, SaaS email platform, employee misconfigures a shared calendar to be public, exposes internal meeting details, company tries to blame the provider. Not accurate, since access config is always customer side even in SaaS. Maps back to misconfiguration and human error from Domain 2, both correct on my end, no corrections needed here.

## Network deployment models

| Concept | What it means | Key distinction |
|---|---|---|
| On-premises | Infrastructure physically owned and hosted by the org | Full control, full responsibility, opposite end of the spectrum from SaaS |
| Cloud | Hosted by a provider | Shared responsibility applies (see table above) |
| Hybrid | Mix of on-prem and cloud | Common setup, legacy stays on-prem, new workloads go cloud |
| SDN | Network control plane separated from data plane, managed via software instead of manual hardware config | Same pattern as PDP/PEP from Zero Trust, just applied to network management, not just access decisions |
| SD-WAN | SDN applied specifically to WAN, connecting branch offices or remote sites | Routes traffic dynamically over the best available path instead of a fixed line |
| SASE | SD-WAN plus actual security functions (ZTNA, firewall, secure web gateway), delivered as one cloud service | Giveaway vs plain SD-WAN: security functions bundled in, not just dynamic routing |

The SDN row was a good "click" moment for me, realizing control plane decides / data plane executes isn't just a Zero Trust specific idea, it's a repeating architecture pattern that shows up one level up at the network management level too.

Scenario here had a company running its legacy finance system in its own data center (hybrid, paired with a cloud hosted customer facing app) plus a separate system routing branch office traffic dynamically across broadband, LTE, and MPLS, combined with cloud delivered firewall and Zero Trust access. Correctly identified hybrid for the first part and SASE for the second, specifically because the firewall and Zero Trust piece is what pushes it past plain SD-WAN.

## Status

Domain 3.1 architecture models covered so far: Zero Trust, cloud shared responsibility, deployment models (on-prem, cloud, hybrid), SDN/SD-WAN/SASE. Still remaining in 3.1: IaC, serverless, microservices, containerization (touched conceptually earlier but not tested with scenarios yet). Domain 3.2 (secure infrastructure: firewalls, device placement, attack surface) still ahead after that.
