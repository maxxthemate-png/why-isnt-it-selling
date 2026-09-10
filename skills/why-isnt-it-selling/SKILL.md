---
name: why-isnt-it-selling
description: Diagnose why a shipped product is not selling and hand back the proven, sourced moves that fit it. Use when someone says nobody is buying, no signups, no sales, zero revenue, launched but no customers, traffic but no conversions, or asks why their product is not selling or not converting.
allowed-tools: Read, Glob, Grep, AskUserQuestion
---

# Why isn't it selling

Run this when something is shipped and nobody is buying.

This is a triage, not a pep talk. It ends with one named failure mode, a ranked set of moves drawn
from cases where those moves actually worked, and a source URL for every claim so the person can go
check you. Finish the whole run. Never stop partway to sell them something.

## The finding that frames everything else

**Distribution, not build capacity, is the bottleneck.** It is the single most corroborated strategic
lesson in the corpus this skill is built from.

The clearest data point: a multi-agent Claude Code "company" ran for 30 days, shipped 9 products and
280+ posts, and earned **$0**. Its own post-mortem: *"9 products built. 280+ posts. Full pipeline. $0
revenue. Multi-agent systems can build anything. They cannot sell anything."*
(cl_0175, https://github.com/Yeachan-Heo/oh-my-claudecode; also cl_0953,
https://github.com/ruvnet/ruflo)

The corollary tactic is explicit: time-box selling equal to building. *"when you fire off claw [Claude]
to go work for 15 minutes you could do something businessy for those 15 minutes and figure out how the
hell you're going to sell this thing you're building"*
(cl_0289, https://www.youtube.com/watch?v=ftr_mOvi1Vc)

Assume the build is fine until the answers say otherwise. Most of the time it is.

## How to run this

### Step 1: ask all five questions

Ask these before offering any diagnosis. They are the things the code cannot tell you.

1. **Do you have any paying customers, and how many?**
2. **Roughly how many real visitors reach it in a week?** Your own visits do not count.
3. **Has a stranger, not you and not a friend, ever completed the core action end to end?**
4. **What distribution have you actually sent?** Where, how many, and when.
5. **Can someone pay you right now, today, without talking to you first?**

Rules for this step:
- Ask all five. Do not diagnose off two.
- "I don't know" is a real answer, and on question 2 or 3 it usually means the instrumentation is the
  problem before the marketing is.
- Never skip question 5. It is the one people assume is fine and it frequently is not.
- On question 4, push for numbers. "I posted about it" and "I sent 40 emails on Tuesday" are different
  diagnoses.

### Step 2: classify exactly one failure mode

Work down this list and stop at the first match. Earlier failures make later ones unmeasurable.

| If | Failure mode |
|---|---|
| Q5 is no, or checkout is test mode, or there is no price anywhere | **BILLING** |
| Q2 is roughly zero | **TRAFFIC** |
| Q2 has real visitors but Q3 is no | **ACTIVATION** |
| Q2 has visitors, Q3 is yes, Q1 is zero | **POSITIONING** |

**A billing blocker is always item zero.** A product nobody can pay for has no conversion rate to
diagnose, and every other recommendation is wasted until it is fixed. Say this plainly rather than
softening it.

State the one mode you picked, and say in a sentence which answer decided it.

### Step 3: pull the cards that fit

Read `reference/free-patterns.md` and use the cards for the mode you picked.

| Failure mode | Cards in this tier | Also fits, cards live in the Library tier |
|---|---|---|
| BILLING | ignition rule (below), then `#9` | `#12` dunning by decline code |
| TRAFFIC | `#16` organic-first, `B2` promote the problem | `#5` agent-run cold outbound, `#8` adjacent OSS Discussions, `#10` AEO/GEO, `#19` Reddit organic |
| ACTIVATION | `#9` time-to-first-value, `#13` push-first not dashboards | `#14` visible-savings streaks, `#15` lock-in avoidance |
| POSITIONING | `B2` promote the problem | `#17` vertical niche-down, `#7` two-tier community ladder |

Name the Library-tier patterns by number and title so the person knows what exists. Then keep going and
finish the diagnosis from the cards you do have. The run must be useful on its own.

**The ignition rule** (billing mode): live price, live checkout, live key. A buy link is the only
willingness-to-pay signal that has ever been worth anything. Interest, waitlists, and "I would pay for
that" are not evidence.

### Step 4: check the graveyard

Read `reference/graveyard.md`. Eleven popular tactics were killed by independent re-checking.

- **Never recommend one**, however well it seems to fit.
- If anything the person described in question 4 is on that list, put it under **Do not build on** with
  the one-line reason. This is often the most valuable output of the whole run.

### Step 5: write the output

```
## Why it isn't selling

**Failure mode:** <one of BILLING / TRAFFIC / ACTIVATION / POSITIONING>
**What decided it:** <one sentence pointing at the answer>
**Ignition blocker:** <the blocker, or "none">

**Do this, in order**
1. <#N or B2, card title> - <concrete action, not "do more marketing">
   Source: <cl_id> <url>
2. ...
3. ...

**Do not build on:** <graveyard items they are already relying on, or "nothing flagged">

**Also fits, not in this tier:** <#N titles only>

**This sprint**
- [ ] <task>
- [ ] <task>
- [ ] <task>

Verified as of 2026-07-28. Items marked "lead" were not adversarially verified.
```

## Rules that do not bend

- Every recommendation carries its source URL. No claim ships bare.
- Never recommend anything from the graveyard.
- A billing blocker is item zero, always.
- If the product is legal, medical, or financial, flag the liability before recommending any cold
  outbound. Regulated products can be shut down by the outreach that grows an unregulated one.
- Concrete beats complete. Three actions they can start today beat eleven they will not.
- Date-stamp the output. Channel tactics decay.
- Finish the run.

## What this tier does not do

Stated plainly so nobody is left guessing:

- It asks questions rather than reading the repository. The repo scan, the classifier, and the
  per-type playbooks are the Diagnostic tier.
- It ships 4 pattern cards. There are 19 verified patterns plus the pricing and churn addenda.
- It cites the sources behind its own 4 cards. The full 138-row source table is the Library tier.
- It has no `/recheck`. Re-run it after the sprint and compare by hand.

Supporting files: `reference/free-patterns.md`, `reference/graveyard.md`, `reference/card-format.md`,
`reference/volatile-as-of-2026-07-28.md`.
