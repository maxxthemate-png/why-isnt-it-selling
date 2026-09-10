# How to read a card

Every pattern card carries the same header fields.

**`tag`** says where the evidence came from.
- `[CC]` evidence from Claude Code and coding-agent products specifically.
- `[TA]` tool-agnostic evidence, from software products generally.
- `[CC/TA]` or `[TA/CC]` both, leading tag first.

**`category`** is one of `marketing`, `monetization`, `churn`, or a combination. It tells you which
failure mode the card speaks to.

**`status`** says whether the pattern survived adversarial refutation: an independent pass that tried to
break the claim rather than confirm it. `VERIFIED` survived. `completeness recovery` means it was
recovered from evidence an earlier draft under-weighted, and then verified. Anything that did not face
that stage says so.

**`verified`** is the date the evidence was last checked at source. Everything in this tier is
`2026-07-28`.

**`decay`** is how fast the card goes stale.
- `low` is a mechanism. Why a dashboard kills activation does not change when a platform does.
- `high` is channel-specific or tool-specific. A named platform, a flag, a program, a price. Re-check
  before acting.

**`confidence`**
- `verified` survived adversarial refutation.
- `lead (not adversarially verified)` corroborated but never stress-tested. Worth testing, not worth
  betting on.

**`Backing`** lists the evidence cluster IDs behind the card and the source URL for each. `cl_0146` is
an internal filing number; the URL next to it is the thing you can actually go read. Every claim is
traceable to a real page. If a card ever cites something you cannot open, distrust the card.

**`Value source`** says where the card's value comes from, and it is deliberately unglamorous:
- `volume` many independent sources said the same thing.
- `specificity` one source gave an unusually exact, copyable detail.
- `rarity` few people know it.
- `recency` it is new enough that most advice predates it.

None of this is secret. It is public but buried, in minute 47 of a podcast, a pinned comment, a GitHub
issue body. The value is that it was collected and checked, not that it was hidden.
