# Backup Types (Sec+ Domain 3.4)

This closes out 3.4, and with it, all of Domain 3. Opened with a review scenario on RTO/RPO and site types from last session, correctly caught that a warm site with an hours-long recovery timeline doesn't actually satisfy a 30 minute RTO requirement, which was the real point of that question, applying the mismatch instead of just accepting the label at face value.

## The three backup types

| Type | What it backs up | Restore speed | Storage cost |
|---|---|---|---|
| Full backup | Everything, every time | Fastest restore, one backup to restore | Highest storage cost |
| Incremental backup | Only what changed since the last backup (full or incremental) | Slowest restore, need full plus every incremental since | Lowest storage cost |
| Differential backup | Only what changed since the last full backup | Medium restore, need full plus latest differential only | Medium storage cost |

## The trap that mattered most

Incremental vs differential, both sound like "just the changes" but the reference point is different. Incremental only looks back to the previous backup, whatever that was, so restoring means replaying a full chain, full then incremental 1 then incremental 2 then incremental 3, in order. Differential always looks back to the last full backup, so each differential backup grows larger over time, but restoring only ever needs two pieces, the full backup plus the most recent differential, no chain to replay.

## Scenario I worked through

Company runs a full backup every Sunday. Monday, Tuesday, Wednesday backups each only capture changes since Sunday's full, meaning Wednesday's file is the largest of the three. Server crashes Thursday, needs restoration from Wednesday's backup.

Correctly identified this as differential, and pulled the right evidence, each backup referencing back to Sunday's full (not the previous day's backup) is the defining trait, plus the detail that Wednesday's file being the largest confirms it since differentials accumulate everything since the full over time. Correctly identified the restore only needs two files, Sunday's full plus Wednesday's differential, no chain through Monday and Tuesday needed.

## Status

Domain 3.4 (resilience and recovery) is now fully closed. Covered: RTO/RPO, high availability and redundancy, site types (hot, warm, cold), and backup types (full, incremental, differential).

This closes Domain 3 entirely. All four subtopics done: 3.1 architecture models, 3.2 secure infrastructure, 3.3 protect data, 3.4 resilience and recovery.

Next session is a hands-on session to apply what's been covered across Domain 3, since it's been all theory for a while now.
