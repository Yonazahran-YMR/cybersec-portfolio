# Cloud Security: Cloud IAM

Theory notes.

## The big idea

Cloud IAM is like an office building. Everyone who walks in is a principal with a badge. Showing the badge at the door is authentication. Each door has a rule sheet (the policy), and the guard who reads it and says yes or no is authorization. A visitor day pass that expires at the end of the day is a role. This clicked for me because it splits one fuzzy word, "access," into two separate questions: who are you, and what are you allowed to do.

| Building | Cloud IAM | Meaning |
|---|---|---|
| Person with a badge | Principal (user, role, service) | Who is asking |
| Showing the badge | Authentication | Prove who I am |
| Rule sheet on the door | Policy | What this principal may do |
| Guard reading the sheet | Authorization | Allow or deny the request |
| Visitor day pass | Role | Temporary identity, expires on its own |

The core objects:

| Object | What it is | Use |
|---|---|---|
| User | Long term identity for one human | People |
| Group | Collection of users, policy attached once | Manage by job function |
| Role | Identity I assume, gives temporary credentials | VMs, functions, cross account access |
| Policy | JSON document of permissions | Attached to a user, group, or role |

Mapping between clouds: an AWS IAM role is like an Azure managed identity. An AWS IAM policy is like an Azure RBAC role assignment.

A policy statement has 4 parts:

1. Effect: Allow or Deny
2. Action: what operation (read, delete)
3. Resource: on which thing (this bucket)
4. Condition (optional): only if (from this IP, with MFA)

How the policy engine decides, in this exact order:

1. Everything starts as implicit deny
2. Any explicit deny wins, always
3. Otherwise an explicit allow grants access
4. No match means deny

Least privilege means granting only the actions and resources the task needs. Start from zero and add, never start from admin and remove.

Old pattern connection: the policy engine that decides is the PDP, the service that enforces the answer is the PEP. I mixed these up before, so this is the cloud version of it.

Exam traps:

1. Authentication is who I am, authorization is what I can do. Don't swap them.
2. Explicit deny beats any allow.
3. Workloads get roles, not long term access keys.
4. The root account is for rare setup tasks only, locked with MFA, never daily use.
5. A role has no password of its own. It is assumed and it expires.

## Warm-up: what I got right and wrong

This warm-up had 3 questions, one cloud, one networking, one recurring mistake.

1. Shared responsibility, IaaS VM with an OS vulnerability. I said the customer handles guest OS and data, and the provider only gives raw VMs, storage, and network. Correct. The term I should name is IaaS, so I patch the guest OS, and data and identity are always mine. I checked the service model first, which was my old mistake from the shared responsibility note.
2. Networking, packet through 3 routers. I said both MACs change, both IPs stay the same, and I explained that the router strips the layer 2 header, reads the destination IP, picks the next hop, and builds a new frame. Correct. Layer 2 is hop by hop, layer 3 is end to end.
3. Email trio. I said SPF is the guest list, DKIM is the wax seal, DMARC is the doorman. Right match, but my Why was thin. I should say what each one checks: SPF checks the sending server IP against the domain's DNS record. DKIM checks the signature against a public key in DNS, so it proves the message wasn't altered. DMARC needs alignment with the From domain, then applies a policy: none, quarantine, or reject. The formal term I missed was alignment.

## The scenario

A developer's script on a cloud VM needs to read files from one storage bucket. To make it work quickly, a teammate pastes an admin user's long term access keys into the script. The script is later pushed to a public repository. Which principle was violated, what should have been used instead, and why is it better?

My answer: least privilege was violated. I should have used an IAM role like an instance profile on AWS with a scoped read only policy, which is better because there's no hardcoded secret and the credentials are temporary. Correct on all 3 parts.

Corrections to my reasoning:

1. There were two violations, not one: least privilege (admin keys for a read only job) and hardcoded credentials in code.
2. The role fixes how the script authenticates, and the scoped policy fixes what it may do (Get and List on that one bucket). I should name both halves.
3. I said "automatic key rotation." Better wording: role credentials are issued by STS (Security Token Service) and expire on their own. Rotation is what I do to long term keys. A leaked admin key stays valid until someone revokes it, while a leaked role credential dies in hours.

The chain for my notebook:

1. Wrong: long term admin key in code, then public repo, then anyone can act as admin until revoked
2. Right: VM assumes a role, STS gives temporary credentials, policy allows only Get and List on one bucket, so the leak impact is small and short

Extra exam point: if the keys already leaked, the first action is to revoke and rotate them. That is a corrective control, because the damage path already exists. The preventive layer is secret scanning in the repo and a secrets manager.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| Authentication vs authorization | Who I am vs what I can do |
| Principal | Anything that can make a request: user, role, service |
| Role | Assumed identity with temporary credentials from STS |
| Policy statement | Effect, Action, Resource, optional Condition |
| Evaluation order | Implicit deny, explicit deny wins, then explicit allow |
| Least privilege | Start at zero and add, never start at admin |
| Workloads | Use roles, never long term keys in code |
| Root account | Rare setup only, MFA, never daily use |
| Leaked key response | Revoke and rotate, that is a corrective control |
| PDP vs PEP | PDP decides, PEP enforces |
| Email trio | SPF checks sender IP, DKIM checks the signature, DMARC needs alignment then applies policy |

## Still to do

1. Cloud logging and monitoring
2. Network isolation in the cloud
3. Cloud misconfiguration
4. AI and LLM security
5. Later: Security+ gap closers (acronyms, performance based questions)
