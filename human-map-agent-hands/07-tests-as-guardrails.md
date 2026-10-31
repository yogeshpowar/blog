---
layout: chapter
title: "7. Tests as Guardrails"
desc: "Human Map, Agent Hands · Chapter 7 of 13"
book: human-map-agent-hands
book_home: /human-map-agent-hands/
chapter: 7
permalink: /human-map-agent-hands/07-tests-as-guardrails/
---

For a long time, tests were treated as a cost of writing good code: useful,
admirable, and the first thing cut when a deadline came close. With agents,
that view needs to flip. Tests are no longer a by-product of the work. They
are **the most precise part of the map**.

A written specification says what we want in words. A test says it in a
form that a machine can check, every time, without getting tired or
generous. When an agent writes code, the tests are what turn "I think this
works" into "this demonstrably does what we agreed". Without them, an
agent's speed simply produces more unverified code, faster.

This is why I have come back to **test-driven development** as a practical
discipline rather than an ideal. Writing the test first, or having the
agent write it first and a person read it before any implementation
begins, forces the map to become concrete. A vague intent produces a vague
test, and a vague test is easy to spot in review. A precise test gives the
agent a clear target and gives the reviewer a short thing to read instead
of a long diff. It was a rule in
[PROTO]({{ site.baseurl }}{% post_url 2025-09-13-PROTO %}), my early
protocol for agentic coding: even in its lightest mode, agents define
expected outcomes first. In the statement download from [chapter 4]({{ '/human-map-agent-hands/04-map-and-control/' | relative_url }}), the first test
to write is the boundary: a customer asks for a statement and gets only
their own transactions, never anyone else's.

Different kinds of test guard different things. *Unit tests* guard the
logic of small pieces: a calculation, a validation, a state transition.
They are cheap and fast, and an agent can run thousands of them in the time
it takes a person to read one. *Integration tests* guard the joins: a
service talking to a database, a queue, or another service, in an
environment like the one described in the [previous chapter]({{ '/human-map-agent-hands/06-environments-and-observability/' | relative_url }}). *End-to-end
tests* guard what the customer actually experiences: a full path from a
screen through every service and back. Each layer catches mistakes the
others miss, and agents make all three cheaper to write and to run.

One rule matters more than any other here: an agent must not change a test
to make its own code pass **without a person agreeing**. It sounds obvious,
and in my experience it is one of the first things to go wrong. Faced with
a failing test, an agent will often conclude, quite reasonably from its
point of view, that the test is wrong. Sometimes it is. But a test is a
statement of intent, and *changing a test is changing the map*.

In our setup, code and unit tests are committed separately, and tests are
append-only. New behaviour gets a new test; an existing test is not quietly
rewritten. If a change genuinely needs an existing test to break, then by
definition it is not backward compatible, and it has to be flagged. The
simplest way to flag it is one engineers already know: bump the major
version under semantic versioning. *A broken test becomes a visible version
change, not a quiet edit.*

A second rule follows from the first: **coverage is not the goal; meaning
is**. Agents can generate tests that execute every line and check almost
nothing. A high coverage number can hide a test suite that would pass
against almost any implementation. I would rather have fifty tests that
each state a real business rule than five hundred that only prove the code
runs. As I wrote in [AI made coding cheap. Engineering judgment is what is
left.]({{ site.baseurl }}{% post_url 2026-08-17-AI-Engineering-Judgment %}),
coverage percentage is not a strategy; risk and cost of failure are. There is a simple way to check which kind you have: break the code
on purpose and see whether any test fails. Change a greater-than to a
greater-than-or-equal, or return an empty list where a full one is
expected. If the suite stays green, the tests were not guarding that line.
Tools for this practice, known as mutation testing, have existed for years.
Agents make it cheap enough to use routinely.

The industry data, though early and correlational, points the same way.
Google's [2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)
found that higher AI adoption went with an estimated 7.2% drop in delivery
stability. [GitClear's analysis](https://devclass.com/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/)
of 211 million changed lines found that blocks of five or more duplicated
lines became eight times more frequent during 2024, while moved lines, a
sign of refactoring, fell by about 40%. Neither study measures tests
directly. Both suggest that *more code, produced faster, needs stronger
guardrails, not weaker ones*.

Done well, tests also change what the reviewer has to read. When the tests
are agreed first and they pass, the review of the implementation can focus
on what tests are bad at: readability, security, performance, and whether
the design will survive the next change. That is a much better use of a
senior engineer's attention than checking whether the code adds up. And
the higher the risk tier, the more of the reviewer's attention should go to
the tests themselves, because in that tier the tests are the map.

Tests and environments together create something new: a system that almost
anyone on the team can exercise from end to end.
