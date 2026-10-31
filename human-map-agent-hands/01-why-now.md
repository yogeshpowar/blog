---
layout: chapter
title: "1. Why Now: Building Is Fast and Failure Is Cheap"
desc: "Human Map, Agent Hands · Chapter 1 of 11"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 1
permalink: /human-map-agent-hands/01-why-now/
image: /images/human-map-agent-hands-cover.jpg
---

A while ago we found a performance problem in the CAPTCHA check that keeps
bots from disturbing our system. The core fix was not hard. The complexity
was backward compatibility: older clients still in use, and web and mobile
clients on different versions of the CAPTCHA, some through the web
integration and some through mobile SDKs. The team knew how to fix it, but
nobody had the time to build it. I have worked mostly on backend systems, a
little on the web frontend, and almost never on app development. With a
coding agent, I could work through that compatibility in the backend and
the frontend myself, test the logic, and build the feature. It went to
production through our standard development process, like any other
change. Without an agent, I could not have done it.

That small fix changed how I think about **reach**. The first working
version now arrives much sooner, and it can come from someone who would not
have built it at all before. The reach is only safe because the change
still went through the same process as everything else.

I have seen the other side of this cost too. I began my career in embedded
systems, writing Linux drivers and Wi-Fi firmware, where a small change
could take months to reach the chip. Later I became a co-founder and, for a
while, the only developer, and then grew a team slowly, adding the
specialists and the structure a regulated business needs. I have written
about that journey in [From One-Person Engine to Multi-Layered
Machine]({{ site.baseurl }}{% post_url 2026-05-06-Solo-to-multi-layerd-machine %}).
At every stage, building was the expensive part, and the cost of building
shaped every argument about what to build.

I do not want to overstate the change, because the evidence is weak in
every direction, mine included. In a [randomised trial published by METR in
July 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
experienced open source developers took 19% longer to finish tasks in
their own repositories with AI tools than without, while believing the
tools had made them about 20% faster. When METR [tried to repeat the study
in early 2026](https://metr.org/blog/2026-02-24-uplift-update/), it found
some evidence of speedup but called its own estimate unreliable. Feeling
faster and being faster are not the same, and I treat my own impressions
with the same caution. What I can say is narrower: those studies measured
experts in code they knew deeply, and the biggest change I see is not
there. It is in how far a person can reach.

The second change is quieter. **Failure has become cheap in time.** When a
prototype took a month, a failed prototype was a lost month, and teams
protected themselves by not trying. When a prototype takes a day, a failed
one is a lost day, and a team can try three approaches and keep the one
that survives contact with real data. But failure is cheaper only in
hours. It is not cheaper in attention, in trust, or in what it costs when
a failed idea is quietly kept instead of thrown away.

That is the part that is easy to miss. Agents make building cheap. They do
not make owning cheap. A feature built in a day still has to be run,
secured, audited, patched, and explained to support, and in a regulated
business each of those steps has rules and a person accountable for them.
Nor do agents make customers easier to find. Someone still has to want what
was built, and that is as slow and uncertain as it ever was. The cost of
building has fallen; **the cost of owning has not**. A world where anything
can be built quickly is not a world where everything should be.

In a way, agents bring back the speed of the solo phase. One person, or a
small team, can again go from an idea to working code without waiting on
anyone. What they do not bring back is its simplicity. The security
reviews, the compliance checks, and the audit trail did not appear because
typing was slow. They appeared because of what is at stake, and they are
still needed when an agent does the typing.

I made the first half of this argument, from the engineer's side, in [AI
made coding cheap. Engineering judgment is what is
left.]({{ site.baseurl }}{% post_url 2026-08-17-AI-Engineering-Judgment %})
This essay is about what a team does with it, especially a team that
answers to regulators. My answer has two parts. The operational answer is a
deliberate mix: humans hold the map, meaning the intent, the boundaries,
the risk classes, and the approvals, and agents do the hands-on work,
meaning the code, the tests, the environments, and the analysis, with
autonomy set by what a failure would cost. The strategic answer is that
when building is cheap, the most valuable decision is often what not to
build. [Chapters 2]({{ '/human-map-agent-hands/02-three-kinds-of-teams/' | relative_url }}) to 7 are about the first. Chapters [8]({{ '/human-map-agent-hands/08-what-not-to-build/' | relative_url }}) and [9]({{ '/human-map-agent-hands/09-costs-nobody-budgets/' | relative_url }}) are about
the second. Everything here is my experience as the CTO of a fintech
platform, not a universal rule.
