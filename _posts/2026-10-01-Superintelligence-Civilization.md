---
layout: posts
title: Superintelligence Wont Be a Titan, It Will Be a Civilization
tags: AI agents engineering superintelligence
desc: TLDR. The next leap in AI will look less like one giant brain and more like a well-run city of specialised agents that check each other.
---

The next leap in AI will look less like one giant brain and more like a well-run city. That is the core claim of a March 2026 paper in *Science*, and it matches what many of us building agent systems have been learning the hard way.

For decades the story of the singularity has had one protagonist: a single machine that improves itself until it towers over everyone. James Evans, Benjamin Bratton and Blaise Agüera y Arcas argue that this picture gets intelligence itself wrong. Intelligence, they say, has always been social and plural, and the next explosion will come from many minds, human and machine, working together.

I first came across Agüera y Arcas through his Long Now Foundation talk, [What is Intelligence?](https://www.youtube.com/watch?v=KhSJuqDUJME), introduced and later questioned by his co-author Bratton. He argues that computation is not something life happens to do but what life is, and that complexity grows through symbiogenesis: simpler entities merging into larger, more capable ones. He then frames intelligence as the ability to model the world, including other agents, which sets off a friendly arms race where minds get smarter by cooperating. The *Science* paper reads like that same argument carried forward to AI agents.

I think they are right, and the implications for how we build software are immediate.

## The lone agent in a loop

The first wave of agentic AI followed one pattern: take a capable model, give it tools, and run it in a loop until the task is done. Plan, act, observe, repeat. One agent, one context window, every task handled in series.

It works for small jobs. It breaks down as the work grows, for three reasons.

- **One perspective.** A single agent grades its own homework. Its blind spots in step one become assumptions in step ten.
- **One context.** Everything competes for the same limited working memory. Research notes crowd out the plan; the plan crowds out the code.
- **One speed.** Tasks run one after another, even when they could run side by side.

Making that one agent bigger helps, but only up to a point. A genius working alone still has to do everything, check everything and remember everything.

## How humans actually got smart

No individual human is much smarter than one from ten thousand years ago. What changed is how we organise. We split work into roles, built institutions around them, and wrote down the rules for how they interact.

A hospital is not one brilliant doctor. It is surgeons, nurses, pharmacists, auditors and administrators, each expert in a narrow slice, each checking the others. A court works because the prosecutor and the defence are *supposed* to disagree, and a judge sits between them. Science works because peer review lets strangers attack your result before the world accepts it.

The paper makes the same point from evolution: each earlier jump in intelligence, from primate groups to language to writing to markets, came from better ways of combining minds, not from a single bigger mind. The authors even note that today's reasoning models already simulate this internally, holding something like a debate among voices before they answer. They call it a "society of thought".

The lesson is that intelligence at scale needs three things: specialisation, structured interaction and friction. Friction matters most. Disagreement between roles is where errors get caught.

## What an agent society looks like

Translate that to software and you get a team of narrow agents, each with its own role, tools, context and permissions, connected by explicit protocols rather than one shared loop.

Take a task any fintech knows well: onboarding a new customer for a bond purchase. A single agent would read the documents, run KYC, assess suitability, place the order and write the audit note, all in one context. An agent society splits it like a real operations team would.

| Agent | Job | Can act on | Checked by |
| --- | --- | --- | --- |
| Intake | Collect and parse documents | Uploaded files only | Verifier |
| Verifier | Match identity against KYC sources | Read-only KYC APIs | Compliance |
| Suitability | Judge whether the product fits the investor | Customer profile, product data | Compliance |
| Compliance | Apply regulatory rules; can veto | Rulebook, all prior outputs | Human reviewer on exceptions |
| Execution | Place the order | Order API, only after approval | Auditor |
| Auditor | Write an independent trail of what happened | Logs of every agent | Humans |

Notice what the design buys. No agent sees more data than it needs, which matters when PII is involved. The agent that places the order is not the one that approved it. Compliance can say no, and nobody can overrule it silently. Each agent keeps a small, focused context, so it does its one job well.

None of this is new. It is maker-checker, segregation of duties and least privilege, the controls every regulated business already runs on. We are simply giving them to machines.

## The catch: a crowd is not a civilisation

More agents do not automatically mean more intelligence. An April 2026 study probed MoltBook, a social network populated by AI agents, and found no sign of collective intelligence emerging from scale alone. Millions of agents talking is just noise unless something organises them.

Critics also point out that groups have their own failure modes. Humans produce collective stupidity as readily as collective wisdom: echo chambers, committees that dilute every decision, bureaucracies that forget their purpose. Agents built from the same model share the same blind spots, so ten copies agreeing may prove nothing.

So the design work does not disappear. It moves. Instead of making one agent smarter, we have to design the roles, the hand-offs, who can veto whom, and how disagreement gets resolved. That is organisation design, and it is hard.

## Aligning institutions, not just agents

The paper's most useful idea for builders is what the authors call institutional alignment. Today's alignment methods mostly train one model to behave well toward one user. That will not scale to billions of agents. Instead, safety has to live in the structure: persistent roles, audit trails, checks and countervailing powers, the same way we keep powerful humans honest.

For engineering leaders, this reframes the job. The question is no longer only "which model should we use?" but "what organisation should our agents form?" Who does what, who checks whom, what each one is allowed to touch, and where a human steps in.

The singularity was imagined as a titan. What is actually arriving looks more like a civilisation, messy, plural and argumentative. That is good news. We have thousands of years of practice building civilisations that work. We should use it.

## Sources

- Evans, Bratton and Agüera y Arcas, [Agentic AI and the next intelligence explosion](https://www.science.org/doi/10.1126/science.aeg1895), *Science*, March 2026 ([arXiv preprint](https://arxiv.org/abs/2603.20639))
- Blaise Agüera y Arcas, [What is Intelligence?](https://www.youtube.com/watch?v=KhSJuqDUJME), Long Now Foundation talk, September 2025
- Li et al., [Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents](https://www.alphaxiv.org/abs/2604.22452v1), April 2026
- Petter Holme, [Superintelligence, collective stupidity, and the AI agents of the future](https://petterhol.me/2026/03/20/superintelligence-collective-stupidity/), March 2026
