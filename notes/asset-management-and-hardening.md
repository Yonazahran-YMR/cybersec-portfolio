# Domain 4: Security Operations

## Session 1: Asset Management & Hardening

Starting Domain 4 with the two concepts everything else in this domain builds on.

### Asset management

Basically: you can't protect what you don't know you have. Three layers to it.

1. Inventory: knowing every device, server, app, and cloud resource that exists. Sounds obvious but this is where a lot of real breaches trace back to, a forgotten server nobody was tracking.
2. Classification: tagging assets by how critical or sensitive they are. A dev test box and a production database server don't get the same level of scrutiny.
3. Enumeration: actively discovering what's on the network, not just trusting a spreadsheet someone made two years ago.

This feeds directly into vulnerability management. Can't patch or scan something that isn't in the inventory in the first place.

### Hardening

What you do once you know what you have. Reducing attack surface on each asset.

1. Disable unused services and ports. If a server doesn't need SMB running, turn it off.
2. Change default credentials. Still a top finding in real-world assessments even though it feels obvious.
3. Apply secure baselines. CIS Benchmarks are the free, open standard here, they give a checklist per OS/platform.
4. Patch management on a defined cadence, not "whenever someone remembers."

### Scenario I'm working through

Legacy file server, 8 months unpatched, running SMBv1, reachable from the general employee VLAN. Three separate findings, three separate control categories (patch management vs hardening vs segmentation), even though they all stack into one overall risk picture. Working through the reasoning next session.
