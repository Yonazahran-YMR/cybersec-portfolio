# Identity and Access Management

Theory notes. This chunk has a lot of similar sounding terms, so the skill is knowing the deciding factor for each one.

## The big idea

The analogy that made it click: a hotel. The front desk checks my ID (**authentication**), my keycard opens only my room and the gym (**authorization**), and the door log records who entered when (**accounting**). Federation is like a festival wristband that every stall accepts.

| Concept | One line |
|---|---|
| Provisioning, deprovisioning | Create accounts and rights on hire, remove everything on exit |
| Least privilege | Only the access the job needs |
| SSO | One login for many apps inside one organization |
| Federation | Trust across organizations: log in with my own company's identity at a partner |
| SAML | XML assertions for enterprise SSO and federation (authentication) |
| OAuth | Delegated authorization: an app gets limited access without my password |
| LDAP | Directory protocol for looking up users and groups |

| Access control model | Deciding factor |
|---|---|
| DAC | The owner decides who gets access |
| MAC | The system decides by labels and clearances (military) |
| RBAC | Access follows the job role |
| Rule based | Fixed rules apply to everyone (firewall style) |
| ABAC | One policy checks many attributes together: user, resource, time, location |

| MFA and password concepts | One line |
|---|---|
| Factors | Know (password), have (token), are (biometric), somewhere you are (location) |
| Two passwords | Still one factor, not MFA |
| Passwordless | Passkeys or security keys replace the password |
| Password manager | Unique strong passwords without memorizing |

**PAM** (privileged access management) protects admin access with **password vaulting**, **just in time permissions** (access granted only when needed, then removed), and **ephemeral credentials** that expire on their own.

## Warm-up: what I got right and wrong

1. **Spoofed domain, make receivers reject the mail.** I answered DMARC, correct, but I left out the reasoning. SPF and DKIM do the checks, and DMARC is the policy that tells receivers to reject when they fail.
2. **Unpatchable legacy server in an isolated VLAN.** Compensating, correct. My reasoning was the real deciding factor: the flaw stays, so I reduce exposure instead. Why not corrective: corrective fixes things after an incident, and no incident happened.
3. **Card charged, then an unhandled error stops the order.** A10 Mishandling of Exceptional Conditions, correct. The system was left half finished (money taken, no order). Not A06, because the design isn't the problem, the error handling is.

## The scenario

1. **Company A employees log in to Company B's app with Company A credentials, no new accounts at B.** I said federation, correct. But my reasoning only restated the scenario. The deciding factor is that trust crosses **organizations**: Company B trusts Company A's identity provider. The distractor to watch is SSO, which works inside one organization.
2. **Doctors see only their department's patients, only during their shift, only from the hospital network.** ABAC, correct, because the decision depends on dynamic attributes. What I should add: a role alone (RBAC) can't express department assignment, shift time, and network location together, and ABAC evaluates all of them in one policy.
3. **Admin needs elevated access for a two hour window, and it must disappear afterward without anyone remembering.** Just in time permissions, correct. Again my reasoning restated the scenario. The deciding factor is that access **expires automatically**, so no one has to remember cleanup and no standing privilege is left behind. It's least privilege applied over time.

The pattern in 1 and 3: right answer, but I described the situation instead of naming the deciding factor. Next time I'll finish the sentence "the deciding factor is...".

## Likely exam trap: SAML vs OAuth

SAML proves who I am (authentication, enterprise SSO). OAuth grants an app limited access to my data without sharing my password (authorization). If the question is about logging in, think SAML. If it's about an app acting on my behalf, think OAuth.

## Quick recap for future me

| Situation | Answer |
|---|---|
| Trust across two organizations | Federation |
| One login inside one organization | SSO |
| Many attributes decide access | ABAC |
| Access follows the job | RBAC |
| Owner decides | DAC |
| Labels and clearances | MAC |
| Temporary admin access that expires itself | Just in time permissions |
| App gets limited access without my password | OAuth |
| Enterprise login assertion | SAML |

## Still to do

Next are the missing incident response pieces (4.8): training, tabletop testing, root cause analysis, and threat hunting. After that comes the Domain 4 review quiz.
