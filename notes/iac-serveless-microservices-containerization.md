# IaC, Serverless, Microservices, Containerization

This closes out 3.1, architecture models. Started with a quick review scenario on shared responsibility and SASE from last session (mostly solid, just need to name the underlying principle when asked "why" instead of just restating what happened), then moved into today's new content.

## The four concepts

| Concept | What it is | Security angle |
|---|---|---|
| IaC (Infrastructure as Code) | Infrastructure defined in config files (Terraform, CloudFormation) instead of manual point and click setup | Consistent, version controlled, auditable, fewer manual misconfig errors, this ties straight back to the S3 bucket leak problem from the shared responsibility session |
| Serverless | Provider manages all underlying infrastructure, you only write and deploy functions (AWS Lambda, Azure Functions) | Pushes almost everything to the provider's side of shared responsibility, you're only responsible for your code's logic and the data it touches |
| Microservices | App broken into small, independent services instead of one monolithic app | Each service can be secured and scaled independently, but it also multiplies the attack surface, more services means more entry points to secure |
| Containerization | Packages an app plus its dependencies together (Docker), runs isolated but shares the host OS kernel | Faster and lighter than full VMs, but that shared kernel means a container escape can be more dangerous than a VM escape |

## The distinction that mattered most

Container vs VM isolation. A VM virtualizes the whole OS, so isolation is at the hardware level. A container shares the host's kernel, so isolation is only at the process level, lighter but a theoretically weaker boundary if something breaks out.

## Scenario I worked through

Company migrates a monolithic app into 15 separate microservices, each containerized, deployed via Terraform scripts that define every server, network rule, and container config in version controlled files.

First question was the specific security benefit of Terraform vs manual setup, that's IaC, consistent, version controlled, auditable, fewer manual misconfig errors compared to manual setup which just opens more possibility for error.

Second question asked for two separate trade-offs, and this was the actual point of the question, don't blend them together. Splitting into 15 microservices means each can be secured independently but also opens up more attack surface. Separately, containerizing instead of running 15 full VMs makes things lighter, but a container escape is more dangerous than a VM escape because of that shared kernel. Got both parts right and kept them separate instead of combining into one blended answer.

## Status

Domain 3.1 (architecture models) is now fully closed. Covered across sessions: Zero Trust (control plane, data plane, PDP, PEP, implicit trust), segmentation types (network, micro, DMZ, jump box), cloud shared responsibility (IaaS, PaaS, SaaS), deployment models (on-prem, hybrid, SDN, SD-WAN, SASE), and today's IaC, serverless, microservices, containerization.

Next up is Domain 3.2, secure infrastructure, covering firewalls, device placement, and attack surface.
