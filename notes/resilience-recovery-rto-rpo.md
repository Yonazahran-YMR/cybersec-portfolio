# Resilience & Recovery: RTO/RPO, HA, Site Types (Sec+ Domain 3.4)

Started 3.4 tonight, the last domain 3 subtopic. Opened with a review scenario on data classification and data sovereignty from last session, both came back clean, no corrections needed.

## RTO vs RPO

Two different questions that get confused easily.

| Metric | Question it answers | Example |
|---|---|---|
| RTO (Recovery Time Objective) | How long can we be down before it's unacceptable | "We must be back online within 4 hours" |
| RPO (Recovery Point Objective) | How much data can we afford to lose | "We can lose at most 15 minutes of data", determines backup frequency |

The distinction that matters, RTO is about time to restore service, RPO is about how far back your last good backup needs to be. A tight RPO demands frequent backups regardless of how fast you can restore, a tight RTO demands fast restoration or failover regardless of backup frequency. They're independent knobs, not the same thing measured two different ways.

## High availability and redundancy

Redundancy means duplicate components so one failing doesn't cause an outage, extra servers, power supplies, network paths. High availability is the overall goal or design outcome, minimal downtime, often expressed as five nines, 99.999% uptime. Failover is the automatic switch to a backup system when the primary fails. Load balancing distributes traffic across multiple servers and also provides redundancy as a side effect, since one server failing doesn't take down the whole service.

## Site types for disaster recovery

| Site type | Readiness | Cost |
|---|---|---|
| Hot site | Fully operational, real-time data replication, can fail over almost instantly | Highest cost |
| Warm site | Partially configured, hardware ready but data needs syncing, hours to become operational | Medium cost |
| Cold site | Just physical space and power, no equipment ready, days to weeks to become operational | Lowest cost |

## Scenario I worked through

Bank's core transaction system needs to be back online within 15 minutes of any outage, and can tolerate losing at most 30 seconds of transaction data. They maintain a fully mirrored, real-time-synced secondary data center ready to take over instantly.

Correctly identified 15 minutes as RTO and 30 seconds as RPO. Correctly identified the secondary data center as a hot site, and tied the mechanism to the requirement instead of just naming it, real-time replication satisfies the tight RPO (near zero data loss since it's constantly synced), and instant failover capability satisfies the tight RTO (minutes, not hours).

## Status

Domain 3.4 in progress. RTO/RPO, high availability/redundancy, and site types covered. Backup types (full, incremental, differential) still ahead before this domain, and Domain 3 as a whole, is fully closed.
