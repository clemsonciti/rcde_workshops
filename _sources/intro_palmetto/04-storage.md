# Storage on Palmetto
questions:
- "How and where can I store my files?"
teaching: 15
exercises: 0
objectives:
- home directory, scratch space
keypoints:
- "users get 100 Gb of backed-up storage in their home directories"
- "they also have access to more than 2 Pb of scratch storage"
- "scratch storage is not backed up, and files left unused for 1 month are deleted"

Every Palmetto user gets 100 Gb of storage space; this storage is backed up at the end of every day, and the backup is kept for 42 days. So if you accidentally delete a file that was created more than a day ago, we might be able to restore it. This storage is called *home directory*.

To see how much space you have left in your home directory, please type:

~~~
checkquota
~~~
{: .bash}

Since most of you are new users of Palmetto, you should be using very little storage at the moment.

When you log into Palmetto, you end up in your home directory. To see which directory you are in, type 

~~~
pwd
~~~
{: .bash}

...which stands for "print working directory". It should give you something like

~~~
/home/<your Palmetto username>
~~~
{: .output}

100 Gb might be enough for some, but for people dealing with extensive amounts of data that would not be enough. We also offer the access to *scratch space*, which is about 2+ Petabytes in total. Scratch space is not backed up; files that haven't been used for more than a month are automatically deleted (and cannot be restored). We strongly encourage people to use scratch space, but please be aware of its temporary nature. When you get anything that is worth keeping, please back it up, either in your home directory, or on your local machine.

To go to a scratch directory, or to any directory on Palmetto, use the `cd` ("change directory") command:

~~~
cd /scratch1/<your Palmetto username>
~~~
{: .bash}
 
To go to your home directory, you can do

~~~
cd /home/<your Palmetto username>
~~~
{: .bash}

There is also a shortcut; to go to your home directory, you can simply type

~~~
cd
~~~
{: .bash}

NOTE: please don't use `/tmp` for temporary storage! Use `/scratch1` or `$TMPDIR`.
