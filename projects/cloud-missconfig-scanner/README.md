# Cloud Misconfiguration Scanner

A small Python scanner that looks for common AWS misconfigurations and prints one sorted report. Right now it has three checks: security groups open to the whole internet, S3 buckets that are publicly exposed or missing a public access block, and IAM policies that allow every action on every resource.

I built this as my second portfolio project, after the log parser. The first one taught me detection logic on the SOC side. This one is me learning what "misconfiguration" actually looks like in code, since I'm heading toward cloud security.

## Why it runs against moto and not real AWS

I'm a student and I really didn't want a surprise bill from a real AWS account. I started with LocalStack, but its image now needs an auth token to start, so I switched to moto, which runs as a plain Python process with no login and no Docker. The scanner uses normal boto3 calls, so the code would work on a real account by removing the endpoint override. I haven't tested that though, and I'm not claiming it. More on that in the limitations section.

## What it checks

**Security groups** (`check_security_groups.py`): flags any inbound rule open to `0.0.0.0/0` or `::/0`, then rates it by what's exposed.

| Rule | Severity | Reasoning |
|---|---|---|
| All traffic open to the world | CRITICAL | No port restriction at all |
| Range includes SSH (22) or RDP (3389) | CRITICAL | Admin access from anywhere |
| Single port 80 or 443 | LOW | Public web is often intended |
| Anything else open to the world | HIGH | Exposed, and I can't tell if it's meant to be |

These ratings are my own judgment calls, not an official standard.

**S3 buckets** (`check_public_buckets.py`): two separate findings so the report says what's actually wrong.

| Finding | Severity | Reasoning |
|---|---|---|
| Public ACL with write permission | CRITICAL | Anyone can change the contents |
| Public ACL, read only | HIGH | Anyone can read the contents |
| Public ACL, but full public access block is on | LOW | The block neutralizes it, still worth cleaning up |
| No public access block configured | MEDIUM | Not exposed by itself, but the safety net is missing |

If the scanner can't read a bucket (say, access denied), it logs a warning and moves on. I decided that "couldn't check" is not the same as "found a problem," so it doesn't create a finding.

**IAM policies** (`check_iam_policies.py`): looks at customer-managed policies and flags any Allow statement that grants every action on every resource. That's CRITICAL, since it's effectively full admin.

The part that tripped me up: AWS lets `Statement`, `Action`, and `Resource` each be either a single value or a list, so `"Action": "*"` and `"Action": ["*"]` mean the same thing. A small helper turns everything into a list first, so the check works for both shapes.

## Running it

You'll need Python 3 and a terminal. Commands below are for Windows cmd.

1. Create the environment and install dependencies:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
2. In one terminal, start moto:
```
moto_server -p 4566
```
3. In a second terminal (venv active), seed the fake account with test resources, then scan:
```
python seed.py
python run_scan.py
```

Moto keeps everything in memory, so restarting it wipes the seeded resources. Just run `seed.py` again.

## The test resources

`seed.py` creates a bad and a good version of each thing, so there are known right answers to check against.

| Resource | What it is | Expected result |
|---|---|---|
| bad-sg | SSH open to 0.0.0.0/0 | CRITICAL |
| worst-sg | All traffic open to 0.0.0.0/0 | CRITICAL |
| web-sg | HTTPS open to 0.0.0.0/0 | LOW |
| good-sg | SSH from 10.0.0.0/16 only | no finding |
| bad-public-bucket | Public read ACL, no access block | HIGH and MEDIUM |
| good-private-bucket | Full public access block | no finding |
| bad-admin-policy | Allow everything on everything | CRITICAL |
| good-readonly-policy | Read one object in one bucket | no finding |

The default security group that moto creates should also stay clean, and it does.

## Sample output

```
CRITICAL  SG_OPEN_INGRESS              worst-sg
CRITICAL  SG_OPEN_INGRESS              bad-sg
CRITICAL  IAM_ADMIN_POLICY             bad-admin-policy
HIGH      S3_PUBLIC_ACL                bad-public-bucket
MEDIUM    S3_NO_PUBLIC_ACCESS_BLOCK    bad-public-bucket
LOW       SG_OPEN_INGRESS              web-sg

CRITICAL  3
HIGH      1
MEDIUM    1
LOW       1
total: 6
```

Every run also writes the full findings to `report.json`, with the check ID, resource, and severity for each one.

## Tests

```
pytest -v
```

Moto has to be running first. The tests reset moto and reseed before each run, so you don't need to restart anything by hand. They check the severity of each bad resource, that `worst-sg` has no ports, that the bad bucket produces exactly two findings with the right IDs, and that none of the good resources get flagged. That last one matters most to me, since a scanner that cries wolf gets ignored.

Something that made tests click for me: I temporarily changed the `web-sg` rating and watched a test fail with the expected and actual values side by side. After that I understood why people bother.

## Limitations

1. **Tested against moto only.** I haven't run this on a live AWS account, and moto doesn't behave exactly like AWS in every case.
2. **Three checks.** There's no encryption, logging, or anything else yet.
3. **S3 checks look at ACLs and the public access block, not bucket policies.** A bucket made public through a policy would be missed.
4. **The IAM check only flags `*` on `*`.** Broad but partial wildcards like `s3:*` on everything aren't flagged. It ignores `Condition` blocks, skips inline policies on users and roles, and doesn't check whether a policy is attached to anything.
5. **IPv6 open rules are handled in the code but not covered by a test.** Moto's support there is patchy, so I left it out rather than fake it.
6. **The "public ACL but fully blocked" downgrade to LOW has no seeded example**, so it isn't tested yet.
7. **One region only** (us-east-1), and the severity ratings are my own judgment.
8. **The `reference` field is a generic pointer** to CIS AWS Foundations. Mapping each finding to its exact control ID is still on my list.

## What's next

1. Map findings to exact CIS control IDs.
2. Catch partial wildcards in IAM policies.
3. Cover the missing test cases from the limitations list.
4. Try the same checks against a real account with strict billing alerts, once I'm comfortable with that.

## Files

```
seed.py                    creates the test resources in moto
check_security_groups.py   security group check
check_public_buckets.py    S3 check
check_iam_policies.py      IAM check
run_scan.py                runs every check, prints the report, writes report.json
test_scanner.py            pytest suite
requirements.txt           dependencies
```
