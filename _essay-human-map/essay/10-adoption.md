## 10. Adoption: Moving a Team Toward the Mix

Our own path went through all three kinds of team. From a single
developer, to a team of experts, to pods, we worked the conventional,
orthodox way. The move toward agents did not start as a push from the top.
Some people were curious and began using AI on their own, and some started
presenting its work as their own. When the push from the top did come, it
leaned on what the orthodox way values most: we put a person at every step.
Then, as we built protocols like
[PROTO]({{ site.baseurl }}{% post_url 2025-09-13-PROTO %}) and ran agentic
orchestration like the [pilot I described
earlier]({{ site.baseurl }}{% post_url 2026-10-02-Agentic-SDLC %}), our
confidence grew, and we moved closer to the fully agentic end. We do not
aim to be fully agentic. We aim to move more of our work into the
autonomous corner as the evidence earns it.

That path taught me that a team does not move by announcement. A memo that
says "we are now an agentic team" changes the tools and leaves the habits,
and the habits decide what happens. Moving a team is a sequence of small,
reversible steps, each justified by evidence from the step before. It is
the same lesson as growing a company, which I wrote about in [From
One-Person Engine to Multi-Layered
Machine]({{ site.baseurl }}{% post_url 2026-05-06-Solo-to-multi-layerd-machine %}):
the real work is managing each transition deliberately.

[DIAGRAM: diagrams/10-adoption-timeline.mmd]

I think of it as four stages, with an **evidence checkpoint** between each.
In the first, agents assist individuals with work that never reaches
customers on its own, and nothing about releases changes. The checkpoint is
whether the team can name, from its own experience, where agent output can
be trusted and where it cannot. In the second, the team builds the map,
the senses, and the guardrails of chapters 3, 5, and 6: production-like
environments, local observability, meaningful tests, and a map format
people actually use. The checkpoint is whether an agent can make a change
and return evidence that a reviewer finds convincing.

In the third stage, agents carry changes to pull requests and named people
approve them, with risk classes enforced in permissions and pipelines, as
chapter 4 described. The checkpoint is whether approved changes behaved as
the evidence said, and whether reviewers were reviewing rather than
rubber-stamping. The fourth stage is where the grid is meant to lead. In
the low-risk corner, agents would ship without a person approving each
change, and people would review the record afterwards, while the
highest-risk actions stay human at every step. That stage is never
finished: every incident, audit, or change in the rules is a reason to
revisit a tier. The checkpoints also do a second job. Their evidence is the
same kind chapter 7 described for auditors and regulators, so a team that
adopts agents this way builds its audit trail as it goes.

Where are we? For production, we are at stage three: agents do much of the
work, and people approve what ships. No production deployment is fully
autonomous yet. Below production, we are further along. For some projects,
changes to development and UAT deploy automatically, and on the local setup
agents have full autonomy. As chapter 4 described, for us autonomy follows
the environment before it follows the change.

A few things I have learned along the way. Start with willing people on
low-risk work, and let their results do the persuading; in my experience,
evidence from a colleague persuades engineers more than advice from
leadership does. A pod, with a couple of developers, a product manager, and
a QA engineer, is a natural unit for this, because it has every role the
stages need. Keep the cautious voices in the room. The people most wary of
agents are often the ones who remember why a rule exists, and they make
the map better. Measure what reaches customers, not what is generated: how
often a change has to be rolled back, and how long review takes compared
with how much it finds, say more than the number of pull requests. And
expect roles to change, and say so honestly. The work shifts toward
writing maps, reviewing evidence, and owning environments. That is a
change in what people do, not in whether they are needed, as I told
students in [Dont Fear AI, Learn to Engineer With
It]({{ site.baseurl }}{% post_url 2026-09-20-Dont-Fear-AI-Learn-To-Engineer-With-It %}).

Adoption also needs a way back. If the evidence at a checkpoint is weak,
the honest response is to stay where you are, or step back, and fix what
is missing. A team that can only move forward is not adopting a practice.
It is following a fashion.

<!-- REVIEW NOTES (remove before publishing)
1. The brief asks for your real experiences here. Two [ADD]s are open:
   where your teams are today (plus what was harder than expected), and an
   optional step back.
2. New: stage four now has a checkpoint ("never ends": incidents, audits,
   rule changes). Before, it had none, which made the timeline look
   finished.
3. Deeper thought, new: "a team that adopts agents this way builds its
   audit trail as it goes". This links adoption to chapter 7. Is that true
   in your experience, or is it a hope?
4. Stage names moved from bold to italics, to reduce bold. The four
   lessons keep bold, since they are what a skimmer should see.
5. "Keep the orthodox voices in the room" became "cautious voices", so it
   does not read as a label for people (chapter 2 says the types are not
   labels for people).
6. "Engineers trust evidence from colleagues far more than advice from
   leadership" is now a softer experience claim. Confirm.
7. "That is a change in what people do, not in whether they are needed"
   was added for hard rule 6 (no claims that roles disappear).
8. New metric suggestion: rollback frequency, and review time compared
   with what review finds (links to the chapter 2 symptom).
9. New (2026-10-31): a pod as the natural unit for starting adoption. This
   is offered as advice, not as what your teams did. If a pod did go first,
   that would be a good answer to the [ADD] about where your teams are
   today.
10. Revised 2026-11-01 (review finding 5): stage four is now written as
   intent ("would"), since production is at stage three.
11. Moved here 2026-11-01 from chapter 11 (review finding 11): your
   adoption path, placed just before "Where are we?".
12. Trimmed 2026-11-01 (review findings 2, 6, 7): about 1,000 to about 820
   words. Opens on your path story instead of a generic line. The four
   stages are two paragraphs of prose instead of four labelled ones. The
   four bold lessons are plain prose. Removed italics, including on "builds
   its audit trail as it goes" and "following a fashion".
-->
