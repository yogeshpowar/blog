## 13. The Hard Picture

I want to end without pretending that any of this is simple.

The hard picture is this. Building has become fast, and it will keep
getting faster. Failure has become cheap in time, and teams that use that
to learn will pull ahead of teams that do not. At the same time, nothing
about running a platform, keeping it secure, satisfying the rules it lives
under, or finding people who want what it offers has become cheap. If
anything, those costs have grown, because there is more software to own
and the foundations under it are less settled than they were.

Every engineering team now sits between those two facts. There is no
position on the line from orthodox to fully agentic that is free of cost.
The orthodox team pays in speed and in the ideas it never tests. The fully
agentic team pays in decisions nobody made and evidence nobody can show.
The agent-skeptic team pays a little of both while feeling it has paid
neither. *Every team is choosing.* The only question is whether it
**chooses on purpose**.

My own path went through all three. From a single developer, to a team of
experts, to pods, we worked the conventional, orthodox way. The move toward
agents did not start as a push from the top. Some people were curious and
began using AI on their own, and some started presenting its work as their
own. When the push from the top did come, it leaned on what the orthodox
way values most: we put a person at every step. Then, as we built
protocols like [PROTO]({{ site.baseurl }}{% post_url 2025-09-13-PROTO %})
and ran agentic orchestration like the [pilot I described
earlier]({{ site.baseurl }}{% post_url 2026-10-02-Agentic-SDLC %}), our
confidence grew, and we moved closer to the fully agentic end. *We do not
aim to be fully agentic. We aim to get closer to it, with faster human
approvals.*

The mix I have described is my attempt to choose on purpose. Humans hold
the map: the intent, the boundaries, the risk classes, and the approvals.
Agents do the hands-on work: the code, the tests, the environments, and
the analysis. The balance between them is not fixed. It is set by what a
failure would cost, and the honest measure of that is the worst thing a
change could do, not the change itself. It is enforced by the system
rather than by goodwill, and revisited as the evidence changes.
Environments and observability give agents senses. Tests give them
guardrails. Wider end-to-end testing lets more people check the work. And
the audit trail turns all of it into something an organisation can stand
behind.

None of this is new in spirit. Finance has long relied on the idea that
one person makes and another checks. What is new is that the maker can now
be an agent, working faster than any of us, and that makes the checker
more important, not less.

None of this removes the need for engineers either. It changes what good
engineering looks like. The engineer who writes a clear map, reads evidence
carefully, owns an environment, and knows when to say "we should not build
this" is more valuable now, not less. I do not know exactly how teams will
look in five years, and I am wary of anyone who claims to. What I do know
is that the judgement to decide what matters, and the accountability for
that decision, still sit with people. Tasks can be assigned, to a person or
to an agent, and so can authority. As I wrote in [From Character to
Ownership]({{ site.baseurl }}{% post_url 2026-07-22-ownership %}),
ownership cannot.

And so I come back to the decision that agents help with least. In a world
where almost anything can be built by Friday, the scarce skill is not
building. It is choosing. *Nine of ten things will look right*, and from
the inside the tenth looks just like them. The work of a team, and
especially of its leaders, is to test the things outside the code before
the building starts, to protect the nine that matter, and to have the
evidence to explain both choices to anyone who asks.

The most valuable decision is often **what not to build**. Agents have not
changed that. They have made it matter more.

---

*This essay is licensed under [Creative Commons Attribution 4.0
(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).*

<!-- REVIEW NOTES (remove before publishing)
1. Your path added (2026-10-31): orthodox from solo to experts to pods;
   curiosity from below, including people presenting AI work as their
   own; the response was a person at every step; PROTO and agentic
   orchestration built confidence; the aim is closer to fully agentic with
   faster human approvals, not all the way. The rest of the chapter is
   still my draft, so approve or rewrite it.
2. New: the closing now gathers the ideas added during refinement, as
   threads rather than a recap list: "the worst thing a change could do"
   (chapter 5), maker-checker (chapter 9), and "the tenth looks just like
   them" plus "test the things outside the code" (chapter 10).
3. Deeper thought: the new maker-checker paragraph ("makes the checker more
   important, not less") is a candidate for the essay's last image instead
   of "what not to build". The brief's thesis ends on "what not to build",
   so I kept that as the final line. Your call.
4. Two whole bold sentences now bold only the key phrase: "chooses on
   purpose" and "what not to build".
5. Hard rule 6: "None of this removes the need for engineers" stays as the
   explicit statement that roles are not disappearing.
-->
