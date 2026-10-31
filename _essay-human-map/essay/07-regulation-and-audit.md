## 7. Regulation and the Audit Trail

Working in fintech in India means that every serious change eventually
meets a question from outside the engineering team, from compliance, an
auditor, or a regulator. The question is rarely "did the code work?". It
is usually "who decided this, on what basis, and how do you know it was
done correctly?".

That question is why I think of **human checkpoints as evidence**, not as
bureaucracy. When a named person approves a change against a written map,
and that approval is recorded next to the tests that ran and their results,
the organisation has something it can show. When an agent merges and
deploys on its own, the organisation has logs, and logs are not a decision.

The rules point the same way. India's [Digital Personal Data Protection
Act, 2023](https://www.indiacode.nic.in/bitstream/123456789/22037/2/a2023-22.pdf)
requires an organisation to protect personal data "by taking reasonable
security safeguards to prevent personal data breach" (section 8(5)), to
report breaches, and, for the largest data handlers, to appoint an
independent data auditor (section 10(2)). Its rules, notified in November
2025, mostly apply from May 2027. For financial entities, the Reserve Bank
of India issued technology risk directions in July 2026, with a separate
version for each type of regulated entity. I use the [version for
non-banking financial
companies](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13592)
only as an illustration. It asks for a board-approved change management
policy, audit trails, and maker-checker controls under which transactions
are completed only after independent verification and approval by at least
two individuals.

Maker-checker is the oldest idea in financial controls: one person makes,
another checks, and neither can do both. The rule is written for
transactions, not for code, but the mix I am describing is the same
principle applied to software, with one detail a risk officer will rightly
press on. An agent and the engineer directing it are one maker, not two.
The checker has to be someone else. In our teams, every pull request is
reviewed by a peer, never only by its author. The one exception is the
first drop of a very new, isolated project, which can go out without a
second reviewer so that the team reaches an MVP faster. That exception
belongs only where a mistake is cheap to undo, which is what the grid in
chapter 4 is for. I find that compliance teams recognise maker-checker
quickly when it is described this way.

I am not a lawyer, and nothing here is legal advice. But my reading is
that none of these frameworks asks whether code was written by a person or
by a tool. They ask whether **the organisation can show it was in
control**. Agents can make that easier, if the record is designed in. An
agent can attach to every change the map it worked from, the tests it
ran, the environment output, and a plain summary of what it did, which is
a more complete record than most engineers ever produced by hand. What it
cannot provide is the decision. The record must show which person
accepted the risk.

Agents also help find gaps. Given a regulation, an internal policy, and a
codebase, an agent can point to personal data logged where the policy
forbids it, a retention rule that is not implemented, or an access path
that lacks the review the policy requires. We do this often, by asking an
agent to take a role: a chief information security officer reviewing a
design, a vulnerability assessment and penetration testing (VAPT) tester
probing the system, or an information security reviewer reading a policy
against the code. Each role makes the agent look for different gaps. The
line I draw is simple to say and hard to keep: agents can find gaps;
**people accept the risk**. Deciding that a remaining gap is acceptable, or
telling a regulator that a control is in place, belongs to a person whose
name is on the record.

Agents also bring a question of their own. When an agent reads code,
configuration, or logs, that material may be sent to a model provider. The
agent is then part of the data flow and the supply chain, and it deserves
the same scrutiny as any other third party: what it can see, where that
data goes, and what is retained. Keeping real customer data out of the
environments agents work in, as chapter 5 argued, makes this far easier to
answer.

So the audit trail has three layers. The *map*: intent, boundaries, risk
class, and approver, written before the work. The *evidence*: tests,
environment results, traces, and the agent's summary, produced during the
work. The *decision*: a named person's approval, recorded with the time
and the evidence they looked at. With all three, agent speed and
regulatory accountability can live together. With only the evidence, you
have a fast system that cannot explain itself. In my [agentic SDLC
pilot]({{ site.baseurl }}{% post_url 2026-10-02-Agentic-SDLC %}), the
decision layer lived in git: each approval was a commit, pinned to the
exact commit being shipped, so the audit is a search of the history.

<!-- REVIEW NOTES (remove before publishing)
1. Deeper thought, new: maker-checker as the bridge between finance and the
   mix ("the agent makes; a person checks"). The essay says plainly that
   the RBI rule is about transactions, not code, and presents the link as
   an analogy. The line "compliance teams recognise it quickly" is written
   as your experience. Confirm it or cut it.
2. New: agents as part of the data flow and supply chain (code and logs
   sent to a model provider). This is a real concern for regulated
   readers. It makes no legal claim. Keep, expand, or cut?
3. Removed "used to need weeks ... now days", which was an unsourced
   time claim. It now reads "a blank page" vs "a first draft".
4. Two whole bold sentences ("They ask whether..." and "Agents can find
   gaps. Humans accept the risk.") now bold only the key phrase. "Humans"
   became "people" to match the rest of the essay. The brief's core ideas
   say "humans accept the risk". Switch back if you prefer.
5. The long regulation paragraph is split into DPDP and RBI paragraphs,
   with links to the official texts.
6. Experience claim: the closing line ("the more common reason, in my
   experience"). Confirm.
7. Filled (your answer, 2026-10-31): agents asked to act as CISO, VAPT
   tester, or information security reviewer to find gaps. "Each role makes
   the agent look for different gaps" is my wording.
8. Revised 2026-11-01 (review finding 4): the agent plus the engineer who
   directs it count as one maker; a different person checks. Your practice:
   every PR is peer reviewed, except the first drop of a very new, isolated
   project, which can skip a second reviewer to reach an MVP faster. Confirmed:
   that first drop goes out without peer review. The line
   "That exception belongs only where a mistake is cheap to undo" is my
   wording, written as advice. Removed the italic "The agent makes; a person
   checks." because, as written, it described one human, not two.
9. Trimmed 2026-11-01 (review findings 2, 10, 13, 14): about 1,070 to about
   800 words. The DPDP section keeps one quote and summarises the rest. The
   RBI paragraph now says each type of regulated entity has its own version
   and the NBFC one is only an illustration, so readers are less likely to
   infer the regulator in the chapter 8 story. Cut: the Superintelligence
   link, the closing signpost "Regulation is one reason to slow down",
   the italics on "finding gaps", and repeated sentences.
-->
