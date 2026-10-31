---
layout: chapter
title: "9. Regulation and the Audit Trail"
desc: "Human Map, Agent Hands · Chapter 9 of 13"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 9
permalink: /human-map-agent-hands/09-regulation-and-audit/
image: /images/human-map-agent-hands-cover.jpg
---

Working in fintech in India means that every serious change eventually
meets a question from outside the engineering team. Sometimes it comes from
compliance, sometimes from an auditor, sometimes from a regulator. The
question is rarely "did the code work?". It is usually "who decided this,
on what basis, and how do you know it was done correctly?".

That question is why I think of **human checkpoints as evidence**, not as
bureaucracy. When a named person approves a change against a written map,
and that approval is recorded next to the tests that ran and the results
they produced, the organisation has something it can show. When an agent
merges and deploys on its own, the organisation has logs, and logs are not
the same as a decision.

The rules point the same way. India's [Digital Personal Data Protection
Act, 2023](https://www.indiacode.nic.in/bitstream/123456789/22037/2/a2023-22.pdf)
requires an organisation to protect personal data "by taking reasonable
security safeguards to prevent personal data breach" (section 8(5)), and to
inform the Data Protection Board and each affected person when a breach
happens (section 8(6)). Organisations notified as Significant Data
Fiduciaries must also appoint an independent data auditor and carry out
periodic Data Protection Impact Assessments and audits (section 10(2)). The
DPDP Rules, 2025, notified in November 2025, phase these obligations in,
with most operational rules due to apply from May 2027.

For financial entities, the Reserve Bank of India issued entity-wise
Cybersecurity, Technology: Risk, Resilience and Assurance Framework
Directions in July 2026. The [version for non-banking financial
companies](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13592),
for example, asks for a board-approved change management policy, audit
trails for IT assets, and maker-checker controls under which transactions
are completed only after independent verification and approval by at least
two individuals.

Maker-checker is worth pausing on, because it is the oldest idea in
financial controls: one person makes, another checks, and neither can do
both. That rule is written for transactions, not for code. But the mix I
am describing is the same principle applied to software. *The agent makes;
a person checks.* Finance has trusted this pattern for a long time, and I
find that compliance teams recognise it quickly when it is described this
way. I explored the same idea for groups of agents in [an earlier essay on
superintelligence as a civilization of
agents]({{ site.baseurl }}{% post_url 2026-10-01-Superintelligence-Civilization %}):
the agent that places the order is not the one that approved it.

I am not a lawyer, and nothing here is legal advice. But my reading is
that none of these frameworks asks whether code was written by a person or
by a tool. They ask whether **the organisation can show it was in
control**.

Agents do not make that harder by default. They can make it easier, if the
record is designed in. An agent can attach to every change the map it
worked from, the tests it ran, the environment output, and a plain summary
of what it did. That is a more complete record than most engineers ever
produced by hand. What the agent cannot provide is the decision itself. The
record must show which person accepted the risk.

There is a second way agents help: *finding gaps*. Agents are good at
reading large volumes of text patiently. Given a regulation, an internal
policy, and a codebase, an agent can point to places where, for example,
personal data is logged when the policy says it should not be, a retention
rule is not implemented, or an access path lacks the review the policy
requires. We do this often, by asking an agent to take a role: a chief
information security officer reviewing a design, a vulnerability
assessment and penetration testing (VAPT) tester probing the system, or an
information security reviewer reading a policy against the code. Each role
makes the agent look for different gaps. This kind of review used to start from a blank page and
a specialist's time. Now it can start from a first draft that the
specialist checks.

Agents also bring a question of their own. When an agent reads code,
configuration, or logs, that material may be sent to a model provider.
For a regulated business, the agent is then part of the data flow and the
supply chain, and it deserves the same scrutiny as any other third party:
what it can see, where that data goes, and what is retained. Keeping real
customer data out of the environments agents work in, as [chapter 8]({{ '/human-map-agent-hands/08-who-can-test/' | relative_url }})
argued, makes this question far easier to answer.

The line I draw is simple to say and hard to keep: agents can find gaps;
**people accept the risk**. An agent can tell you that a control is
missing, suggest how to add it, and even add it. Deciding that a remaining
gap is acceptable, signing off a risk assessment, or telling a regulator
that a control is in place are acts of accountability. They belong to a
person whose name is on the record.

In practice this means the audit trail has three layers. The first is the
*map*: intent, boundaries, risk class, and approver, written before the
work. The second is the *evidence*: tests, environment results, traces,
and the agent's summary, produced during the work. The third is the
*decision*: a named person's approval, recorded with the time and the
evidence they looked at. With all three, agent speed and regulatory
accountability can live together. With only the second, you have a fast
system that cannot explain itself. In my [agentic SDLC
pilot]({{ site.baseurl }}{% post_url 2026-10-02-Agentic-SDLC %}), the
decision layer lived in git: each approval was a commit, pinned to the exact
commit being shipped, so the audit is a search of the history.

Regulation is one reason to slow down. The more common reason, in my
experience, is that the thing should not have been built at all.
