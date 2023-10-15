# Storage on Picotte

Picotte storage hardware includes
- Parallel Scratch Storage
  - Dell EMC/BeeGFS Solution for HPC	
  - 175 TB usable capacity aggregate 44 GB/s read, aggregate 41 GB/s write
- Persistent Storage
  - Dell EMC PowerScale Isilon scale-out storage	(Potentially PHI Compliant, talk to us for more details)
  - 649 TB usable capacity
  - 10 Gbps Ethernet
- Node-local scratch storage
  - 854 GB 12 Gbps SAS SSD (per node)	 
- Network Fabric	
  - 4X HDR Mellanox InfiniBand connected at 100 Gbps
  - 10 Gbps Ethernet

Picotte provides three data spaces: home, scratch, and paid storage.

| NAME                      | SIZE            | DISK TYPE  | FILE SYSTEM | 
| ------------------------- | --------------- | ---------- | ----------- | 
| `/home/{username}`        | 64GB per user   | HDD        | `isilon`    | 
| `/beegfs/scratch`         | 127TB (shared)  | HDD        | `beegfs`    | 
| `/local_scratch`          | 838GB           | HDD        | `ext4`      | 
| `/ifs/groups/{Grp}`       | Varies by owner | HDD        | `isilon`    | 

## Home Storage

Every Picotte user gets 64GB of storage space; This storage is called *home directory*.

To see how much space you are using in your home directory, please type:

```bash
cd ~
du -h -d -1
```

Since most of you are new users of Picotte, you should be using very little storage 
at the moment.

When you log into Picotte, you end up in your home directory. To see which directory you are 
in, type

```bash
pwd
```

...which stands for "print working directory". It should give you something like

```
/home/<your Picotte username>
```

## Scratch Storage

64 Gb might be enough for some, but for people dealing with extensive amounts of data that would not be enough. 
We also offer the access to *scratch space*, which is about 127TB in total. Scratch space is not backed up; files 
that haven't been used for more than a month are automatically deleted (and cannot be restored). We strongly 
encourage people to use scratch space, but please be aware of its temporary nature. When you get anything that is 
worth keeping, please back it up.

To set up your scratch directory:

```bash
mkdir /beegfs/scratch/${USER}
cd /beegfs/scratch/${USER}
pwd
```

To go to your home directory, you can do

```bash
cd /home/<your Picotte username>
```

:::{hint}
There is also a shortcut; to go to your home directory, you can simply type

```
cd
```
:::

## Local Scratch

Every Picotte compute node has storage on the node itself and is referred to as local scratch. 
This scratch space can only be accessed by a job running on the node. 

To access this space in your Slurm script, use the `$TMP` environment variable or the location `/local/scratch/$SLURM_JOBID`. 

:::{warning}
Files in local scratch will be purged automatically when your job terminates. Copy files elsewhere before your job ends.
:::

:::{note}
Please don't use `/tmp` for temporary storage! Use `/beegfs/scratch` or `$TMP`.
:::

## Group Storage

Group storage space on Picotte is available at a charge for faculty members. Please contact us 
for further information.

## Performance Guidelines

Generally speaking, `$TMP` will always be the fastest file system to use because there is no network involved. 
However, this space cannot be shared between a group of nodes participating in a job, and the data must be 
moved to permanent storage before the job completes.

`beegfs/scratch`` is a parallel file system that runs atop spinning disk drives and is best suited for workflows 
issuing sequential, large read or write requests. The Picotte support team encourages you to test your workflows 
against all three file systems to see which one works best for you.

