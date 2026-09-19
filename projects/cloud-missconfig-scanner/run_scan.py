import json
from collections import Counter
from check_security_groups import check_security_groups
from check_public_buckets import check_public_buckets
from check_iam_policies import check_admin_policies

ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

def run_all():
    findings = []
    for check in (check_security_groups, check_public_buckets, check_admin_policies):
        findings.extend(check())
    return sorted(findings, key=lambda f: ORDER[f["severity"]])

if __name__ == "__main__":
    results = run_all()
    for f in results:
        print(f"{f['severity']: <9} {f['check_id']: <28} {f['resource']}")

    counts = Counter(f["severity"] for f in results)
    print()
    for sev in ORDER:
        print(f"{sev: <9} {counts.get(sev, 0)}")
    print(f"total: {len(results)}")

    with open("report.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)