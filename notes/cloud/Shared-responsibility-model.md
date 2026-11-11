# Cloud Security: Shared Responsibility Model

Theory notes.

## The big idea

The shared responsibility model is like renting an apartment. The landlord secures the building, the roof, and the main door. I lock my own unit, decide who gets a key, and protect my belongings. If someone breaks in through my unlocked window, that's my problem, not the landlord's. This clicked for me because every other cloud term builds on this one question: whose job is this layer?

The rule: the provider secures security of the cloud, the customer secures security in the cloud.

| Provider (of the cloud) | Customer (in the cloud) |
|---|---|
| Physical data centers | Data and its classification |
| Hardware, hypervisor | Identity and access management |
| Core network and global infrastructure | Configuration of every service I use |

The service model changes where the line sits:

| Model | I get | Provider handles | I still handle | Example |
|---|---|---|---|---|
| IaaS | Raw VMs, storage, network | Hardware, virtualization | Guest OS, patching, apps, data, IAM | EC2, Azure VMs |
| PaaS | A platform to run code | Plus OS and runtime | App code, data, IAM, configuration | Elastic Beanstalk, App Service |
| SaaS | A finished app | Plus the application | Data, user access, configuration | Microsoft 365, Gmail |

Hook: the higher up the stack, the more the provider handles, but data and identity are always mine.

Exam trap: "the cloud provider is secure" doesn't mean my configuration is secure. Most real cloud breaches come from customer side misconfiguration, like a public storage bucket or an over permissioned role.

## Warm-up: what I got right and wrong

This session's warm-up was a 6 question networking quiz, and I got 6 of 6. The wording fixes are the useful part:

1. Which fields change at every router hop? I said both MACs, with the full decapsulation explanation. Correct, and the old source MAC gap is closed.
2. Smallest subnet for 28 devices. I said /27, with 30 usable. Correct (28 + 2 = 30, next power of 2 is 32, so 5 host bits and /27). My wording was ambiguous though. I said "lower subnet," but /26 has a lower prefix number and is a bigger subnet. Better: "/26 is too big, /28 is too small."
3. Server listening on TCP port 23. I said SSH replaces it and gave a good reason, but the question had 2 parts and I never named Telnet. Port 23 is Telnet, which sends everything in plaintext. That contrast is the Why. This is my recurring mistake of skipping a part.
4. One host sending thousands of DNS queries with long random subdomains to one external domain. I said DNS tunneling. Correct, the clue is high volume plus long random names to one domain.
5. Valid padlock on a phishing site. I said it proves the connection is to the domain named in the certificate. Correct. It proves identity of the domain, not safety.
6. Stolen server key, year of recorded TLS traffic. I said forward secrecy. Correct. Tighter: the session keys are never stored and are discarded after each session, so the long term key can't recreate them.

## The scenario

A company runs a web app on virtual machines in IaaS. An attacker exploits a known vulnerability in the guest operating system, which was never patched. Who is responsible for patching it?

My answer: the customer, because the provider only supplies raw VMs, storage, and network. Correct, both parts answered.

Formal terms I should add: the provider secures the cloud itself, meaning the hardware and the hypervisor. In IaaS, everything from the guest OS upward (patching, apps, data, IAM) belongs to me. A good short Why: "IaaS provider stops at the hypervisor, the guest OS sits above that line."

The model decides the answer. Same question, different service model:

| Service model | Who patches the guest OS? | Why |
|---|---|---|
| IaaS | Customer | Provider only supplies the VM |
| PaaS | Provider | OS and runtime are part of the platform |
| SaaS | Provider | The whole stack is the provider's |

Constant across all three: data and identity access stay with the customer. I was right because it was IaaS, so I check the model first on every shared responsibility question.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Security of the cloud | Provider: data centers, hardware, hypervisor |
| Security in the cloud | Customer: data, identity, configuration |
| IaaS | I patch the guest OS and above |
| PaaS | Provider handles OS and runtime, I handle app code, data, IAM |
| SaaS | Provider handles nearly everything, I handle data and user access |
| Always the customer | Data and identity access, in every model |
| Most cloud breaches | Customer side misconfiguration |
| Port 23 | Telnet, plaintext, replace with SSH |

## Still to do

1. IAM in the cloud (users, roles, policies, least privilege)
2. Cloud logging and monitoring
3. Network isolation in the cloud
4. Cloud misconfiguration
5. AI and LLM security
