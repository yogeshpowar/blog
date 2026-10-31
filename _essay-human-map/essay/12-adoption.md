## 12. Adoption: Moving a Team Toward the Mix

If the mix is the goal, how does a team get there? Not by announcement. A
memo that says "we are now an agentic team" changes the tools and leaves
the habits, and the habits decide what actually happens. In my experience,
moving a team is a sequence of small, reversible steps, each one justified
by evidence from the step before. It is the same lesson as growing a
company, which I wrote about in [From One-Person Engine to Multi-Layered
Machine]({{ site.baseurl }}{% post_url 2026-05-06-Solo-to-multi-layerd-machine %}):
the real work is managing each transition deliberately.

[DIAGRAM: diagrams/12-adoption-timeline.mmd]

I think of it as four stages, with an **evidence checkpoint** between each.

*Stage one: assist.* Agents help individuals with work that never reaches
customers on its own: explaining unfamiliar code, drafting tests,
summarising logs, writing internal documentation. Nothing about the
release process changes. The purpose of this stage is to build familiarity
and to learn where the tools are reliable and where they are not. The
checkpoint before moving on is simple: can the team name, from its own
experience, the kinds of task where agent output can be trusted and the
kinds where it cannot?

*Stage two: build the senses and the guardrails.* Before agents get more
autonomy, the team invests in what makes autonomy safe: an environment
that matches production, local observability, a test suite that states
real business rules, and a written map format that people actually use.
These are chapters 4, 6, and 7 of this essay, and agents can do much of
the work themselves. The checkpoint: can an agent make a change, run it in
a realistic environment, and return evidence that a reviewer finds
convincing?

*Stage three: propose and approve.* Agents now carry changes from map to
pull request, with tests and evidence, and named people approve before
anything reaches customers. Risk classes are assigned to parts of the
system and enforced in permissions and pipelines, as chapter 5 described.
The checkpoint: over a meaningful period, did approved agent changes
behave as the evidence said they would, and did reviewers feel they were
reviewing rather than rubber-stamping?

*Stage four: autonomy by tier.* In the low-risk corner of the grid, agents
ship without a person approving each change, and people review the record
afterwards. Everywhere else, propose and approve continues, and the
highest-risk actions remain human at every step. This stage is never
finished, and so its checkpoint never ends. Every incident, every audit,
and every change in the rules is a reason to ask whether an area belongs
in a different tier.

The checkpoints do a second job. The evidence a team gathers to decide
whether to move forward is the same kind of evidence chapter 9 described
for auditors and regulators. *A team that adopts agents this way builds
its audit trail as it goes*, instead of trying to reconstruct one later.

Where are we? For production, we are at stage three: agents do much of the
work, and people approve what ships. No production deployment is fully
autonomous yet. Below production, we are further along. For some projects,
changes to development and UAT deploy automatically, and on the local setup
agents have full autonomy. As chapter 5 described, for us autonomy follows
the environment before it follows the change.

Some things I have learned to watch for, offered as my experience rather
than as rules. **Start with willing people on low-risk work**, and let
their results do the persuading. A pod is a natural unit for this. With a
couple of developers, a product manager, and a QA engineer, it has every
role the stages need, from writing the map to checking the evidence, and
its results are easy for other pods to see. In my experience, evidence from a
colleague persuades engineers more than advice from leadership does.
**Keep the cautious voices in the room.** The people most wary of agents
are often the ones who remember why a rule exists, and they make the map
better. **Measure what reaches customers, not what is generated.** More
code, more pull requests, and more tests are not outcomes. How often a
change has to be rolled back, and how long review takes compared with how
much it finds, say more. **Expect roles to change, and say so honestly.**
The work shifts toward writing maps, reviewing evidence, and owning
environments. That is a change in what people do, not in whether they are
needed, and it deserves support and training, not surprise. I said the
same to students in [Dont Fear AI, Learn to Engineer With
It]({{ site.baseurl }}{% post_url 2026-09-20-Dont-Fear-AI-Learn-To-Engineer-With-It %}):
some roles will evolve, but that does not mean the end of engineering.

Adoption also needs a way back. Every stage should be reversible. If the
evidence at a checkpoint is weak, the honest response is to stay where you
are, or step back, and fix what is missing. *A team that can only move
forward is not adopting a practice. It is following a fashion.*

<!-- REVIEW NOTES (remove before publishing)
1. The brief asks for your real experiences here. Two [ADD]s are open:
   where your teams are today (plus what was harder than expected), and an
   optional step back.
2. New: stage four now has a checkpoint ("never ends": incidents, audits,
   rule changes). Before, it had none, which made the timeline look
   finished.
3. Deeper thought, new: "a team that adopts agents this way builds its
   audit trail as it goes". This links adoption to chapter 9. Is that true
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
   with what review finds (links to the chapter 3 symptom).
9. New (2026-10-31): a pod as the natural unit for starting adoption. This
   is offered as advice, not as what your teams did. If a pod did go first,
   that would be a good answer to the [ADD] about where your teams are
   today.
-->
