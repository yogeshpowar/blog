---
layout: posts
title: A Prompt Writes Code, a Process Ships It
tags: Agentic AI SDLC agents engineering
desc: TLDR. One prompt can generate a working app. Production needs more - guardrails, gates, humans who approve, and a record of every agent's work that you can watch live and audit later. That is what an agentic SDLC gives you.
---

> A single prompt can give you a signup and login app in minutes. It will
> even run. But nobody reviewed it, nobody tested it in a staging
> environment, nobody approved it for production, and a month from now
> nobody will be able to tell you why it was built the way it was. For a
> toy that is fine. For production it is not. Production quality needs a
> process - and with AI agents, that process has to be explicit.

Last year I wrote about [PROTO](https://yogeshpowar.github.io/blog/2025/09/13/PROTO.html),
a simple protocol for agentic coding: one agent, a `TODO.md`, a
`context.md`, and a human in the loop. It worked well for small things.

This post is about what came next. I took the same idea all the way to a
full **software development life cycle run by specialised agents**, and I
ran a pilot project through it - from the first requirement to a tagged
release in production.

The protocol is open source: [github.com/yogeshpowar/ai_sdlc](https://github.com/yogeshpowar/ai_sdlc).

## Why a prompt is not enough

Ask a model to "build signup and login" and you get code. Ask the
questions a production team would ask, and you get silence:

1. Does it do what was asked, every acceptance criterion of it?
2. Who reviewed it - and did the reviewer re-run the tests, or trust the author?
3. Was it tested in uat and stage, not just on the developer's machine?
4. Who approved the production deploy, and what exactly did they approve?
5. What did it cost?
6. If something breaks in six months, can anyone reconstruct who did what, and why?

None of these is about writing code. They are about **process**. Human
teams answer them with roles, reviews, environments, approvals and
history. Agents need the same - written down, so that every agent follows
it the same way every time.

## Not the first, and that's fine

Role-based agent teams for software are not new. [MetaGPT](https://github.com/FoundationAgents/MetaGPT)
(2023) gave agents the roles of product manager, architect, engineer and
QA, with standard procedures and written handoffs between them.
[ChatDev](https://github.com/OpenBMB/ChatDev) ran a virtual software
company through waterfall phases. The [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)
brought agile story files and analyst, PM, architect, dev and QA agents.
Spec-driven tools like GitHub's [Spec Kit](https://github.com/github/spec-kit)
and AWS's [Kiro](https://kiro.dev/) made the spec the source of truth for
agents. And most agent platforms now trace runs and track token costs.

These showed that agents can write software together. Most of them stop
when the code is written, or when a pull request is opened. ai_sdlc
focuses on what comes after that:

1. promotion through real environments (dev → uat → stage → prod), with a
   QA gate at each one and a rehearsed rollback,
2. human approvals that are committed, and pinned to the exact commit and
   binary being shipped,
3. an audit trail that lives in the repo, as plain text in git, with no
   platform needed,
4. a live view that a human can actually watch,
5. and a vendor-neutral protocol, not a product. It works with any agent
   runner that can read and write files.

It is one practitioner's protocol, tested on one pilot. Read what follows
as a field report, not a breakthrough.

## What ai_sdlc is

It is a protocol plus a template, not a platform. You run
`sdlc-init` in a repo, and it creates a `.sdlc/` folder that the agents
use as their shared workspace. The ideas behind it:

1. **One agent per role, each with its own context.** BD, PRD, data, API
   design, UX, UI, schema, backend, frontend, docs, reviewer, security, QA,
   DevOps, release, monitor - and an Orchestrator that runs the show but
   never writes product code.
2. **Files are the only shared memory.** Agents don't remember each
   other. They hand off through written specs, review reports and messages.
   If it isn't written down, the next agent can't see it.
3. **Every stage has a gate.** Work moves forward only when the exit
   criteria pass. QA gates every environment: dev, then uat, then stage,
   then prod.
4. **Least privilege.** QA cannot edit code. Developers cannot deploy. Only
   DevOps promotes, and only what a human has approved.
5. **Humans approve the irreversible**, and the approval is committed the
   moment it is made, pinned to the exact commit being shipped.
6. **Thin slices, not big bangs.** Small, functionally complete items go
   all the way to prod, and the human steers after every release.
7. **The project outlives the agents.** Architecture, API contract, ADRs
   and runbook live in the project's own `docs/`, for every future
   developer. `.sdlc/` is only the record of how the work was done.

## The pilot

The pilot project is a small web app: sign up, sign in, see a landing
page, sign out. It has a Go backend, plain HTML/CSS/JS, accounts stored as
files, and four environments (dev, uat, stage, prod) running side by side
on one machine. It is a toy, but it was built the way you would build a
real product.

From the first requirement to `v0.1.0` in production:

| | |
|---|---|
| Agent runs | 37, across 17 roles |
| Handoff messages for the main feature | 51 |
| Commits | 65, of which 61 name the agent run that made them |
| Code | about 5,100 lines of Go, 114 tests, 82.8 to 100% coverage per package |
| Acceptance criteria | 19 of 19 passing in dev, in uat and in stage |
| Project docs | architecture, API contract (OpenAPI), data model, 4 ADRs, security, runbook, glossary |
| Human decisions | 2 (sign off the spec, approve the prod deploy) |
| Wall clock | about five and a half hours, including a pause to upgrade the protocol mid-flight |
| Tokens | a little over 3 million (estimated - more on that below) |

The interesting part is not the numbers. It is what the process caught.

## What the guardrails caught

**The reviewer didn't trust the author.** It re-ran every gate itself -
build, vet, tests, coverage, a vulnerability scan - started the binary,
and probed it live. It mapped every one of the 19 acceptance criteria to
the code and to a named test. Then it **rejected** the first round anyway,
because the README and CONTRIBUTING still described an older version of
the API. Code and docs disagreeing is exactly the kind of drift a single
prompt never notices.

**The design was corrected before the code shipped.** The API contract and
the implementation had drifted apart in six places. Instead of quietly
"fixing" one side, the item went back to design, and a version 2 of the
contract was written to match reality and reviewed.

**Security found a real bug.** The security agent noticed that a request
path was written to the log unescaped. A percent-encoded newline could
forge log lines. It was a low-severity finding, but it was fixed, with a
test, before release.

**A crash lost nothing.** One run died halfway through on an API usage
limit. On its next start, the Orchestrator found the uncommitted work,
saved it as a `wip(...)` commit with a note saying where it came from,
marked the run as timed out, and started a retry that finished the job.

**An agent asked instead of guessing.** Before production, DevOps
noticed two rules that contradicted each other: deploy only tagged
commits, but tag only after the deploy passes its smoke test. It did not
pick one. It put the question in front of me, with a recommendation, inside
the approval request. My answer became part of the approval record:

```yaml
type: approval
decision: approved
by: human:yogesh
approves:
  commit: 9aa7c6b05a7e3649ae4cd842177337094935525f
  sha256: 15c9284a91031676673277d02a1141089449c9e865dc3ce2157860ee8c9b81f1
  target: prod
```

That approval covers that commit and that binary, nothing else. If anything
had changed after I approved, the agents would have had to ask again.

**Mistakes were written down so they don't repeat.** Three lessons went
into `lessons.md`, which every agent reads before starting - for example,
"when a contract version changes, search the docs for claims that depended
on the old one".

## Watching it, live

Agents can work for a long time. Staring at a silent terminal is not
oversight. So the protocol includes a live view:

```
 toy_first_ai_sdlc: SDLC status · 🟢 2 agents working · now on FEAT-0001 (PROD) · tokens 3.4M
 uat: 9aa7c6b · stage: 9aa7c6b · prod: 9aa7c6b
 LIVE                                      │ ACCOUNTS
 - ⏳ monitor on FEAT-0001 · 10m58s 56% ·  │ * [p] (p0) Signup and login @monitor stage:prod
   Watching prod: healthz 200, login 200,  │     * [X] design r1: Write PRD @prd tok:39.0k
   5xx new=0                               │     * [X] design r1: Architecture, API contract
 - ⏳ orchestrator · Waiting for the human  │       and ADRs @data-flow took:5m18s tok:86.0k
   to approve … ⚠ quiet for 20m47s         │     * …
 RECENT                                    │ PLATFORM
 - 03:56:38 ✅ ui completed · FEAT-0002    │ * [o] (p1) Env shown in footer stage:design
 - 03:53:08 ▶ prd spawned · FEAT-0002 ·    │     - DESIGN→DEV PASS; waiting for WIP slot
   Write S story: footer shows the env name│ * [O] (p0) Protocol 1.4 migration stage:qa
 - 03:52:26 ▶ monitor spawned · FEAT-0001  │     * [f] dev r1 … API usage limit (HTTP 429)
```

That is a real snapshot from the pilot, a few minutes after the release.
Monitor is watching prod. The next slice is already in design, but it is
waiting for a free slot, because only one item may be in flight at a time.
Even the run that died on a usage limit is still there, marked `[f]`. And the
Orchestrator is flagged as quiet, because it is waiting for me.

On the left is what is happening right now. On the right is the whole
board, in the plain-text [TODO.MD](https://github.com/doublefreein/TODO.MD)
format, which you can scroll. Every agent posts a heartbeat in plain words -
"watching prod: healthz 200, login 200" - so you always know what it is
doing.

## Auditing it, later

This is the part I value most. Every agent run gets an ID, a parent, a
start, an end, an outcome and a token count. Every commit carries the
run and item that made it. Every human decision is a committed file. So
questions that are usually hard become one-liners:

```sh
git log --grep "Approved-By"          # every decision a human made (since protocol 1.3)
git log --grep "Item: FEAT-0001"      # everything done for one feature
grep RUN-…-qa-… .sdlc/trace/runs.jsonl  # what one agent did, when, at what cost
```

The present (what is running now), the recent past (the last few runs) and
the whole history (every handoff, review, rejection and approval) are all
in the repo, in plain text, versioned with the code.

## What didn't go well

A pilot that only reports successes isn't worth much. Here is what didn't work:

1. **We skipped the walking skeleton.** The protocol says the first item
   should be a "hello world" deployed all the way to prod, to prove the
   pipeline. The first item was a full signup and login feature instead. The
   pipeline was only proven at the very end, on the most expensive item.
2. **The items were too big.** The main feature had 19 acceptance criteria.
   The protocol's limit for a medium item is 5. It cost almost three times
   its budget, and about a fifth of all tokens went to rework. With smaller
   slices, both the cost and the rework would have dropped.
3. **Token counts were estimates.** The agents could not see their real
   usage, so nearly every count is an estimate, corrected afterwards. That
   is a gap in tooling, not in the idea: the next step is a thin harness
   that records real counts automatically, instead of trusting each agent to
   report them.
4. **The process itself changed mid-project.** I upgraded the protocol from
   1.2.1 to 1.4 while the pilot was running. An upgrade tool merged the new
   rules in without touching code, history or approvals - but it shows the
   process is still young.

## Prompt vs process

| | One prompt | Agentic SDLC |
|---|---|---|
| Speed to first code | minutes | hours |
| Matches every requirement | maybe | each AC mapped to a test, checked in three environments |
| Review | none | an independent reviewer that re-runs everything |
| Security | luck | a dedicated agent with the power to block |
| Production | "it runs on my machine" | deployed only what a human approved, pinned to a commit |
| Visibility | a scrolling terminal | live view of every agent |
| Audit | none | every run, decision and handoff, versioned in git |
| Docs for the next developer | whatever is left | architecture, contract and runbook kept in sync |

Yes, the process costs more. Several million tokens and a few hours for a
toy app is not cheap. But most of that cost buys **evidence**: reviews, test
reports, approvals and a history you can trust. For a hackathon, one prompt
is enough. For anything that real users depend on, the evidence is the
product.

## Try it

```sh
git clone https://github.com/yogeshpowar/ai_sdlc.git
export AI_SDLC="$PWD/ai_sdlc"; export PATH="$AI_SDLC/bin:$PATH"
mkdir my-app && cd my-app && git init && sdlc-init . my-app
```

Write a short brief, start the Orchestrator, and open `sdlc-watch` in a
second terminal. The [GUIDE](https://github.com/yogeshpowar/ai_sdlc/blob/main/GUIDE.md)
walks through the rest. It is GPL-3.0, and it works with any agent runner
that can read and write files, run commands and start sub-agents.

AI makes writing code cheap. It does not make engineering cheap. The
discipline that turns code into a product - specs, reviews, environments,
approvals, history - still matters. With agents, it simply has to be
written down.
