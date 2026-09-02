# Zero Trust Architecture

First real session in Domain 3, building on the "never trust, always verify" principle I already had from Domain 1. Today was about the actual architecture behind that principle.

## Control plane vs data plane

Zero Trust splits into two planes.

Control plane decides if access is allowed. This is the policy engine, adaptive identity checks, all the "should this be allowed" logic. Data plane is what actually carries the traffic once approved, this is the part that happens after the gate opens.

Two components sit inside this. PDP, policy decision point, is the brain that evaluates the request. PEP, policy enforcement point, is the actual gate, it takes whatever the PDP decided and enforces it, allow or block. Important distinction I kept messing up early in this session, PDP decides, PEP enforces, they're separate components even though they always work together.

## Implicit trust

The core principle Zero Trust is trying to kill off is implicit trust, meaning "already inside the network" being treated as good enough permission. A flat internal network where one compromised laptop can reach the finance server, HR database, and domain controller with no further checks, that's implicit trust in action, and it's the exact opposite of never trust always verify.

I actually got tripped up on this at first, I called it a "Control Plane" violation instead of naming implicit trust as the principle. Control Plane is a component, not a principle, that was the correction I needed.

## Segmentation types

This is the part that actually enforces Zero Trust in the data plane.

Network segmentation splits the network into broad zones, like VLANs, coarse grained. Microsegmentation goes further, each individual server or workload gets its own enforced policy, even if they're sitting in the same VLAN. This is the fix for lateral movement within a zone, not just between zones.

Screened subnet, also called DMZ, is specifically for public facing services. It isolates something like a public web server between two firewalls, one facing the internet and one facing the internal network, so the internet can reach the web server but never the internal database directly. The condition that makes something a DMZ specifically is that public exposure, I learned this the hard way by mislabeling a plain internal VLAN split as a DMZ when there was no internet facing component involved at all.

Jump box or bastion host is different again, it controls an access path, specifically how admins reach sensitive systems. It's not the same as stopping lateral movement in general, that's still microsegmentation's job.

## Scenarios and mistakes worth remembering

Flat network scenario, one phished laptop reaching finance, HR, and DC freely. Answer here is implicit trust violated, fix is microsegmentation so every resource re-checks access, not just adding more identity checks at the login gate. I initially reached for "add more Control Plane checks" which doesn't fix a Data Plane enforcement gap.

VPN scenario, comparing a company where login is the only gate versus a company where a PDP and PEP both operate per resource. The mistake I made here was collapsing "PDP decides" and "PEP enforces" into one step in my answer. They're two separate actions.

DMZ scenario, correctly identified a public web server between two firewalls as DMZ. Follow up question asked what stops an attacker who gets past that DMZ from moving further internally, I answered jump box, but the more accurate answer is microsegmentation. Jump box controls who can initiate admin access, it doesn't stop an already compromised host from reaching other internal hosts on its own.

## Patterns to watch

Two things showed up more than once tonight. First, merging PDP and PEP into a single step instead of naming them as separate decide vs enforce actions, this got fixed by the third scenario. Second, picking a segmentation term without checking its specific defining condition, especially DMZ requiring actual public/internet exposure, not just "some kind of network split."

## Status

Domain 3 in progress. Control plane, data plane, PDP, PEP, implicit trust, and segmentation types (network, micro, DMZ, jump box) covered. More Domain 3 topics still ahead.
