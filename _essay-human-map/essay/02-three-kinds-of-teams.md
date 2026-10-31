## 2. Three Kinds of Teams and Where They Break

Teams are responding to agents in three broad ways. These are not labels
for people, and none of them is foolish. Each is a reasonable answer to a
real fear, each fails in its own way, and a single company can have all
three at once. I have seen all three at work.

[DIAGRAM: diagrams/02-spectrum.mmd]

The first is the **orthodox team**. It works the way good teams worked five
years ago: requirements written and estimated, code built and reviewed by
hand, a release on a schedule. AI may help with documentation or an email,
but not with code that ships. The reasons are often sound, such as data
leaving the company, licensing, or code nobody fully understands, and in a
regulated business they are not paranoia. Every change has a human author
and a human reviewer, so the process produces evidence almost by accident.
The orthodox team breaks on opportunity cost. When every experiment costs
weeks, people stop proposing experiments, and the backlog fills with ideas
nobody will test. Nothing breaks, so nobody calls it a failure. I have seen
one such team up close: estimates in man-days, plans on a whiteboard,
steady but slow progress. It was so slow that the people tracking its
progress eventually gave up. The team did deliver, but by then nobody was
excited about what it delivered.

The second is the **agent-skeptic team**. It uses AI in small doses, such
as code completion, a chat window for a stubborn regular expression, or a
first draft of a unit test, and the process around the code does not
change. In my experience this is the most common pattern, and a sensible
place to start. It breaks at the review queue. When some engineers produce
code faster, pull requests grow in number and size, but reviewers do not.
Reviewers face larger diffs in a style that is fluent but not their own,
and an approval comes to mean less than it used to. The symptom is review
time growing while review comments shrink. Our version had a twist.
Managers and product managers now build too, through agents, and they are
busy with their own products. Juniors tagged them for review, and code
generated that way never shipped, because the reviewers had no context on
what had been built or why. So we made a review of the product
requirements document mandatory. Anyone who wants a colleague to review
their code must involve that reviewer early, at the design stage if
possible, so that key decisions are settled before the code exists rather
than arriving as review comments that need a complete rewrite.

The third is the **fully agentic team**. A person describes an outcome, and
agents plan it, write the code and the tests, and open the pull request; in
the boldest setups they also merge and deploy when the checks pass. These
teams are fast in a way the other two cannot match. They break on
accountability. Agents are good at doing what they were asked and poor at
knowing what they should not have been asked. A vague request can be
interpreted confidently, built, tested against that interpretation, and
deployed, with every check passing. When someone later asks why the system
behaves as it does, the answer is a chain of prompts rather than a decision
a person made. In fintech that is not acceptable, because a regulator, an
auditor, or a customer has the right to ask *who decided this, and where is
that written down?*, and **"the agent" is not an answer**. We saw a
different form of this break. One project was peripheral to the business,
so we built it fully agentically, to deliver fast. The trouble came
afterwards. When the code needed changes, or a requirement shifted even
slightly, nobody on the team was in control of it, and each change meant
starting again from zero.

A simple way to place your own team is to ask three questions about the
last change that reached customers. Who wrote the code? Who checked it?
Who decided it could go live? If the answer to all three is a person, you
are near the orthodox end, whatever tools people use in their editors. If
an agent wrote it and a person checked and released it, you are in the
middle. If an agent did all three, you are at the agentic end, whether or
not anyone chose to be there.

Each kind of team protects one thing and gives up another. The orthodox
team protects control and gives up speed. The fully agentic team protects
speed and gives up control. The agent-skeptic team tries to keep both by
changing nothing important, and slowly loses a little of each. What none of
them does by default is separate the two kinds of work in shipping
software: deciding what should happen, and making it happen. Those carry
very different risks and suit very different hands. **The mix I argue for**
separates them, and it is not a fixed point on the line. It moves with what
is being changed.

What has worked best for us so far started on the agent-skeptic side and
moved toward that separation. Agents built a fast first version, a minimum
viable product, so we could see the idea working. Then, before anything
went further, people reviewed the architecture and how it would behave
under scale and load. The code was rewritten to match that review, and only
then deployed. The first version was a probe, not the product: it showed
us what to build, and the review turned that into the map the real code was
written against. A product we had estimated at nine months before agents
was delivered in four.

<!-- REVIEW NOTES (remove before publishing)
Merged 2026-11-01 from old chapters 2 and 3 (review finding 2).
1. Each team type now has its description, where it breaks, and your story
   in one paragraph. The three-question self-test and the "what worked" MVP
   story are kept; the MVP story must stay last, because chapter 3 refers
   back to it.
2. Cut: the second ending of old chapter 2, "the rest of this essay tries to
   make that trade explicit", the "quieter risk" about engineers leaving,
   uneven adoption, and all italic one-liners ("Nothing broke, and something
   was still lost", "The evidence remains...", "Review moved from the end of
   the work to the start", "A system nobody holds in their head...").
3. Kept bold: the three team names, "the agent" is not an answer, and "the
   mix I argue for". The diagram still shows the mix as a fixed node, which
   the review flagged; that is for the diagrams pass.
4. Confirmed facts used: nine months was the estimate before agents.
-->
