# Cloud Security: Network Isolation

Theory notes.

## The big idea

Network isolation in the cloud is like an office building. The lobby is open to visitors. Staff floors need a keycard. The server room has its own locked door that only certain staff can open. This clicked for me because the whole topic is just one question: which parts of my system can the internet reach, and which parts can't it reach.

| Building | Cloud | Meaning |
|---|---|---|
| The whole building | VPC (AWS) or VNet (Azure) | My own isolated virtual network |
| Lobby | Public subnet | Has a route to the internet gateway |
| Staff floor | Private subnet | No direct route from the internet |
| Front door | Internet gateway | Two way door to the internet |
| One way exit door | NAT gateway | Private resources go out, nothing comes in unasked |
| Door lock on one room | Security group | Firewall on the resource |
| Floor checkpoint | NACL | Firewall on the subnet |
| Signpost in the hallway | Route table | Decides where traffic goes next |

What makes a subnet public or private? Not its name. It's the route table. A public subnet has a route to the internet gateway, a private one doesn't.

Security group vs NACL, the classic exam pair:

| | Security group | NACL |
|---|---|---|
| Applies to | Resource (instance) | Whole subnet |
| State | Stateful: reply traffic is allowed automatically | Stateless: return traffic must be allowed explicitly |
| Rules | Allow only | Allow and deny |
| Evaluation | All rules together | In number order, first match wins |
| Default | Deny all inbound | Depends: the default NACL allows all |

Ways to reach private things safely:

| Need | Use |
|---|---|
| Admin access to a private server | Bastion host (jump box) or a managed session service, never open SSH to the world |
| Reach a cloud service (storage) without the internet | VPC endpoint (AWS) or Private Link (Azure), traffic stays on the provider network |
| Private servers need OS updates | NAT gateway, outbound only |
| Link two networks | VPC peering, VPN, or transit gateway |

The 3 tier design: web tier is public or behind a load balancer, app tier is private, database tier is private. Each tier allows traffic only from the tier before it. This is segmentation.

Links to my old patterns:

1. Segmentation is a mitigation category, not a control type. When isolation protects something that can't be patched, the term is compensating control.
2. A DMZ only applies to the public facing part. The database never belongs there.
3. Security group rules work on IP, port, and protocol, so L3 vs L4 still matters.

Exam traps:

1. Public vs private subnet is decided by the route table, not the name.
2. Security groups are stateful, NACLs are stateless.
3. Only NACLs can explicitly deny. Security groups cannot.
4. NAT gateway is outbound only. It doesn't make a server reachable from the internet.
5. Shared responsibility: the provider isolates the platform, but I design and configure my own VPC, subnets, and rules. A wide open security group is my misconfiguration.
6. Least privilege applies to network rules too: never allow 0.0.0.0/0 to admin ports.

## Warm-up: what I got right and wrong

## The scenario

A company runs a web app in the cloud. The web servers must accept traffic from the internet. The database must accept connections only from the web servers and never from the internet. Which design meets this requirement?

The answer has 2 parts plus a Why:

1. Placement: the web servers go in a public subnet, the database goes in a private subnet.
2. Access rule: a security group on the database allows the database port (for example 3306) only from the web servers' security group. No 0.0.0.0/0.
3. Why: the private subnet means no route from the internet, so nobody on the internet can reach the database directly. The security group lets only the web servers in. This is segmentation plus least privilege for network rules.

The chain:

1. Internet
2. Load balancer or public web tier
3. Security group allows the database port from the web security group only
4. Private database subnet

The wrong version is a database in a public subnet with 0.0.0.0/0 on the database port. That's a misconfiguration, which leads into the next topic.

## Quick recap for future me

| Takeaway | One liner |
|---|---|
| VPC or VNet | My own isolated virtual network |
| Public subnet | Route to the internet gateway |
| Private subnet | No route from the internet |
| What decides public or private | The route table, not the name |
| Security group | Firewall on the resource, stateful, allow only |
| NACL | Firewall on the subnet, stateless, allow and deny |
| NAT gateway | Outbound only for private servers |
| Admin access to private servers | Bastion host or managed session, never SSH open to the world |
| Reach cloud services privately | VPC endpoint or Private Link |
| Web and database design | Web public, database private, security group allows only the web servers |
| Isolating what can't be patched | Compensating control |
| Network rule least privilege | Never 0.0.0.0/0 to admin ports |

## Still to do

1. Cloud misconfiguration
2. AI and LLM security
3. Later: Security+ gap closers (acronyms, performance based questions)
