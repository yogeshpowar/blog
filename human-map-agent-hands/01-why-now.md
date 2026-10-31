---
layout: chapter
title: "1. Why Now: Building Is Fast and Failure Is Cheap"
desc: "Human Map, Agent Hands · Chapter 1 of 13"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 1
permalink: /human-map-agent-hands/01-why-now/
image: /images/human-map-agent-hands-cover.jpg
---

I began my career in embedded systems, writing Linux drivers and Wi-Fi
firmware. There, failure was very hard. The systems had very strong quality
checks in place, and a small change used to take months to ship to the
chip. Nobody tried an idea casually, because every idea had to survive that
whole path.

Later I became a co-founder and, for a while, the only developer. In that
phase the expensive part of software was easy to name: my own hours. I held
the whole system in my head, so decisions were instant and nothing waited
for a handoff. But there was only so much one person could build, test, and
run.

The team grew slowly, and the expensive part moved. Specialists brought
depth. Then came the structure a regulated business needs: leads, reviews,
security, compliance. I have written about that journey before, in [From
One-Person Engine to Multi-Layered
Machine]({{ site.baseurl }}{% post_url 2026-05-06-Solo-to-multi-layerd-machine %}).
Every layer was there for a good reason, and every layer added distance
between an idea and a customer. An idea now had to wait for a sprint, then
for the right people, then for a review, then for a release window. By the
time it reached a customer, it had already cost weeks of people's time, and
that cost shaped every conversation about it. We argued about ideas
carefully because building them was slow and throwing them away was
painful.

That is no longer how it feels to me. My own example is small, but it
changed how I think. I have worked mostly on backend systems, a little on
the web frontend, and almost never on app development. We found a
performance problem in the CAPTCHA check that keeps bots from disturbing
our system. The core fix was not the hard part. The complexity was backward
compatibility: older clients still in use, and web and mobile clients on
different versions of the CAPTCHA, some through the web integration and
some through mobile SDKs. The team knew how to fix it, but nobody had the
time to build it. With a coding agent, I could work through that
compatibility in the backend and the frontend myself, test the logic, and
build the feature. It then went to
production through our standard development process, like any other
change. Without an agent, I could not have done it. **The first working
version arrives much sooner**, and it can come from someone who would not
have built it at all before. That changes the shape of every decision that
comes after it.

I do not want to overstate this, because the careful studies are less
flattering than the headlines. In a [randomised trial published by METR in
July 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
experienced open source developers working in their own large repositories
took *19% longer* to finish tasks with AI tools than without them, while
believing afterwards that the tools had made them about 20% faster. When
METR [tried to repeat the study in early 2026](https://metr.org/blog/2026-02-24-uplift-update/),
it found some evidence of speedup but called its own estimate unreliable,
partly because many developers no longer wanted to work without AI at all.
I take two things from this. First, *feeling faster and being faster are
not the same*, and I should be suspicious of my own impressions. Second,
those studies measured experts finishing tasks in code they knew deeply.
My example was the opposite: work outside my usual area, on a fix the team
already understood, which would otherwise have waited. That is where I see
the biggest change. Not in making experts faster at what they already do,
but in how far a person can reach, and how quickly a team can get from an
idea to a first version it can test. The reach is only safe because the
change still went through the same process as everything else.

The second change is quieter. **Failure has become cheap in time.** In
firmware, a change that turned out to be wrong could cost months. Even in
web software, when a prototype took a month, a failed prototype was a lost
month, and teams protected themselves by not trying. When a prototype takes a day, a failed
one is a lost day. It is still a loss, but it no longer has to be defended
in a meeting. A team can try three approaches and keep the one that
survives contact with real data. Notice the words *in time*, though.
Failure is cheaper in hours. It is not cheaper in attention, in trust, or
in what it costs when a failed idea is quietly kept instead of thrown away.
I will come back to that.

The third change is that the challenges are more open. The landscape moves
every few months. Models improve, tools appear and disappear, and practices
that were sensible last year now look slow. A question like "how should a
team of ten ship software?" used to have settled answers. Today it has
several reasonable answers and no consensus. Problems that once needed a
large team are now within reach of a small one. That is why we introduced
pods: small teams of a couple of developers, a product manager, and a QA
engineer, each owning a problem end to end. I find that
exciting, and I also find it unsettling, because **a world where anything
can be built quickly is not a world where everything should be**.

This is the part that is easy to miss. Agents make building cheap. They do
not make everything else cheap. A feature built in a day still has to be
run, secured, audited, patched, explained to support, and sold to someone
who needs it. In a regulated business such as fintech, each of those steps
has rules, and each rule has someone who is accountable for it. Finding
customers is as slow and uncertain as it ever was. **The cost of building
has fallen. The cost of owning has not.** I made the same point from the
engineer's side in [AI made coding cheap. Engineering judgment is what is
left.]({{ site.baseurl }}{% post_url 2026-08-17-AI-Engineering-Judgment %})

In a way, agents bring back something of the solo phase. One person, or a
small team, can again go from an idea to working code without waiting on
anyone. What they do not bring back is the simplicity of that phase. The
security reviews, the compliance checks, and the audit trail did not appear
because typing was slow. They appeared because of what is at stake, and
*they are still needed when the typing is done by an agent*.

That gap is what this essay is about. It is written from my experience: in
firmware, then as the only developer at a startup, and now as the CTO of a
fintech platform, where
a mistake is not an awkward bug report but a question about someone's
money. My claims are my experience, not
universal truths. I will try to be honest about where agents have helped
me, where they have not, and where I am still unsure.

The argument, in short, is this. Speed without evidence, control, and
accountability creates risk. The answer is not to refuse the speed, and it
is not to hand everything to agents. It is a deliberate mix: *humans hold
the map*, which means the intent, the boundaries, the risk classes, and the
approvals, and *agents do the hands-on work*, which means the code, the
tests, the environments, and the analysis. How much autonomy the agents get
should depend on what a failure would cost. And in a world where building
is easy, **the most valuable decision a team makes is often what not to
build**.

Before I get to the mix, it helps to look at how teams are actually
responding today.
