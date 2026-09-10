# why-isnt-it-selling

[![installs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/maxxthemate-png/why-isnt-it-selling/main/stats/badge-cloners.json)](https://github.com/maxxthemate-png/why-isnt-it-selling)
[![stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/maxxthemate-png/why-isnt-it-selling/main/stats/badge-stars.json)](https://github.com/maxxthemate-png/why-isnt-it-selling/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

You shipped it and nobody is buying. Install this and Claude Code diagnoses why, then hands you the
proven moves that fit your product, each one with a source you can go read.

Built from 4,300 real cases of what sold vibe-coded products, plus the 11 popular tactics that did not
survive verification.

## Install

```
/plugin marketplace add maxxthemate-png/why-isnt-it-selling
/plugin install why-isnt-it-selling
```

Then run `/why-isnt-it-selling` in any project.

## What it does

It asks you five questions, names one failure mode, and gives you a ranked set of moves with a source
URL on every claim.

- **The finding that frames everything.** Distribution, not build capacity, is the bottleneck. The
  clearest case in the corpus is a multi-agent build system that shipped 9 products and 280+ posts in
  30 days and earned $0.
- **Four full pattern cards** that apply to almost any product: collapse time-to-first-value, push-first
  instead of dashboards, organic before paid, and promote the problem instead of the product.
- **The complete graveyard.** Twenty patterns went through adversarial refutation. Eleven died. All
  eleven are here, with what killed them. This is the part nobody else gives you.
- **A hard rule about billing.** If nobody can pay you today, that is the entire diagnosis and every
  other recommendation is noise until it is fixed.

Every card carries the date its evidence was checked and how fast it goes stale.

## What it does not do

Stated plainly rather than discovered halfway through a run:

- It asks questions. It does not read your repository. The repo scan, the classifier and the per-type
  playbooks are a separate paid tier.
- It ships 4 of the 19 verified patterns.
- It cites the sources behind its own 4 cards, not the full 138-row source table.

The run always finishes. It will never wall partway through and ask you for money.

## No telemetry

The skill declares `allowed-tools: Read, Glob, Grep, AskUserQuestion`. It has no shell access, no
network tools, and no way to phone home. Nothing you tell it leaves your machine.

## Where the evidence comes from

3,549 evidence clusters distilled from YouTube, podcasts, GitHub, Reddit, Indie Hackers and dev.to.
Every claim in every card carries a cluster ID and the URL behind it. None of it is secret. It is
public but buried, in minute 47 of a podcast or a pinned comment or a GitHub issue body. The value is
that it was collected, cross-checked, and adversarially refuted.

Verified as of 2026-07-28.

## The paid tiers

Both are available now, not pre-orders, and both are delivered as Claude Code plugins.

**$27, The Library.** All 19 verified patterns with mechanism, evidence and resolved source URLs. The
complete 11-item graveyard with what killed each one. The pricing and churn addenda, labelled as
unverified leads. A 138-row source table where every claim resolves to a page you can open.
[Get it](https://buy.stripe.com/8x29AUbb32b12zqfPpejK00).

**$91, The Diagnostic.** Everything above, plus `/diagnose`: it reads your repository, classifies type,
stage and failure mode from real code signals, and returns a ranked plan naming your own files rather than
speaking in general terms. Adds `/recheck`, `/pattern`, five per-type playbooks, and lifetime updates.
[Get it](https://buy.stripe.com/5kQeVegvn7vl6PGav5ejK01).

For scale: the $91 tier is less than half a month of a $200 assistant subscription, and it is one payment.

**How delivery works.** You enter your GitHub username at checkout, get added as a read-only collaborator
on the private repo, and install with two commands. Your own git credentials authorize it, so there is no
license key. Updates arrive through `/plugin update`.

**What is honestly not promised.** Everything is verified as of 2026-07-28. Cards are marked `decay: low`
or `decay: high`, the volatile facts are quarantined in their own file, and that file is refreshed at
least every 90 days. There is no promise of a full research re-run on a fixed schedule, because that costs
a multiple of the original build and promising it would be a lie with a date on it.

## License

MIT. See [LICENSE](LICENSE).
