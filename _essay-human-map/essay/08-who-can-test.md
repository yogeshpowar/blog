## 8. Who Can Test the Whole Path Now

As a team grows, testing the whole path from a customer's screen to the
database and back tends to become a specialist job. It needed a working
staging environment, test accounts, knowledge of which services to start,
and often one particular engineer who knew the tricks. Everyone else tested
their own piece and trusted that the pieces fitted.

That is changing, and I think it is one of the most underrated effects of
agents. When the environment starts with one command, when observability
is local, and when an agent can explain what it sees in plain language,
**end-to-end testing stops being a specialist job**. A product manager can
walk through a new journey on a local build. A designer can check that an
error message actually appears when a payment is declined. A support lead
can reproduce a customer complaint and attach a trace instead of a
screenshot. It extends an old habit I have recommended to teams: [buy one
unit of what you sell]({{ site.baseurl }}{% post_url 2023-12-11-MondayMotivationTech %}),
so that you become a user of your own platform and notice what users
notice.

This fits the shape of our pods, each with a couple of developers, a
product manager, and a QA engineer. With a local environment and an agent,
the product manager and the QA engineer could check the whole path
themselves, instead of waiting for an engineer to set it up for them. *The
people who define a journey and the people who check it would no longer
depend on the people who build it to see it working.*

[DIAGRAM: diagrams/08-checkout-trace.mmd]

Consider a generic example. A customer reports that the final step of a
checkout feels slow on their phone. In the old way, this becomes a ticket,
waits for an engineer, and starts with "cannot reproduce". In the new way,
anyone on the team can start the system, locally or on a shared test
environment, walk through the same screens, and ask an agent to show the request timeline: from the client,
through the API gateway, into the service, down to the database. The slow
step is visible on the timeline. The person who found it may not know how
to fix it, but they can hand over a precise description of where the time
goes. That is a far better starting point for an engineer, or for an
agent.

We are not fully there. In our teams, the code is still managed by
developers and a few product managers. QA engineers do not yet have
working local setups; they test on shared servers such as UAT, staging, and
sometimes production. But anyone can discover an issue and record it in the
issue tracker, and the curious ones go further. They switch into analysis
mode and add the extra information that a developer, and the developer's
agents, can work from. *Discovery is already shared; the local setup is
not yet.* Giving everyone in a pod the same local setup the developers have
is the obvious next step.

This matters for three reasons. First, *the people closest to the customer
can check the customer's experience themselves*, instead of describing it
second-hand. Second, it puts more eyes on agent-built work, from more
angles. An engineer reviewing a diff sees the code. A product manager
walking through a journey sees whether the code does what the customer
needed. Both views are needed, and the second is the one most often
missing. Third, it spreads understanding of the system across the team.
People who can run and observe the whole system ask better questions about
it.

There is a fourth benefit that connects back to the guardrails. When
someone outside engineering finds a problem this way, the path they walked
can become an end-to-end test. The agent can turn "I tapped Pay and waited
too long" into a repeatable test with a time limit, so the same problem
cannot quietly return. *Every journey someone checks by hand is a test
waiting to be written*, and agents make writing it cheap.

There are cautions. Easy access to environments must not mean easy access
to real customer data. Local and shared test environments should use
synthetic or properly masked data, and that rule has to be enforced by the
system, not assumed. And a non-engineer finding a problem is not the same
as a non-engineer approving a fix, and checking a path is not the same as
building outside one's domain. Agents make that tempting too, which is the
trap I described in [The Hidden Trap of AI
Tools]({{ site.baseurl }}{% post_url 2025-09-18-AI-Trap %}). Testing can be
widely shared;
**accountability for releasing still sits with the people named in the
map**.

This wider testing also produces a record: who tried what, what they saw,
and what changed as a result. In a regulated business, that record has a
value of its own.

<!-- REVIEW NOTES (remove before publishing)
1. Experience claim: "In most teams I have worked with, testing the whole
   path ... was a specialist job." Confirm.
2. New: a fourth benefit, that a hand-checked journey becomes an end-to-end
   test. It links back to chapter 7. Deeper thought: does this happen on
   your teams, or is it a suggestion?
3. The bold sentence "Testing can be widely shared; accountability ..." was
   a whole bold sentence. Now only the accountability phrase is bold.
4. Diagram: diagrams/08-checkout-trace.mmd is a sequence diagram. Mermaid
   cannot draw a phone screen, so a "Phone checkout screen" participant
   stands in for it.
5. Corrected (your answer, 2026-10-31): QAs do not have local setups yet;
   they test on UAT, staging, and sometimes production. Code is managed by
   developers and a few PMs. Anyone can log issues; curious people go into
   analysis mode. The pods paragraph now says "could" and "would", and a
   new "We are not fully there" paragraph describes what actually happens.
   The checkout example now says "locally or on a shared test environment".
   My wording: "Discovery is already shared; the local setup is not yet"
   and "Giving everyone in a pod the same local setup ... is the obvious
   next step". The second one implies a plan, so confirm or cut it.
-->
