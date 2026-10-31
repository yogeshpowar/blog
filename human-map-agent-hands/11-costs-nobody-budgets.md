---
layout: chapter
title: "11. The Costs Nobody Budgets For"
desc: "Human Map, Agent Hands · Chapter 11 of 13"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 11
permalink: /human-map-agent-hands/11-costs-nobody-budgets/
---

When people talk about the cost of AI in software teams, they usually mean
licences and model usage. Those costs are real, and they are easy to see on
an invoice. The costs I worry about more are the ones that do not appear on
any invoice, and that grow precisely because building became cheap.

The first is **the cost of running a platform under strict rules**. A
fintech platform is audited, tested for security, reviewed by partners, and
held to standards on availability, data protection, and record-keeping.
Every service we add enlarges that surface. Every new dependency is
another thing that must be scanned, every new data flow is another thing
that must be documented, and every new integration is another thing that
must be explained to an auditor. Integrations alone are a standing cost.
As I wrote in [India Fintech Open Source
Stack]({{ site.baseurl }}{% post_url 2023-07-19-IndiaFintech %}), each
vendor requires a new implementation that must be regularly maintained.

The second is **the cost of keeping foundations secure**. In my
experience, the stream of security issues in widely used open source
software has become one of the largest sources of unplanned work for an
engineering team. The public numbers point the same way. [One independent
count](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/) found
48,185 vulnerabilities (CVEs) published across all software in 2025, up
about 21% from 39,962 in 2024. [GitHub
reported](https://github.blog/security/supply-chain-security/a-year-of-open-source-vulnerability-trends-cves-advisories-and-malware/)
a 69% rise in published advisories about malicious open source packages
over the same period. A remote code execution flaw in a common library is
not a problem in our code, but it is our problem, with our deadline.
Components we once thought of as stable, the plumbing nobody thought
about, have needed urgent patches. On 31 March 2026,
attackers published two malicious versions of Axios, a widely used
JavaScript library; installing them [downloaded a remote access
trojan](https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/)
onto the machine. In October 2026, PHP issued [emergency
patches](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)
for two critical flaws that let an attacker without an account run code on
a web server, in nearly every PHP version back to 5.4. *The foundations we built on are being shaken*, and every
service an agent adds sits on those same foundations. Agents also add
dependencies easily, often without being asked. Each one should pass the
same checks as a dependency a person chose, because to an attacker it
makes no difference who added it.

The third is **the cost of review**. Agents shift work from writing to
reading. That is a good trade when the reading is focused, and a bad one
when every change produces a large diff that a senior engineer must
understand. Review time does not appear in any budget line, but it is the
scarcest thing in most teams, and agents compete for it. The map from
[chapter 4]({{ '/human-map-agent-hands/04-map-and-control/' | relative_url }}) and the agreed tests from [chapter 7]({{ '/human-map-agent-hands/07-tests-as-guardrails/' | relative_url }}) are the best ways I know to
keep that cost down.

The fourth is **the cost of code nobody wrote**. Code generated quickly
still has to be understood when it breaks at an inconvenient hour. If
nobody on the team ever held that code in their head, the first person to
do so will be the one on call, under pressure. Teams need deliberate
habits to keep understanding in step with output: walkthroughs, design
notes, agent summaries that are actually read.

This is not a new problem. Long before agents, key modules written by
people who had since left were treated as black boxes, and everyone worked
around them. What has changed is that agents help here too. They can read
old code that nobody wanted to touch, find its loopholes, and suggest
upgrades. *Code nobody wrote and code nobody remembers are the same risk*,
and agents can help with both, as long as someone reads what they find.

The fifth is **the cost of keeping the agent's world in shape**. The local
environments, observability, tests, and written maps that make agents
safe are themselves software. They drift, break, and need owners. This is
an investment, and it pays back, but it has to be budgeted as real work,
not as something engineers will do in their spare time.

And the sixth, which no amount of engineering removes, is **the cost of
distribution**. Finding customers, earning their trust, and keeping them
is still expensive and still uncertain. Agents have made it much cheaper
to build something. They have not made it much cheaper to get anyone to
use it. In financial services, where trust is earned slowly, this may be
the most important cost of all. *If building is cheap and distribution is
expensive, then building more is not a strategy. Choosing better is.*

None of these costs is an argument against agents. They are an argument
for **counting the whole cost before choosing the speed**. A team that
budgets only for the building will be surprised by everything that comes
after it.
