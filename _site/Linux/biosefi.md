#  Ubuntu on Lenovo G505s

A friend of mine wanted my help on installing Gnu/Linux on one of his new
laptops. He had already installed _Windows 7_ on it and tried installing
_Ubuntu_ on it which had consistently failed to boot in normal or rescue mode.


After doing some research on the Internet, I found that people have faced
similar problems using similar hardware. I tried a fresh installation of
_Ubuntu_ _14.04_ (the latest) and it showed the same behaviour. That is **_no
activity on screen after loading initrd._** The same behavior was seen even for
_Archlinux_.


All this time I was trying to boot using the BIOS method. Some post on the
Internet have mentioned correct working of _Ubuntu_ provided one use _EFI_
method. _UEFI_ method requires _EFI partition_ which is a _DOS FAT32_ and
requires _GPT_ formatted disk.

It was clear then that disk would be reformatted. All I had to do was to boot
the machine using _EFI_ method and then _Ubuntu_ installation would be taking
care of the rest. Eventually it did but by removing entire data from disk
without giving me any warning. And it stupidly took all the share of the disk by
keeping 500MB for the EFI partition and the remaining 1 TB for itself.


Live _Ubuntu_ CD again came for the rescue.

I had to fix it by first resizing the _EXT4_ using _resize2fs_ and then fixing
the partition table using the _parted_ to match the partition size with that of
file systems. To know file system size, used _dump2fs_ to find block count and
multiplied it by block size. Then created a few more partitions for swap and etc
using parted; _fdisk_ doesn't work on GPT disks (why?)


Formatted the newly created swap partition using _mkswap_ and fixed the
_/etc/fstab_ file with its correct _UUID_ and rebooted the machine to see the
_Ubuntu 14.04_ up and running.


**Happy hacking**.

---

Updated On: 9 Aug 2014

