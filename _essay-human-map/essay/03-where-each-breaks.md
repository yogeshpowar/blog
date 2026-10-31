## 3. Where Each Kind of Team Breaks

Every way of working has a failure mode that its own members find hard to
see. The failure is rarely dramatic. It is a slow pressure that builds
until something gives. For each kind of team, it helps to know what that
pressure is, and what the early symptom looks like.

**The orthodox team breaks on opportunity cost.** It rarely ships a
catastrophic bug, and it can explain every change it made. What it cannot
do is try things. When every experiment costs weeks, the team learns to
stop proposing experiments, and the backlog fills with ideas nobody will
ever test. Meanwhile, teams that can test ten ideas in the time it takes to
test one start to learn faster. The orthodox team does not experience this
as a failure, because nothing broke. It notices it, eventually, as a market
that moved without it. There is a quieter risk too: engineers who want to
work with modern tools may not want to stay where those tools are kept at
arm's length. *The symptom is a backlog of reasonable ideas that nobody
expects to see built.*

I have seen this up close. One team worked in the conventional way:
estimates in man-days, plans on a whiteboard, steady but slow progress. It
was so slow that the people tracking its progress eventually gave up. The
team did deliver, but by then nobody was excited about what it delivered.
*Nothing broke, and something was still lost.*

**The agent-skeptic team breaks at the review queue.** When some engineers
generate code faster, the number and size of pull requests grow, but the
number of reviewers does not. Review becomes the bottleneck. Reviewers face
larger diffs, written in a style that is fluent but not quite their own,
and the temptation to skim is strong. On paper the process is unchanged:
every change reviewed and approved. In practice an approval can come to
mean less than it used to. *The evidence remains; the scrutiny behind it
thins.* A second break is uneven adoption. When one engineer works much
faster than the next, the team's estimates, its planning, and its sense of
fairness all start to wobble. *The symptom is review time growing while
review comments shrink.*

Our version of this break had a twist. Managers and product managers now
build too, through agents, and they are busy with their own products.
Juniors tag them for review. For a while, people generated code and sent it
to them to review, and it never shipped further, because the reviewers had
no context on what had been built or why. So we made a review of the
product requirements document mandatory. Anyone who wants a colleague to
review their code must involve that reviewer early, at the design stage if
possible. Key decisions and layouts are settled before the code exists,
instead of arriving as review comments that would need a complete rewrite.
*Review moved from the end of the work to the start.*

**The fully agentic team breaks on accountability.** Agents are good at
doing what they were asked. They are not good at knowing what they should
not have been asked. A fully agentic pipeline can take a vague request,
interpret it confidently, build it, test it against its own
interpretation, and deploy it, and every check will pass. The failure
shows up later, as behaviour nobody intended in a system nobody fully read.
When someone asks why the system does what it does, the answer is a chain
of prompts and generated plans rather than a decision a person made. In
most industries that is uncomfortable. In fintech it is not acceptable,
because a regulator, an auditor, or a customer has the right to ask who
decided, and **"the agent" is not an answer**. *The symptom is a question
about intent that nobody on the team can answer without reading the code.*

I have seen this too, in a different form. One project was peripheral to the
business, so we decided to build it fully agentically, to deliver fast.
The trouble came afterwards. When the code needed changes, or when a
requirement shifted even slightly, the people on the team were not in
control of it. Each change meant starting again from zero. *A system nobody
holds in their head cannot be changed, only replaced.*

There is a pattern across all three. Each kind of team protects one thing
and gives up another. The orthodox team protects **control** and gives up
**speed**. The fully agentic team protects speed and gives up control. The
agent-skeptic team tries to keep both by changing nothing important, and
slowly loses a little of each.

What none of them does by default is separate the two kinds of work
involved in shipping software: *deciding what should happen*, and *making
it happen*. Those two kinds of work carry very different risks, and they
suit very different hands. That separation is the core of the mix.

What has worked best for us so far started on the agent-skeptic side and
moved toward that separation. Agents built a fast first version, a minimum
viable product, so we could see the idea working. Then, before anything
went further, people reviewed the architecture and how it would behave
under scale and load. The code was rewritten to match that review, and only
then deployed. *The speed came from the agents; the control came from the
review in between.* A product that would have taken nine months was
delivered in four. That is the mix in an early form, and the rest of this
essay is about it.

<!-- REVIEW NOTES (remove before publishing)
1. Your answers (2026-10-31) filled the orthodox and fully agentic [ADD]s,
   and the "what has worked" paragraph. The agent-skeptic [ADD] (review
   load or uneven adoption) is still open, because your story is about what
   worked, not where that team breaks. Lines that are my wording, not
   yours: "Nothing broke, and something was still lost", "A system nobody
   holds in their head cannot be changed, only replaced", and "The speed
   came from the agents; the control came from the review in between".
   Also check "would have taken nine months": you said "a product of 9
   months", which I read as the estimate before agents.
2. Softened two claims that sounded like observations I could not source:
   "good engineers ... start to leave" is now a risk, not a fact, and
   "the honest ones admit they are skimming" is now "the temptation to skim
   is strong". Restore the stronger versions if they match what you have seen.
3. New: a one-line "symptom" for each team type, so readers can recognise
   the failure in their own team. Deeper thought: are these the right
   symptoms? The agent-skeptic one (review time up, review comments down)
   is something a team could actually measure.
-->
