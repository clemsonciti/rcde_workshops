# Storage on Palmetto

Palmetto provides three data spaces: home, scratch, and paid storage.

| NAME             | SIZE                  | DISK TYPE      | FILE SYSTEM | NETWORK CONNECTION | BACKUP                 |
| ---------------- | --------------------- | -------------- | ----------- | ------------------ | ---------------------- |
| `/home/{username}`          | 100GB per user        | HDD            | `zfs`       | ethernet           | yes |
| `/scratch1/{username}`      | 1933TB                | HDD            | `beegfs`    | IB, ethernet       | no                 |
| `/fastscratch/{username}`   | 168TB                 | NVMe           | `beegfs`    | IB, ethernet       | no                 |
| `/local_scratch` | 99GB - 2.7TB per node | HDD, SSD, NVMe | `ext4`      | internal           | no                 |
| `/zfs/{group}`   | Varies by owner       | HDD            | `zfs`       | ethernet           | yes |

## Home Storage

Every Palmetto user gets 100 Gb of storage space; this storage is backed up at the end of every day, and the backup is kept for 42 days. So if you accidentally delete a file that was created more than a day ago, we might be able to restore it. This storage is called *home directory*.

To see how much space you have left in your home directory, please type:

```bash
checkquota
```

Since most of you are new users of Palmetto, you should be using very little storage at the moment.

When you log into Palmetto, you end up in your home directory. To see which directory you are in, type

```bash
pwd
```

...which stands for "print working directory". It should give you something like

```
/home/<your Palmetto username>
```

## Scratch Storage

100 Gb might be enough for some, but for people dealing with extensive amounts of data that would not be enough. We also offer the access to *scratch space*, which is about 2+ Petabytes in total. Scratch space is not backed up; files that haven't been used for more than a month are automatically deleted (and cannot be restored). We strongly encourage people to use scratch space, but please be aware of its temporary nature. When you get anything that is worth keeping, please back it up, either in your home directory, or on your local machine.

To go to a scratch directory, or to any directory on Palmetto, use the `cd` ("change directory") command:

```bash
cd /scratch1/<your Palmetto username>
```

To go to your home directory, you can do

```bash
cd /home/<your Palmetto username>
```

:::{hint}
There is also a shortcut; to go to your home directory, you can simply type

```
cd
```
:::

## Local Scratch

Every Palmetto compute node has storage on the node itself and is referred to as `/local_scratch`. This scratch space can only be accessed by a job running on the node. The file system for `/local_scratch` has no hardware failure protection and is never backed up.

To access this space in your PBS script, use the `$TMPDIR` environment variable or the location `/local_scratch/pbs.$PBS_JOBID`. If you are using multiple nodes, further setup is required.

:::{warning}

Files in /local_scratch will be purged automatically when your job terminates. Copy files elsewhere before your job ends.
:::


:::{note}
Please don't use `/tmp` for temporary storage! Use `/scratch1` or `$TMPDIR`.
:::

## Storage Purchasing

We offer storage space on Palmetto for sale to faculty members, with the price of $150 per 1 terabyte. This storage is backed up just like your home directory. Please contact us if you are interested in buying storage.

## Performance Guidelines

Generally speaking, /local_scratch will always be the fastest file system to use because there is no network involved. However, this space cannot be shared between a group of nodes participating in a job, and the data must be moved to permanent storage before the job completes.

/scratch1 is a parallel file system that runs atop spinning disk drives and is best suited for workflows issuing sequential, large read or write requests. /fastscratch is also a parallel file system but runs atop NVMe flash drives and is best suited for workflows having small, random read or write access patterns. However, /fastscratch will also run well with any kind of sequential workload. Either system can handle large numbers of files and directories.

The Palmetto support team encourages you to test your workflows against all three file systems to see which one works best for you.

:::{admonition} Key Points
- Users get 100 Gb of backed-up storage in their home directories.
- Users also have access to more than 2 Pb of scratch storage.
- Scratch storage is not backed up, and files left unused for 1 month are deleted.
- Faculty can purchase backed up ZFS storage space.
:::
