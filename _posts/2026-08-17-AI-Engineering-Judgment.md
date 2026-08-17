---
layout: posts
title: "AI made coding cheap. Engineering judgment is what is left."
tags: AI engineering software
desc: TLDR. AI has made implementation cheap. It has not made software cheap to run, secure, or own.
---

> AI has made implementation cheap. It has not made software cheap to run,
> secure, or own. Teams that only translate tickets into code are funding a
> skill that is being automated. The work that lasts is engineering: name
> the metric, make the tradeoff explicit (cost, scale, reliability, speed),
> and treat security and privacy as design inputs. That bar applies to app,
> web, backend, data, DevOps, and testing. AI can draft the work. A person
> still owns the bill, the outage, and the leak. If nobody can defend the
> design after the model is gone, we did not engineer it - we generated it.

AI is the reason this is happening now. It is collapsing the market value of
"I can write the code." Implementation that used to take a week can be
drafted in minutes. That makes the first draft cheap - and it makes unowned
software more dangerous. If we keep paying people to translate tickets into
code, we will be funding a skill that is being automated. The durable work
is engineering: owning outcomes, not producing files. Judge teams on that,
not on story points.

An engineer does not stop at "it works" or "the model generated it." They
answer three questions before the work is done:

**Metric** - What number in production proves this is better? Latency,
error rate, conversion, cost per request, time to recover. If there is no
metric, there is no outcome - only activity.

**Tradeoff** - What did we give up? Cost vs scale, reliability vs speed,
simplicity vs flexibility. AI will optimise whatever you forgot to
constrain. That is how you get a fast system you cannot afford, or a cheap
system that fails at 2x traffic.

**Security and privacy** - What data do we store, who can see it, how do we
fail, and what are we willing to send to a model? These are design
decisions. Treating them as a late review is how incidents get scheduled.

That standard applies across the stack.

### App (mobile)

AI can scaffold screens. It cannot own crash-free sessions, cold start,
battery, binary size, or behaviour on a weak network. Every SDK, permission,
and background job has a cost - including AI features that send user
context off-device. If we cannot say what we collect, what we cache, what we
send to a model, and why, we are not shipping a product. We are shipping a
privacy incident with a UI.

### Web

A page that looks finished is not a result. Core Web Vitals, bundle size,
cache hit rate, and accessibility are the result. XSS, CSRF, cookies, and
third-party scripts are design constraints, not QA leftovers. Generated
markup does not get a waiver. If AI wrote it, the team still owns the leaked
token and the 400kb of unused JavaScript that we pay for on every session.

### Backend

A 200 response is the starting line. p95/p99 latency, throughput,
idempotency, retries, and blast radius are the job. So is unit cost: CPU,
memory, database, egress, and now tokens. A generated endpoint that "works"
and is reachable without real authz is not velocity. It is an open door with
a merge timestamp. Secrets and least privilege belong in the design, not in
the ticket after launch.

### Data

A query that returns is not a pipeline. Freshness, completeness, and
accuracy are SLAs. Warehouse cost vs query speed, batch vs stream, and
field-level access are tradeoffs you will feel on the bill and in the board
pack. PII, retention, and lineage are product decisions. Putting sensitive
data into a model without purpose, retention, and access control is not an
experiment. It is a privacy failure. A wrong number at scale is worse than
no number. An AI-confident wrong number is how bad decisions get funded.

### DevOps / platform

Pipelines and clusters are products. Deploy frequency, lead time,
change-fail rate, and MTTR are the metrics. Idle capacity has a cost.
Outages have a larger one. Generated Terraform that is slightly wrong is
still production. If the person who merged it cannot explain what happens
when it fails - secrets, network path, blast radius - they are not
operating the system. They are hoping. Hope is not a reliability strategy.

### Testing / QA

Finding bugs is useful. Buying confidence is the job - especially when more
code is machine-generated and looks plausible. Coverage percentage is not a
strategy. Risk and cost of failure are. AI will generate tests that encode
the same wrong assumption as the code. That is not quality. The scarce skill
is knowing what not to trust: authz gaps, data leaks, insecure defaults,
prompt or data exfiltration. If QA only checks the happy path of generated
features, we are paying for theatre.

### What this means for how we run the work

AI speeds up the first draft. It does not remove the need for someone who
can say yes or no with a reason - and who is still there when it breaks.

The operating bar, for every role, is the same three questions above,
enforced before the fact rather than asked after:

**No metric, no build.** Define "good" in production before the first
accepted line of generated code.

**No implicit tradeoffs.** Write down cost, scale, reliability, and speed.
You cannot maximise all four - if the tradeoff is unspoken, AI will pick one
for you, and you will pay for it later.

**Security and privacy are inputs**, not a gate at the end.

The old habit still closes tickets: take the story, generate the code, move
on. That habit has no durable role. Implementation is being automated.
Accountability is not. Teams that only produce code will look busy and
become replaceable. Teams that can defend a design with numbers, failure
modes, and a clear "what we gave up" will use AI as leverage.

The question for every design review is no longer "did we write it?" It is
"would we still own this if the model disappeared tomorrow?"

If the answer is no, we did not engineer it. We generated it. That is the
gap we have to close - on purpose, while we still have the choice.
