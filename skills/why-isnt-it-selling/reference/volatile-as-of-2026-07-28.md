# Volatile as of 2026-07-28

**True on this date, probably not now.** Platforms rename things, programs close, flags change, and
prices move. These specifics were deliberately pulled out of the pattern cards so a stale detail cannot
quietly poison a mechanism that is still sound.

Re-check anything here before acting on it. The cards it was removed from stay valid without it.

## Install and onboarding mechanics (behind `#9`)

- **One-line plugin marketplace install.** One project cut install from a clone-and-symlink flow to
  `/plugin marketplace add <owner>/<repo>` followed by `/plugin install <name>`, while keeping the
  manual path working. (cl_0167, https://github.com/Imbad0202/academic-research-skills)
- **Single-command installers.** `npx <tool> install` replacing a sequence of clone, locate
  dependencies, enable in settings, restart. (cl_0039,
  https://dev.to/great_cto/greatcto-v217-no-more-tambourine-dance-1p5p)
- **Agent-fetched onboarding.** A copy-paste prompt telling the user's agent to fetch a hosted
  `llms.txt` or raw onboarding markdown and follow it. (cl_0146, cl_0378)
- **Permission prompts as the drop-off point.** At the time, some tutorials told beginners to launch
  with the permission checks disabled because the repeated prompts were where people quit. That is a
  real security tradeoff and it is named here rather than in the card so nobody treats it as a
  recommendation. The durable lesson is "find the step where people quit", not "use that flag".
  (cl_0073, https://www.youtube.com/watch?v=Gry_nrydBp0)

## Platform specifics (behind `B2`)

- The three corroborating cases came from Product Hunt discussion forums. Forum mechanics, scoring, and
  moderation rules on that platform change often. The mechanism, promote the problem rather than the
  product, is not platform-specific and holds regardless.

## Numbers that are cases, not benchmarks

The figures in the cards ($3K to $10K to $30K to $100K in `#16`, $250 to 300K impressions in `#16`,
1.5M impressions to 150+ beta users in `B2`, 30% spend reduction in `#13`) are what happened to specific
people in specific niches. They show a sequence is possible. They are not targets, and they are not
forecasts for anyone else.
