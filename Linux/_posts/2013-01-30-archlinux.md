---
layout: posts
title: Archlinux to save good old Ubuntu
tags: GNU/Linux OS
desc: Notes on recovering Ubuntu using Archlinux
---

# Archlinux to save good old Ubuntu

I had an old machine (Intel P4 processor, Intel D845GBV motherboard) which was
not under use for a long time. When I assembled all the parts together to find
machine doesn't boot. It's RAM was gone. Had to buy a new DDR-I type 512 MB but
it was much much cheaper than the older one. I got older one for 1200 Rs per 256
MB and latest one for just 430 Rs for 512 MB

Whatever, after replacing the memory machine still did not boot reason was bad
MBR of HDD (Seagate Baracuda 40GB).

Its a machine which was bought in year 2002. Windows XP was only OS that was
being used untill in 2006 I started using Ubuntu for total replacement to
Windows.

This is year 2013 and I have moved from Ubuntu to Archlinux (and Parabola) over
these last 7 years.

This is how I recovered Ubuntu using Archlinux's live rescue disk.

1. Boot using Rescue disc Archlinux
2. find old root partition using `fdisk -l` eg., /dev/sda8 (as it was mine)
3. `mount /dev/sda8 /mnt`
4. `mount -o bind /dev /mnt/dev`
5. `mount -o bind /sys /mnt/sys`
6. `mount -t proc /mnt/proc`
7. `chroot /mnt /bin/bash`
8. Type `mount` to see where is / mounted from.
   It was showing  /dev/hda8 in the mount and hda8 is not a valid device. Where
   as `fdisk -l` has mapped /dev/sda8 with mounted location. Issue was becase
   /etc/mtab.
9. Edited /etc/mtab to mount /dev/sda8 to / instead of /dev/hda8.
   Just before grub-install /dev/sda, I got warning about /dev/sda not being
   BIOS drive. This was because /boot/grub/device.map had still hda into it.
10. Edited /boot/grub/device.map to replace hda to sda.
11. `grub-install /dev/sda  `

Make sure that changes to /boot/grub/device.map and /etc/mtab are undone.

And old ubuntu is up.

This post is made from my good old Ubuntu  :)

```
limejuice@zampaktu:~$ cat /etc/issue  
Ubuntu 6.06 LTS \\n \\l  
```

```
limejuice@zampaktu:~$ cat /proc/cpuinfo  
processor       : 0  
vendor\_id       : GenuineIntel  
cpu family      : 15  
model           : 1  
model name      : Intel(R) Pentium(R) 4 CPU 1.70GHz  
stepping        : 2  
cpu MHz         : 1700.129  
cache size      : 256 KB  
fdiv\_bug        : no  
hlt\_bug         : no  
f00f\_bug        : no  
coma\_bug        : no  
fpu             : yes  
fpu\_exception   : yes  
cpuid level     : 2  
wp              : yes  
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm  
bogomips        : 3402.39  
```

Happy Hacking.

---

Updated on: 30/01/2013
