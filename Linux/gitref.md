# How git ref saved my day

**git format-patch HEAD^**  
**scripts/checkpatch.pl 0001-...**  
Found some problem  
Fixed it; haven't committed yet  
**git diff > a.diff**  
**git-reset --hard HEAD^**  
then replaced the diff with the diff in the patch 0001-...  
**git-am 0001-...**  
  
Ooh :O I lost the original 0001-... patch and replaced it with delta fixes.  
  
How to recover the patch? Is it waste of a day's work?  
  
Which FS ? ext3 ok. Google about recovering ext3.  
Ok there is something called as ext3grep; which says  
"Do not attempt to use ext3grep for recovery from a mounted filesystem. Ever."  
  
Unmounted the FS.  
Downloaded the source ext3grep. ./configure, make and make install.  
  
**ext3grep --dump-name /dev/sda5**  
It took a while to scan 183 groups to report its useless :(.  
  
Then thought of Linus and typed "recovering git-reset --hard" to find the solution  

> **\[root@pe-lt345 sjay\]# git reflog**  
> e6b0b9d HEAD@{0}: HEAD^: updating HEAD  
> 9c73133 HEAD@{1}: commit:  
>   
> **\[root@pe-lt345 sjay\]# git reset --hard 9c73133**

  
I Love git.

---

08/02/2012
