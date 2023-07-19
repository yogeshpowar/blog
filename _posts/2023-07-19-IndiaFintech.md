---
layout: posts
title: "India Fintech Open Source Stack"
tags: Fintech India Open Source
desc: Why Indian Fintech Industry need a open source stack
---
When we started Orowealth, I remember that we used to collect wet
signatures for mutual fund KYC. There were human runners who would go door-to-door to
collect the signed documents. This later changed to signing on the screen and
then using Aadhaar-based e-signatures. Every other startup that emerged during that
time aimed to automate tedious manual tasks through online, digital-first
approaches. Now, this has become the industry standard, and not everyone writes
the code themselves; instead, they seek out vendors who have already solved this
problem and utilize their solutions.

So every new technology of the past has become a standard and indispensable step
in future development.

Another way to look at this is first version fintech startups tried to break the
ice by providing non-conventional solutions like
1. eSign: (as explained above)
2. penny drop: Its actually rupee drop to identify if the user's bank name is
   matching with the name tagged to PAN.
3. PGs: Payment gateways to transfer money from user's account to sink's.
4. Aadhaar Auth: To authenticate user's Aadhaar
5. Mutual Fund Transactions: These are the APIs provided by the aggregators like
   MFU/BSE/NSE/MFU or individual AMCs
6. Stock/Broker/Exchange APIs: These are the APIs provided by the online brokers
   and banks
7. Prices/Nav APIs: Daily/hourly/live asset prices
8. KYC: KYC registration agencies
9. SMS: For OTPs and authentications
10. Whatsapp: Its now default communication model for most fintechs in India.

And so on.

To create a comprehensive online platform for an instrument, one typically needs
to incorporate approximately 10 or more vendor implementations. Each vendor has
its own unique authentication and onboarding processes. Many vendors still rely
on conventional data format stacks and protocols. For instance, despite the
prevalence of REST and JSON in the industry, there are still numerous vendors
who utilize XMLs and WSDLs.

Besides, due to the absence of a common protocol and data format, each vendor
requires a new implementation that must be regularly maintained. It is quite
common for vendors to change their protocols and formats.

In many cases, startups that serve as vendors may struggle due to insufficient
funding or an inability to find a viable business model.

As a result, every new vendor has to start from scratch, working on compliance,
onboarding, implementation, testing, and automation.

When looking at an individual company's perspective compared to the market as a
whole, one might argue that overcoming these barriers or eliminating competitors
is the key. However, in this pursuit, companies (specifically the investors who
supported the idea or problem) eventually lose momentum. Out of 100 companies
registered in a similar domain, only 4 or 5 will remain active after 4 years.
The remaining 95% will fail. This is not meant to criticize failure, but rather
to highlight that these companies have no lasting legacy to carry forward.
Nearly all of them would have allocated a significant portion of their tech
budget to these vendor integrations.

Many would have vendor lock-in; it refers to a situation in which a customer
becomes heavily dependent on a particular vendor's products or services, making
it difficult or costly to switch to an alternative vendor. This dependency
arises due to various factors, including proprietary technologies, data formats,
APIs, and contractual agreements that bind the customer to the vendor's
ecosystem.

To mitigate the risks of vendor lock-in, organizations often rely on an
abstraction layer. An abstraction layer acts as an intermediary between the
underlying vendor-specific technologies and the business logic or applications
that utilize those technologies. It provides a standardized interface that
shields the higher-level components from being tightly coupled to the vendor's
implementation details.

Hence there is a need of abstraction layer for every vendor integration.

What if these abstraction layers and created and managed by a neutral entity;
say a not-for profit, section-8 company with Open protocol and Open data format?

<a href="/blog/assets/images/openFinTech.png"> <img
src="/blog/assets/images/openFinTech.png" > </a>

1. It will allow organizations to decouple their applications from the underlying
   vendor-specific technologies.
2. An abstraction layer will promotes interoperability and portability. Ie.,
   switch-in between the vendors will then be a offline task.
3. Since code is open sourced, individuals can take the development further
   without a single point of failure.

That way, the 95% companies which are going to fail, would have contributed to
this open model and their legacy or contributions will remain.

More important, every startup (new/old) rather than fixing the same operating
problems can focus on the core industry problem and take the ecosystem on next
level and thus achieving their goals and taking the solutions to next million or
billion.
