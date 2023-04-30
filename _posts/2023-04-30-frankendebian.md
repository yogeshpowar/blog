---
layout: posts
title: "FrankenDebian"
tags:  debian gnu linux
desc: Dont make a FrankenDebian
---

Recently came to know about a project called as [Prav](https://prav.app/) who
are building a messaging app without a [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in). 
Think of this as ethical in-place replacement for whatsapp.
What was more exciting about this project is the group involved in building
it by registering a Multi State Cooperative Society in India. Please
support this project by [becoming a member](https://prav.app/become-a-member/).

1. Prav is fork of [Quicksy](https://quicksy.im/)
2. Quicksy is a fork of [Conversations](https://conversations.im/)
3. Conversation is based on Jabber/XMPP protocol
4. [XMPP](https://en.wikipedia.org/wiki/XMPP) is open protocol for instant
   messaging and much more. XMPP address has format
   _username@servername/resource_. This allows user to communicate without
   sticking to same server/domain.

There are many xmpp servers with open registration, where people can
register. e.g., `yap@disroot.org` is my xmpp id created on
[disroot.org](https://disroot.org).

Anyways, this blog is about how I broke my stable Debian and how I fixed it.

There is [dino-im](https://dino.im/) Debian package for XMPP client for desktop
and I installed it and used it for a while to find newer features like emojis 
or smileys or quotes are present in the newer version of dino-im. So I thought
of installing just the dino-im from the testing release, Bookworm.

And my browsers stopped working.

Uninstalling dino-im didn't work. And this state of Debian is called as
**FrankenDebian**. In fact
[https://wiki.debian.org/DontBreakDebian](https://wiki.debian.org/DontBreakDebian)
lists it at first place as an advice for Debian users on not breaking the
system.

The following are the sequence of events that led to me fixing it.
1. Upgraded my current stable to latest stable (Bullseye)
2. Reinstalled the browsers (Brave, Firefox and Chromium) and none of them worked.
3. Konqueror browser came for rescue
4. Dist-upgraded stable to testing. Bullseye to Bookworm. But even that didn't
   fix the browser problem.
5. Installed a fresh Bookworm on a fresh small partition of 8 GB and chroot to it.
6. Studied the libraries used on dist-upgraded and newly installed Debian
    - dist-upgraded
```
$ ldd /usr/bin/firefox-esr
	linux-vdso.so.1 (0x00007fff2d9cc000)
	/usr/local/lib/AppProtection/libAppProtection.so (0x00007f7fcca00000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f7fcc600000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f7fccc49000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f7fcc81f000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f7fccd25000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f7fccc44000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f7fccc3d000)
	libX11.so.6 => /lib/x86_64-linux-gnu/libX11.so.6 (0x00007f7fcc4be000)
	libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f7fcc494000)
	libXi.so.6 => /lib/x86_64-linux-gnu/libXi.so.6 (0x00007f7fcc480000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f7fcc3a1000)
	libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6 (0x00007f7fccc36000)
	libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f7fcc000000)
	libXext.so.6 => /lib/x86_64-linux-gnu/libXext.so.6 (0x00007f7fcc38c000)
	libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007f7fcc376000)
	libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0 (0x00007f7fcc369000)
```
	- New installed one
```
# ldd /usr/bin/firefox-esr
	linux-vdso.so.1 (0x00007ffda11c2000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f3bfc000000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f3bfbfe0000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3bfbdff000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f3bfc2d8000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f3bfbd20000)
```
8. Searched about the first mismatched library which has come from `Citrix
   Workplace`
9. [Uninstalling
   Citrix](https://docs.citrix.com/en-us/citrix-workspace-app-for-linux/install.html#to-uninstall-citrix-workspace-app-on-debianubuntu-operating-systems)
   solved the browser problem.

Key take aways from this incident are
1. Must read [Dont Break Debian](https://wiki.debian.org/DontBreakDebian)
2. We often back the user data and ignore the OS data thinking new installation
   would be easy. But configuring the OS is equally hard as it current OS is
   evolved as per the needs from the past. So keep backup of OS.

Good to be on the next-stable now and long live the _bookworm_.
