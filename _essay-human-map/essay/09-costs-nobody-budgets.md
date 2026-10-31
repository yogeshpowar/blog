## 9. The Costs Nobody Budgets For

The cost of AI that shows up on an invoice is licences and model usage. The
costs I worry about more never appear on one, and they grow precisely
because building became cheap.

The first is **running a platform under strict rules**. A fintech platform
is audited, tested for security, reviewed by partners, and held to
standards on availability, data protection, and record-keeping. Every new
service enlarges that surface: every dependency must be scanned, every
data flow documented, every integration explained to an auditor.

The second is **keeping the foundations secure**. In my experience,
security issues in widely used open source software have become one of the
largest sources of unplanned work for an engineering team, and the public
numbers agree: [one independent
count](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/) found
48,185 published vulnerabilities in 2025, up about 21% from 2024. On 31
March 2026, two malicious versions of Axios, a widely used JavaScript
library, [installed a remote access
trojan](https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/)
on any machine that installed them. In October 2026, PHP shipped [emergency
patches](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)
for two flaws that let an attacker without an account run code on a web
server, in nearly every PHP version back to 5.4. A flaw in a common library
is not in our code, but it is our problem, with our deadline, and every
service an agent adds sits on those same foundations. Agents also add
dependencies easily, often unasked. Each one should pass the same checks as
one a person chose; to an attacker it makes no difference who added it.

The third is **code nobody wrote**. Code generated quickly still has to be
understood when it breaks at an inconvenient hour, and if nobody ever held
it in their head, the first person to do so will be the one on call. This
is not new. Long before agents, key modules written by people who had since
left were treated as black boxes. What has changed is that agents help here
too: they can read old code that nobody wanted to touch, find its
loopholes, and suggest upgrades, as long as someone reads what they find.

The fourth is **keeping the agent's world in shape**. The environments,
observability, tests, and maps that make agents safe are themselves
software. They drift and need owners, and they have to be budgeted as real
work, not left to spare time.

The fifth, which no engineering removes, is **distribution**. Finding
customers, earning their trust, and keeping them is still expensive and
uncertain. Agents have made it much cheaper to build something, not to get
anyone to use it, and in financial services trust is earned slowly. If
building is cheap and distribution is expensive, building more is not a
strategy. Choosing better is.

None of this is an argument against agents. It is an argument for
**counting the whole cost before choosing the speed**.

<!-- REVIEW NOTES (remove before publishing)
1. Hard rule 2: no company figures. The only numbers are the public CVE and
   GitHub figures (verified, rows 9 and 10 in references/to-verify.md),
   now linked. The CVE count now says "across all software", because it is
   not limited to open source. The GitHub figure now says "advisories about
   malicious open source packages", which is what it measures.
2. New: agents add dependencies easily, and each one needs the same checks
   as one a person chose. No external claim is made.
3. New: one line linking review cost back to the map (chapter 3) and agreed
   tests (chapter 6).
4. Experience claim: "the stream of security issues ... one of the largest
   sources of unplanned work". Confirm.
5. Deeper thought: six costs, each bolded as a heading inside prose. This is
   the most bold in any chapter, but it lets a skimmer see the list. Keep,
   or switch the six to italics?
6. The brief asks for your real experiences here, in qualitative form.
   Two [ADD]s are still open.
7. Filled (your answer, 2026-10-31): black-box modules from former
   employees, now read by agents that find loopholes and suggest upgrades.
   My wording: "Code nobody wrote and code nobody remembers are the same
   risk" and "as long as someone reads what they find".
8. Trimmed 2026-11-01 (review findings 2 and 10): about 820 to about 560
   words. Cut the cost of review (chapters 2 and 3 cover it), the India
   Fintech link, the GitHub malware statistic (still verified in the
   references file, just unused), "habits to keep understanding in step"
   (walkthroughs, design notes), and the italic lines. Six costs became
   five. The CVE figure and both 2026 incidents stay.
-->
