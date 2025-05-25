---
layout: posts
title: "Microservice Hell"
tags:  Tech
desc: When Good Intentions Go Bad 
---

I was reviewing the code for a new product the other day,  a fresh module built by a new developer who had just joined our team. That’s when I first saw it.

There were five top-level routes:  `/users/`, `/orders/`, `/products/`, and a couple more, and each one had its own dedicated microservice. The codebase looked more like a distributed system diagram than a backend project. That's when it hit me: this developer had unknowingly stepped right into **Microservice Hell**.

There's a widespread misconception, especially among newer developers, *that microservices are the ultimate destination for backend systems*. But microservices aren't some kind of architectural silver bullet. In fact, *they’re not even free*.

Every new service you spin up comes with a hidden tax. That cost shows up in the form of:

* Infrastructure overhead: More services, more containers, more servers.
* Deployment complexity: CI/CD for each service, versioning, coordination.
* Increased monitoring and logging: Distributed logs and tracing are hard.
* Heavier DevOps burden: More moving parts = more things to break.

It doesn't stop there. The real killer in microservice-heavy systems is **inter-service communication**. What used to be a function call in memory now becomes a network call ; inherently slower, less reliable, and more complex.

And now you're dealing with:

a. Latency due to network hops
b. Retry logic and exponential backoffs
c. Timeouts and circuit breakers
d. Debugging across multiple logs and services

And all this, **before your product even has real users**.

What makes this worse is that many of these splits were made on **hypothetical grounds**, like "We might want to scale this independently later." That's dangerous thinking.

Partitioning should be based on **actual execution demand**, not speculative scalability. Good reasons to split services include:

1. You've hit a real *performance bottleneck*
2. You need *independent deployments*
3. There are *clear team ownership boundaries*
4. The module reflects a *well-defined domain* with minimal coupling

Premature splitting leads to fragmentation, redundancy, and long-term architectural pain.

### Start With a Modular Monolith

Instead, I suggest for starting with a **modular monolith** - one codebase, cleanly organized into internal modules.

You can always split modules into services later when:

* They *need to scale independently*
* A *separate team* needs to own them
* They've matured enough to become *stable standalone units*

This gives you all the benefits of good design without paying the upfront cost of full-blown microservices.

### BTW, Optimization is a Day 2 Problem

As I always keep saying,  *optimization is a Day 2 problem*. First, make it work. Then, make it fast or scalable.

Why listen to me? Here’s Elon Musk saying it better:

> *"You know, in general with any given technology, first try to make it work and then you make it efficient."*
> — [Elon Musk](https://www.youtube.com/clip/UgkxAoAXDGgYHQ_3V4eteMn25yWlHYRC3EvD)

So before you break your monolith into a zoo of services, make sure you actually have a reason - one grounded in today's reality, not tomorrow's speculation.

Happy Coding.
