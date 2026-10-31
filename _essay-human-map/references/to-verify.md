# References

Checked on 2026-10-31. "Primary" means the claim was read on the
publisher's own page or document. "Secondary" means it was read in reliable
coverage because the primary source could not be fetched.

## Verified

| # | Sec | Source | URL | Type | Exact claim supported |
|---|-----|--------|-----|------|-----------------------|
| 1 | 1 | METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 10 Jul 2025 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | Primary | 16 experienced developers, 246 issues in their own repos; with AI they took 19% longer; they expected a 24% speedup and afterwards believed AI had sped them up by about 20%. The page now says its results are superseded by the Feb 2026 update. |
| 2 | 1 | METR, "We are Changing our Developer Productivity Experiment Design", 24 Feb 2026 | https://metr.org/blog/2026-02-24-uplift-update/ | Primary | The new experiment "gives us an unreliable signal"; some evidence of speedup (original devs -18%, CI -38% to +9%; new devs -4%, CI -15% to +9%); developers increasingly declined to participate because they did not want to work without AI. |
| 3 | (dropped) | Google Cloud, "Announcing the 2024 DORA report", 23 Oct 2024 | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report | Primary | "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%." |
| 4 | 7 | DevClass (Tim Anderson), "AI is eroding code quality states new in-depth report", 20 Feb 2025, on GitClear's 2025 AI Copilot Code Quality research | https://devclass.com/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/ | Secondary (gitclear.com returned 403) | 211 million lines analysed; blocks with 5+ duplicated lines increased 8x during 2024; 39.9% decrease in moved lines. |
| 5 | 9 | Digital Personal Data Protection Act, 2023 (No. 22 of 2023), Gazette of India, 11 Aug 2023 | https://www.indiacode.nic.in/bitstream/123456789/22037/2/a2023-22.pdf (copy read: https://www.trai.gov.in/sites/default/files/2024-09/DPDT_11082024.pdf) | Primary | s.8(5): "A Data Fiduciary shall protect personal data in its possession or under its control ... by taking reasonable security safeguards to prevent personal data breach." s.8(6): on a breach, "give the Board and each affected Data Principal, intimation of such breach". s.10(2): Significant Data Fiduciary appoints a DPO and "an independent data auditor", and undertakes periodic Data Protection Impact Assessments and periodic audits. |
| 6 | 9 | Hogan Lovells, "India's Digital Personal Data Protection Act 2023 brought into force", 17 Nov 2025 | https://www.hlc.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force- | Secondary | DPDP Rules notified 13 Nov 2025; Rules 1, 2, 17-21 effective immediately; Rule 4 from 13 Nov 2026; Rules 3, 5-16, 22, 23 (including security safeguards and breach intimation) from 13 May 2027. |
| 7 | 9 | RBI, (Non-Banking Financial Companies – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026, RBI/DoS/2026-27/461, 31 Jul 2026 | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13592 | Primary | Effective immediately. Para 21(6): maker-checker, "transactions are completed only after independent verification and approval by at least two individuals". Para 21(8): audit trails for IT assets. Para 41: board-approved change management policy. Para 155: earlier IT Framework and IT Governance directions for NBFCs repealed. |
| 8 | 9 | KPMG India, "RBI's technology focused master directions issued on 31 July 2026", 1 Sep 2026 | https://kpmg.com/in/en/insights/2026/09/rbis-technology-focused-master-directions-issued-on-31-july-2026.html | Secondary | The directions are entity-wise and became effective immediately. |
| 9 | 11 | Jerry Gamblin, "2025 CVE Data Review", 1 Jan 2026 | https://jerrygamblin.com/2026/01/01/2025-cve-data-review/ | Primary (independent analyst) | 48,185 CVEs published in 2025, up 20.6% from 39,962 in 2024 (rejected CVEs excluded). |
| 10 | 11 | GitHub Blog (Jonathan Evans), "A year of open source vulnerability trends: CVEs, advisories, and malware", 26 Mar 2026 | https://github.blog/security/supply-chain-security/a-year-of-open-source-vulnerability-trends-cves-advisories-and-malware/ | Primary | 69% increase in published malware advisories in 2025 compared with 2024. |
| 11 | 11 | Microsoft Security Blog, "Mitigating the Axios npm supply chain compromise", 1 Apr 2026 | https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/ | Primary | On 31 Mar 2026, malicious Axios versions 1.14.1 and 0.30.4 added a dependency whose install hook downloaded an OS-specific remote access trojan; the Windows RAT could run arbitrary PowerShell and enumerate files. |
| 12 | 11 | The Hacker News, "PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws", 21 Oct 2026 | https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html | Secondary (news) | CVE-2026-109618 and CVE-2026-109619 (CVSS v4 9.2) let "an attacker without an account run code on a web server"; affect "nearly every PHP version back to PHP 5.4". No share of servers is given; the author's "70% of PHP servers" could not be sourced and was left out. |

## Still open

| # | Sec | What | Note |
|---|-----|------|------|
| A | 9 | DPDP Rules commencement dates (most operational rules from May 2027) | Confirmed by the author on 2026-10-31. Source: Hogan Lovells (row 6). I have not checked the Gazette notification itself. |
| B | 9 | Which entity-wise RBI direction applies to the author's context | Dropped by the author on 2026-10-31. The NBFC version stays as an example only. |
| C | 7 | A source that measures test coverage or regressions in AI-assisted code directly | None found; the essay says the data does not measure tests directly. The 2025 DORA report reportedly reversed the throughput finding, but that is not checked and not used. |
| D | 11 | Open source incident examples | Done 2026-10-31 (rows 11 and 12). |

## Considered and not used

- RBI Master Direction on IT Governance, Risk, Controls and Assurance
  Practices (7 Nov 2023). The 2026 NBFC directions (row 7, para 155) repeal
  the earlier IT governance directions for NBFCs, though they do not name
  the 2023 direction. The essay cites the 2026 directions instead.
- RBI outsourcing directions. These were reportedly replaced by entity-wise
  "Managing Risks in Outsourcing" directions in Nov 2025. I only found
  secondary sources, so the essay leaves them out.

## Links to the author's earlier posts

Added 2026-10-31. Every quoted or paraphrased line was checked against the
post in `_posts/`. The links use `{% post_url %}`, so the build fails if a
post is renamed.

| Ch | Post | What the essay draws from it |
|----|------|------------------------------|
| 1 | 2026-05-06-Solo-to-multi-layerd-machine | The author's path from sole developer to a layered organisation |
| 1, 7 | 2026-08-17-AI-Engineering-Judgment | "It has not made software cheap to run, secure, or own"; "Coverage percentage is not a strategy. Risk and cost of failure are." |
| 4 | 2025-07-12-devDocs | Code explains what, docs explain why |
| 4, 7 | 2025-09-13-PROTO | Plan and context in repo files (PROTO.md, TODO.md, context.md); "agents define expected outcomes first" |
| 4, 5, 9 | 2026-10-02-Agentic-SDLC | "Files are the only shared memory"; "Humans approve the irreversible, and the approval is committed ... pinned to the exact commit"; `git log --grep "Approved-By"` |
| 8 | 2023-12-11-MondayMotivationTech | "Purchase one unit of the instrument we are selling ... become a user of our platform" |
| 8, 10 | 2025-09-18-AI-Trap | Building outside one's domain; "Prototype illusion" |
| 9 | 2026-10-01-Superintelligence-Civilization | "The agent that places the order is not the one that approved it." |
| 10 | 2025-05-25-microservice | "actual execution demand, not speculative scalability" |
| 11 | 2023-07-19-IndiaFintech | "each vendor requires a new implementation that must be regularly maintained" |
| 12 | 2026-05-06-Solo-to-multi-layerd-machine | Manage transitions deliberately |
| 12 | 2026-09-20-Dont-Fear-AI-Learn-To-Engineer-With-It | "some roles will evolve. But that does not mean the end of engineering" |
| 13 | 2026-07-22-ownership | "Ownership cannot." |

Considered and not linked: AI-Depth (a candidate for ch 3 or 13), PLD
(ch 6 or 7), egoInSWDev, Aadhaar, EisenhowerMatrix, Decentralization.
