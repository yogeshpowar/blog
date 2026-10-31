---
layout: chapter
title: "10. What Not to Build"
desc: "Human Map, Agent Hands · Chapter 10 of 13"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 10
permalink: /human-map-agent-hands/10-what-not-to-build/
---

When building was slow, the cost of building acted as a filter. A weak idea
often died in planning because nobody could justify the weeks it would
take. That filter was crude, and it killed good ideas too, but it did work.
With agents, the filter is gone. A weak idea can be built in a day, and
once it is built, it has a constituency: someone worked on it, a demo
exists, and throwing it away feels like waste.

This is why I have come to believe that **the most valuable decision a
team makes is often what not to build**. It is also the decision agents
help with least, because an agent asked to build something will build it.

The difficulty is that most ideas look right. In my experience, if a team
lists ten things it could build next, nine of them will look sensible, have
a plausible customer, and fit the roadmap. The tenth will look just as
sensible. *Nine of ten things look right. The tenth quietly fails and
steals the show.* It fails not because the code is bad but because
something outside the code was wrong. The customers were not there in the
numbers assumed. A partner would not integrate. A rule forbade it. Or the
cost of running it was larger than the value it created. And because it
fails quietly, after the building is done, it takes attention, people, and
trust from the nine that were working. Agents make this worse in a
particular way, which I called the prototype illusion in [The Hidden Trap
of AI Tools]({{ site.baseurl }}{% post_url 2025-09-18-AI-Trap %}): work
that looks finished long before it is.

The hard part is that you cannot tell which one is the tenth by looking at
it. From the inside, it looks like the other nine. That is why the defence
is not better judgement in the abstract, but cheap, early tests of the
things outside the code. Each of those four failures has a question that
can be asked before anything is built. *Who exactly is this for, and how do
we know they want it?* *Who else has to say yes, and have they?* *Which
rules apply, and has the person accountable for them seen it?* *What does
it cost to run for a year, not to build for a week?*

Agents can help with all four. An agent can draft the market research,
find the relevant rules, list the partners and integrations involved, and
estimate the components the idea would add to the platform. It can also
be asked to argue against the idea: to write the strongest case for not
building it. I find that more useful than asking it to agree with me.
What the agent cannot do is make the call. **The decision to stop is still
a human one**, and it is often the most important decision of the quarter.

Two habits help that decision get made. The first is to build the
*smallest thing that answers the question*, not the smallest version of
the product. If the question is whether customers want it, the smallest
thing may be a page that describes it, not the feature itself. The second
is to decide, before building, what result would make you stop. A kill
criterion written into the map at the start is much easier to honour than
one invented after a month of work. As [chapter 1]({{ '/human-map-agent-hands/01-why-now/' | relative_url }}) said, failure is cheap in
time, but a failed idea that is quietly kept is not cheap at all.

Every feature built is also a feature to run. It has to be secured,
monitored, patched, explained to support, covered in audits, and kept
compatible with everything built after it. That cost does not shrink when
the building gets faster. It grows, because more gets built. *Cheap
building makes expensive ownership easier to start.* Over-building is not
new. In [Microservice
Hell]({{ site.baseurl }}{% post_url 2025-05-25-microservice %}) I argued
that a system should be split by actual execution demand, not speculative
scalability. Agents make that kind of speculation cheaper to start, and no
cheaper to run.

One experience made this real for me. A team spent about a month building
a new product. It was ready for production with a closed user group, the
small, invited set of customers a new product often launches to first.
Then it reached a compliance review, and it was blocked. The reasons are confidential, so I will not go into them here. The problem was not in the code, and better engineering would
not have fixed it.

Looking back, the lesson was not that the team built badly. It was that
they built first. A conversation with compliance at the start, with a
single page describing the intent and asking "can we offer this?", would
have cost far less than a month. With agents, that month of building might
shrink to a week, but **a fast build of the wrong thing** is still the
wrong thing. Speed makes this mistake cheaper. It does not make it go
away. In some ways it makes it more likely, because there is less friction
to make anyone stop and ask.

There is a second cost, and it falls on people. A team was building a
product for another vertical in the company, to the highest quality. It
took real effort and push, and people gave more than everything they had
to meet the deadline. The product was ready, and it launched. Then the
other team did not use it. At the same time, another team was building for
customers directly, in business-to-consumer products, and could see people
using what it made. That team felt it was creating something of value. The
team that had built for an internal team, to improve productivity or to
help that team serve its own customers, never felt the win, and it lost
its motivation. Money is a necessity, but it is not the only thing a team
works for. *People want to see that what they built mattered.* A product
nobody uses wastes more than the effort that went into it. It drains the
energy for the next one.

Today, the first artefact for anything new is the map, not the code, and
compliance and the people accountable for risk see that map before an
agent writes a line.

Deciding not to build is one way to control cost. The other is to be
honest about the costs that remain once something is built.
