## 8. What Not to Build

When building was slow, the cost of building acted as a filter. A weak idea
often died in planning because nobody could justify the weeks it would
take. That filter was crude, and it killed good ideas too, but it did work.
With agents, the filter is gone. A weak idea can be built in a day, and
once it is built, it has a constituency: someone worked on it, a demo
exists, and throwing it away feels like waste.

This is why I have come to believe that the most valuable decision a team makes is often **what not to build**. It is also the decision agents
help with least, because an agent asked to build something will build it.

The difficulty is that most ideas look right. In my experience, if a team
lists ten things it could build next, all ten will look sensible, have a plausible customer, and fit the roadmap. In my experience, nine of them work out. *Nine of ten things look right. The tenth quietly fails and
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
can be asked before anything is built. Who exactly is this for, and how do we know they want it? Who else has to say yes, and have they? Which rules apply, and has the person accountable for them seen it? What does it cost to run for a year, not to build for a week?

Agents can help with all four. An agent can draft the market research,
find the relevant rules, list the partners and integrations involved, and
estimate the components the idea would add to the platform. It can also
be asked to argue against the idea: to write the strongest case for not
building it. I find that more useful than asking it to agree with me.
What the agent cannot do is make the call. The decision to stop is still a human one, and it is often the most important decision of the quarter.

Two habits help that decision get made. The first is to build the
smallest thing that answers the question, not the smallest version of
the product. If the question is whether customers want it, the smallest
thing may be a page that describes it, not the feature itself. The second
is to decide, before building, what result would make you stop. A kill
criterion written into the map at the start is much easier to honour than
one invented after a month of work. As chapter 1 said, failure is cheap in
time, but a failed idea that is quietly kept is not cheap at all.

Every feature built is also a feature to run. It has to be secured,
monitored, patched, explained to support, covered in audits, and kept
compatible with everything built after it. That cost does not shrink when
the building gets faster. It grows, because more gets built. Cheap building makes expensive ownership easier to start. Over-building is not
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
works for. People want to see that what they built mattered. A product
nobody uses wastes more than the effort that went into it. It drains the
energy for the next one.

Today, the first artefact for anything new is the map, not the code, and
compliance and the people accountable for risk see that map before an
agent writes a line meant to ship. A prototype to learn from can come
earlier, but it is never the thing that ships.

Deciding not to build is one way to control cost. The other is to be
honest about the costs that remain once something is built.

<!-- REVIEW NOTES (remove before publishing)
1. Compliance story (hard rule 1): the old draft said "the product, as
   designed, could not be offered under the rules that applied to it".
   That was my inference, not your words. It is now an [ADD] with that
   sentence as an example. The story still needs: state of the work,
   reason for the block, and optional aftermath. "Would have cost an
   afternoon" became "far less than a month", which is less specific.
2. Deeper thought, new: "you cannot tell which one is the tenth by looking
   at it", so the defence is cheap, early tests of the four outside
   failures (customer, partner, rule, running cost). Each failure now has
   a matching question. This gives the nine-of-ten idea a practical answer.
   Does it match how you think about it?
3. New: ask the agent to argue against the idea. "I find that more useful
   than asking it to agree with me" is written as your experience. Confirm
   or cut.
4. New: two habits, "smallest thing that answers the question" and a kill
   criterion in the map. Links back to chapter 1 ("a failed idea that is
   quietly kept"). Suggestion or your practice?
5. Two whole bold sentences now bold only the key phrase, or use italics.
   The "every feature built is also a feature to run" paragraph moved after
   the habits, so it leads into the story.
6. The reason for the block is confidential (your answer, 2026-10-31). The
   text now says so. Check the next sentence, which is my inference: "The
   problem was not in the code, and better engineering would not have fixed
   it." The rest of the lesson depends on it. If it is not true, or you
   cannot say, I will rewrite the lesson.
7. New (your answers, 2026-10-31): a second story. An internal product
   built to the highest quality for another vertical was not used, and the
   team lost motivation. A team building business-to-consumer products felt
   the win. Money is necessary but not enough. My wording: "There is a
   second cost, and it falls on people", "People want to see that what they
   built mattered", and "It drains the energy for the next one". The
   last one is an inference, so confirm or cut it.
8. Changed 2026-11-01 (review finding 3): "before an agent writes a line"
   became "before an agent writes a line meant to ship", plus "A prototype
   to learn from can come earlier, but it is never the thing that ships."
   You confirmed the original sentence, so check this still matches your
   practice.
9. Emphasis pass 2026-11-01 (review findings 7 and 15): one italic line
   kept, your "Nine of ten things look right. The tenth quietly fails and
   steals the show." Its setup no longer contradicts it: "all ten will look
   sensible ... In my experience, nine of them work out." Bold narrowed to
   "what not to build" and "a fast build of the wrong thing".
-->
