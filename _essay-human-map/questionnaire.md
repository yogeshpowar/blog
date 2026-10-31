# Questionnaire: "Human Map, Agent Hands"

Answer in your own words after each **Answer:**. A few lines is plenty. I
will turn your answers into prose in your voice and show you every change.

**How to answer**

- Leave an answer blank to skip it. Write **cut** to remove that part of
  the essay. Write **ok** to confirm a claim as it stands.
- Questions marked *(optional)* can be skipped without leaving a gap.
- Keep everything qualitative and anonymised: no company figures, no names
  of products, vendors, internal projects, or people, and no regulator in
  the compliance story. If an answer needs something sensitive for context,
  mark it **[private]** and I will use it only to shape the wording.

There are 59 questions, but most need only "ok" or a line. The 12 that
matter most are marked ★. Answering those alone fills the biggest gaps.

---

## General

**G1.** Title. Keep "Human Map, Agent Hands"?
Answer: DONE (2026-11-01). Kept, with the new subtitle.

**G2.** Publication date (for the post file name and front matter).
Answer:

**G3.** Tags. Suggested: `AI agents engineering fintech SDLC`. Change?
Answer:

**G4.** ★ The brief says you approved an earlier closing for chapter 13. Do
you still have it? If yes, paste it here or give the path.
Answer: ANSWERED (2026-10-31) with your path; added to chapter 13.

**G5.** The essay mostly says "people" (for example "people accept the
risk"). Your brief says "humans". Which do you prefer throughout?
Answer:

---

## 1. Why Now

**1.1** ★ One concrete example from your own work of something that used to
take weeks and now took hours or days. What it was (generically), roughly
how long before, and how long now.
Answer: DONE (2026-10-31). The bot-protection CAPTCHA fix across backend and
frontend, built with an agent and shipped through the standard process.

**1.2** What did you mean by "challenges are more open as the landscape
changes"? The draft reads it as "no settled answers any more" and
"problems that needed a large team are now within reach of a small one".
Answer: DONE (2026-10-31). Reading confirmed; this is why the team
introduced pods (a couple of devs, a PM, and a QA).

**1.3** The draft reconciles the METR study (experts 19% slower) with your
view by saying the studies measured experts in familiar code, while the big
change is getting a first version in unfamiliar territory. Does that match
your experience?
Answer:

**1.4** New idea: failure is cheap in time, but not in attention or trust.
Keep or cut?
Answer:

---

## 2. Three Kinds of Teams

**2.1** *(optional)* Where were your own teams on the orthodox, agent-skeptic,
fully agentic line when you started?
Answer: DONE (2026-10-31). Seen all three; stories used in chapter 3.

**2.2** Confirm: "In my experience, [agent-skeptic] is the most common
pattern."
Answer:

**2.3** I removed two lines because they claimed experiences you had not
given me: talking to other engineering leaders about this, and learning
from watching fully agentic teams. Is either true? If so, describe it.
Answer:

**2.4** The "three questions" self-test (who wrote it, who checked it, who
decided it could go live). Keep it in chapter 2, or move it later?
Answer:

---

## 3. Where Each Kind of Team Breaks

The brief asks for real experiences here. One short example per team type
is enough. If you have none for a type, write **none** and I will remove
that placeholder.

**3.1** ★ Orthodox: a time a slow, careful process held back a good idea.
Answer: DONE (2026-10-31). Man-days, whiteboard, trackers gave up, no excitement.

**3.2** ★ Agent-skeptic: review queues growing, or uneven adoption within a
team.
Answer: DONE (2026-10-31). Managers/PMs build too; unreviewable code never
shipped; mandatory PRD review with reviewers involved at design.

**3.3** ★ Fully agentic: agent output that passed every check but missed
what was actually intended. From your teams or from peers.
Answer: DONE (2026-10-31). Peripheral project built fully agentically; changes meant starting from zero.

**3.4** I softened two claims. Should either go back to the stronger
version? (a) "Good engineers who want modern tools start to leave."
(b) "The honest reviewers admit they are skimming."
Answer:

**3.5** The "symptom" lines for each team type. Are they right?
Answer:

---

## 4. The Map and the Control

**4.1** *(optional)* How do your teams write the map today: a spec, a ticket
template, a design note, a checklist?
Answer: DONE (2026-10-31). PRDs, then agent-written PRDs, then committed
prompts, then explaining in person.

**4.2** Does having a map actually change review for you, turning it into
"checking a claim"? Or does review still end up being about the code?
Answer: DONE (2026-10-31). Yes: reviewers now join at design (chapter 3 story).

**4.3** The example map (statement download as a PDF). Keep, change the
example, or cut?
Answer:

**4.4** Confirm both: "agents are now very good at the hands and still
unreliable at the map" and "writing a good map is harder than writing the
code was".
Answer:

---

## 5. Autonomy by Risk

**5.1** *(optional)* How do your teams classify a few typical changes?
Describe them generically.
Answer: DONE (2026-10-31). Autonomy by environment; none in production yet.

**5.2** The scoring rule (1 to 3 per axis, add them up). Useful, or too
mechanical?
Answer:

**5.3** "Reversibility is about the failure, not the change." Does that
match how you classify risk?
Answer:

**5.4** Confirm: "most of a typical codebase is not in the dangerous
corner".
Answer:

---

## 6. Environments and Observability

**6.1** Which local Kubernetes tool do you use (kind, k3d, minikube, other)?
Name it in the essay, or keep it generic?
Answer: DONE (2026-10-31). Keep it generic.

**6.2** Which Grafana stack components do you run locally (for example
Grafana, Prometheus or Mimir, Loki, Tempo)?
Answer: DONE (2026-10-31). Grafana.

**6.3** "Measure before, change, measure after." Do your agents do this
today, or is it a proposal? The essay should say which.
Answer:

**6.4** Can your agents query metrics, logs, and traces directly today?
Answer: PARTLY (2026-10-31). Requests are traced locally; agent querying not yet confirmed.

**6.5** Confirm: the cost of maintaining these environments is "smaller than
the cost of giving agents autonomy without senses".
Answer:

---

## 7. Tests as Guardrails

**7.1** How do you stop agents from changing tests without a person
agreeing? For example: code owners on test folders, a separate review, or a
check that flags edited assertions.
Answer: DONE (2026-10-31). Separate commits, append-only tests, major semver
bump for a breaking test.

**7.2** Do your teams use mutation testing (breaking the code on purpose to
check the tests)? If not, I will present it as a suggestion.
Answer:

**7.3** Confirm both: "I have come back to test-driven development" and
"in my experience [agents changing tests] is one of the first things to go
wrong".
Answer:

---

## 8. Who Can Test the Whole Path

**8.1** *(optional)* A time a non-engineer on your team found or reproduced
an issue by running the system themselves.
Answer: DONE (2026-10-31). QAs test on shared servers; anyone logs issues;
curious ones add analysis.

**8.2** Confirm: "In most teams I have worked with, testing the whole path
was a specialist job."
Answer:

**8.3** Do journeys that people check by hand become end-to-end tests on
your teams, or is that a suggestion?
Answer: Suggestion for now (QAs have no local setup yet).

---

## 9. Regulation and the Audit Trail

**9.1** Which RBI entity-wise directions, if any, apply to your context? The
essay uses the NBFC version only as an example and will not name your
company. This answer can be **[private]**.
Answer: REMOVED (2026-10-31). The NBFC version stays as a generic example.

**9.2** *(optional)* Have you used agents to find compliance gaps (for
example personal data in logs, retention rules not implemented)?
Answer: DONE (2026-10-31). Agents asked to act as CISO, VAPT tester, infosec.

**9.3** Confirm: "compliance teams recognise [maker-checker] quickly when
it is described this way".
Answer:

**9.4** The paragraph on agents as part of the data flow (code and logs
sent to a model provider). Keep, expand, or cut?
Answer:

**9.5** Confirm the closing line: "The more common reason [to slow down], in
my experience, is that the thing should not have been built at all."
Answer:

---

## 10. What Not to Build

The compliance story. Keep it qualitative. Do not name the product, the
market, or the regulator.

**10.1** ★ What state was the work in when it reached compliance? For
example: nearly finished, in testing, ready to launch.
Answer: DONE (2026-10-31). Ready for production with a closed user group (CUG).

**10.2** ★ Why was it blocked, in general terms? (The old draft guessed "it
could not be offered under the rules that applied to it". Is that right?)
Answer: CONFIDENTIAL (2026-10-31). The essay says the reasons cannot be shared.

**10.3** *(optional)* What happened afterwards: how the team felt, what was
salvaged, what changed.
Answer: REPLACED (2026-10-31) by a second story: internal product not used.

**10.4** ★ Confirm or correct: "Today, the first artefact for anything new is
the map, not the code, and compliance sees that map before an agent writes
a line."
Answer: DONE (2026-10-31). Confirmed.

**10.5** "You cannot tell which one is the tenth by looking at it", so the
defence is cheap, early tests of the customer, partners, rules, and running
cost. Does that match how you think?
Answer:

**10.6** Confirm: asking an agent to argue against an idea is "more useful
than asking it to agree with me".
Answer:

**10.7** The two habits ("smallest thing that answers the question" and a
kill criterion in the map). Your practice, or suggestions?
Answer:

---

## 11. The Costs Nobody Budgets For

**11.1** ★ How has the cost of running the platform under strict rules felt
as it grew? Qualitative only, no figures.
Answer: SKIPPED (2026-10-31).

**11.2** ★ *(optional)* A time someone had to debug agent-written code that
nobody fully understood.
Answer: DONE (2026-10-31). Ex-employee black-box modules; agents now read them.

**11.3** Confirm: open source security issues are "one of the largest
sources of unplanned work" for an engineering team.
Answer:

**11.4** Do you want one or two dated news examples of open source security
incidents? If yes, I will find and verify them.
Answer:

**11.5** The six costs are each in bold. Keep the bold, or switch to italics?
Answer:

---

## 12. Adoption

**12.1** ★ Where are your teams on the four stages today, and what was harder
than expected?
Answer: PARTLY DONE (2026-10-31). Stage 3 for production, further along below
production. "Harder than expected" removed at your request.

**12.2** *(optional)* A step your teams paused or took back, and why.
Answer: REMOVED (2026-10-31).

**12.3** "A team that adopts agents this way builds its audit trail as it
goes." Is that true in your experience, or still a hope?
Answer:

**12.4** Confirm: "evidence from a colleague persuades engineers more than
advice from leadership does".
Answer:

---

## 13. The Hard Picture

**13.1** The essay ends on "what not to build". The maker-checker line
("makes the checker more important, not less") could be the last image
instead. Which do you want to end on?
Answer:

---

## Anything else

Anything the essay gets wrong, misses, or overstates?
Answer:
