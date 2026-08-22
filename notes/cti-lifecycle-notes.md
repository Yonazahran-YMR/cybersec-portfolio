# CTI Lifecycle 

The Cyber Threat Intelligence process, 5 steps in order:

1. Identify the most critical cyberthreats (Direction) - figure out what to even
   focus on first
2. Collect threat information (Collection) - gather raw data
3. Process the information (Processing) - clean and organize the raw data into
   something usable
4. Analyze and look for indicators of compromise / IoCs (Analysis) - find meaning,
   spot patterns
5. Disseminate the information (Dissemination) - share findings with the people
   who need it

## Why this order makes sense
Can't collect data usefully without knowing what you're even looking for first
(Direction has to come first). Raw collected data is messy, so it needs Processing
before Analysis can actually find anything meaningful in it. Dissemination is
always last since there's no point sharing intel before it's actually been
analyzed into something useful.

This mirrors the general Intelligence Cycle used way beyond just cybersecurity -
military intel, law enforcement, corporate risk teams all follow this same basic
structure.

## Quick test I got right
A team with messy, uncleaned, duplicate firewall logs is stuck at the Processing
step, not Analysis - you can't meaningfully analyze data that hasn't been
cleaned/organized yet.
