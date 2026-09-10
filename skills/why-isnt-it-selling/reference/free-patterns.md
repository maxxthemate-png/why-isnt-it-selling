# Pattern cards, free tier

Four cards. Read `card-format.md` if the header fields are unfamiliar.

Three survived adversarial refutation. One (`B2`) is a corroborated lead that did not go through that
stage, and is labelled as such. Volatile specifics (tool flags, install mechanics, platform rules) are
kept out of these cards and live in `volatile-as-of-2026-07-28.md`, because they rot faster than the
mechanisms do.

---

## #9. Collapse time-to-first-value to near zero

`tag: [CC]` · `category: marketing / churn` · `status: VERIFIED`
`verified: 2026-07-28` · `decay: low` (the mechanism; the named install mechanics are high-decay and
sit in the volatile file) · `confidence: verified`

**Mechanism.** Delete the setup step instead of documenting it. Working instances: one copy-paste
command telling the user's own agent to fetch a hosted onboarding file and follow it interactively
(cl_0146, cl_0378); a single installer command that clones, enables and wires everything in one move
(cl_0039); a browser-only bring-your-own-key tool with no account and no sign-in, usable in well under
a minute (cl_0307, cl_0308); a one-line marketplace install replacing a clone-and-symlink flow
(cl_0167). The diagnosis underneath all of them is the same: find the exact step where a new user
quits, then remove that step (cl_0073, cl_0451).

Quotable proof of how low the bar is:
> "No account creation. No OAuth dance. No 'should I trust this site with my key?' hesitation. Open the
> URL, paste a key, hit send. The tool is yours in under thirty seconds." (cl_0307)

**Backing**
- cl_0146 https://github.com/FlorianBruniaux/claude-code-ultimate-guide
- cl_0378 https://dev.to/wasp/open-vibe-ship-your-saas-with-ai-without-getting-stuck-e2h
- cl_0039 https://dev.to/great_cto/greatcto-v217-no-more-tambourine-dance-1p5p
- cl_0167 https://github.com/Imbad0202/academic-research-skills
- cl_0307 https://dev.to/ferhatatagun/what-i-learned-shipping-four-open-source-claude-dev-tools-in-two-weekends-1f4f
- cl_0308 https://dev.to/chetan_hs_c12b4d5cd3fdded/i-built-10-free-claude-code-tools-in-a-weekend-heres-what-i-learned-2bik
- cl_0073 https://www.youtube.com/watch?v=Gry_nrydBp0
- cl_0451 https://www.youtube.com/watch?v=0WDkwMxj13s

**Value source:** specificity. The friction-point diagnoses are the buried part. Everyone agrees
onboarding matters; almost nobody names the screen people quit on.

**How to apply it.** Time yourself from a stranger's first click to their first useful output. If that
number is over about a minute, that number is your conversion problem, not your copy.

---

## #13. Push-first, not dashboards. The dashboard is what kills activation.

`tag: [CC/TA]` · `category: churn` · `status: VERIFIED (completeness recovery)`
`verified: 2026-07-28` · `decay: low` · `confidence: verified`

**Mechanism.** A dashboard-first product got called "cool" by testers and was never reopened. The team
pivoted to push-first threshold alerts and the product started doing its job (cl_0041). The general
lesson repeats: diagnose the exact onboarding screen where users drop and fix that bottleneck instead
of shipping more features (cl_0003). Where the value is invisible, surface it by pushing it out, for
example an emailed "wrapped"-style report card built from data the user never looks at (cl_0273).

The source, verbatim, because the headline number is easy to misread:
> "started with dashboards, not alerts; testers said 'cool' and never opened it again. Pivoted to
> push-first notifications; usage dropped 30% in one beta team the week after shipping budget threshold
> alerts." (cl_0041)

Read that carefully. The product measured AI spend. The 30% that dropped was the customer's **spend**,
because the alerts made them act. It is the product working, not engagement falling.

**Backing**
- cl_0041 https://www.indiehackers.com/post/we-surveyed-50-teams-about-ai-spend-only-3-could-answer-heres-what-we-built-53fb6f5f6c
- cl_0003 https://www.youtube.com/watch?v=IywUW2RjXis
- cl_0273 https://www.youtube.com/watch?v=VbqaL_eHhKY

**Value source:** specificity. It directly contradicts the default instinct that the dashboard is the
deliverable.

**How to apply it.** If your product's home screen is a dashboard, assume it is the problem. Ask what
single event is worth interrupting someone for, and send that instead. A dashboard requires the user to
remember you. A push does not.

---

## #16. Organic first, then pour paid fuel. The honest spend sequence.

`tag: [TA]` · `category: marketing / monetization` · `status: VERIFIED (completeness recovery)`
`verified: 2026-07-28` · `decay: low` · `confidence: verified`

**Mechanism.** Prove the model cheaply before real ad spend. One operator went from roughly $3K/month
on organic and creator content, to $10K after fixing the paywall, to $30K by month five, and only then
switched on paid ads to scale past $100K (cl_0656). A second case spent $250 on a single influencer
thread, got roughly 300K organic impressions and real revenue, then reinvested into more of the same
before diversifying (cl_0294). This is the correct reading of "the first spend is a demand test", and
it directly counters any instinct to launch ads immediately.

> "In month five, it was about 30K a month as I explored even more formats. And after 30K a month, it
> was simply just putting it on paid ads to scale to over 100." (cl_0656)

**Backing**
- cl_0656 https://www.youtube.com/watch?v=EQfZCe3MkTU
- cl_0294 https://www.indiehackers.com/post/3FvQoHUh2SglJvAJGkSF

**Value source:** specificity. It is an evidenced sequence with real thresholds, not the usual advice to
"validate first".

**How to apply it.** Paid ads scale a channel that already converts. They do not create one. If nothing
organic converts yet, ad spend buys you a faster answer to a question you can answer for free.

---

## B2. Promote the problem, not the product

`tag: [TA]` · `category: marketing` · `status: corroborated 3x independently, NOT adversarially verified`
`verified: 2026-07-28` · `decay: low` · `confidence: lead (not adversarially verified)`

**Mechanism.** Three unrelated operators, same move:
- A companion podcast and newsletter devoted to explaining the problem rather than the product:
  *"I don't actually promote my product. I promote the problem I'm solving."*
- Weeks of problem-only posting before a launch, so that *"by launch day people already agreed with the
  problem"*. The product then reads as the answer instead of a pitch.
- Purely educational niche content with the product mentioned only incidentally. One post reached
  roughly 1.5M impressions and 150+ beta users, *"mainly because the content itself was valuable."*

**Backing**
- Product Hunt discussion thread https://www.producthunt.com/p/general/how-do-you-promote-your-product-without-sounding-too-salesy

**Value source:** volume of independent corroboration within a single high-signal source. Forum threads
are where founders state real numbers, because they are answering a peer rather than marketing at an
audience.

**Confidence caveat.** This came from a small late addition to the corpus (37 cards out of 4,278) that
did not go through the adversarial refutation stage. Treat it as a strong lead to test, not a verified
pattern. Everything above it on this page survived refutation; this did not face it.

**How to apply it.** Write the thing your buyer would read even if your product did not exist. Mention
the product once, at the end. If the piece is only interesting to someone already considering buying,
it is an ad, and it will perform like one.
