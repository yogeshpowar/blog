---
layout: posts
title: Slash does matter
tags:  IITB Random
desc: Why one must be conscious while using `rm` command with files with leading `/`
---

# Slash does matter

Like my other friends, I also wanted to improve my CPI. Improve. Yes, the previous semester, unlike others, CPI was my last preference. Things like Maddu, Footer, H12's google, BB , Mahalaxmi , Staff C, 85 and Andheri had a higher precedence. This semester was going well except OOS. Just before the mid semester exam we (I, Anya and himya) had an excellent fight plan for OOS preparation for the exam. But Jaya spoiled our plan. Jaya is he and not she. There is a reason for throwing light on this point. Once I was also confused about those two. One night it was 3 in the morning and I hurriedly went to the hostel to get some quick sleep but after reaching in front of 85's door I found that the room was locked. So I called Jaya, my roomi and started my conversation with some four letter words because he did not keep the key on the locked door. And Hence he had performed an act of protocol violation. But then instead of male voice I heard a female voice coming from the other side of the phone line. Mistake. The callee was not a Jayesh Aka jaya but Jaya, Suhas's GF; phone book entry jaya had ambiguity which i failed to resolve. Hmmmm, that call became my last call to her.

So He-Jaya spoiled our plan of preparation for OOS midsem. He said OOS is uncatchable for midsem and instead utilizes its time for other subjects like applied economics. We were carried away by our well trusted friend and went to OOS midsem without preparation and like everytime the magic did not happen. We all had an expected result; percentage numbers were smaller then single digit number 5.

This way course projects and end sem became my only hope for grade improvement. Yesterday we some how completed the submission of applied eco's project. Today we were about to finish QoS's project and then day after tomorrow it was OOS's project on the top of queue.

My project partner & I gave a full fight to meet the deadline for the QoS project. Work had also got some good pace. We just wrote some scripts to fetch packets from some network machine and capture the system performance in well defined output. To make the code look neat I decided to put the output files in a directory named dev. So I created a directory named 'dev' under the current directory. I also thought of checking the scripts one more time, so then I had to delete the contents for the dev directory. The command `rm -f dev/*` would have done its work fine so typed `rm -f /dev/*`. Enter. And boom. A very big mistake. All the files under '/dev' instead of 'dev' directory were deleted.

I was then freezed. My partner was more horrible than mine. Her mouth and eyes were wide open and neither she uttered a word nor she moved her neck for 2 minutes. Finally I force rebooted the machine to install and configure new fedora core four on it; without trying to make a simple eye contact with my project partner. Obviously such expressions were expected from any normal person who's 15 days work was gone to null in just a single key hit.

Well luckily the machine was brought up in just 4 hours with as good configure as before the confusion of dev and slash dev.

I will never forget those looks. Period.

---
Published on 01/07/2007
