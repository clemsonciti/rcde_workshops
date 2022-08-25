
# Crash consistency: fsck and journaling"
teaching: 0
exercises: 0
questions:
- "How to update the disks despite crashes?"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"


> ## 1. Persistence
>
> - Data persists after the computer is powered off
>   - This is a given due to disks’ physics
> - If the computer crashes during the file system read/write activities, how can 
> we guarantee that data on disk are still consistent?
>   - This is a more interesting problem for operating systems.
>   - The crash-consistency problem
```

> ## 2. A crash scenario
> 
> - A 4KB file on disk, within a single data block
> - An additional 4KB is written to the file (one more data block added). 
> - If everything went well:
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 3. If the computer crashed during write
> 
> What are all the possible inconsistent states that the FS can be in after the crash?  
> 
> - Only one thing updated
>   - Case 1: Just the `data block` is updated, but not the `data bitmap` and `inode`
>   - Case 2: Just the `inode` is updated, but but not the `data bitmap` and `data block`
>   - Case 3: Just the `data bitmap` is updated, but not the `inode` and `data block`
> - Only two things updated
>   - Case 4: `inode` and `data bitmap` updated, but not `data block`
>   - Case 5: `inode` and `data block` updated, but not `data bitmap`
>   - Case 6: `data bitmap` and `data block` updated, but not `inode`  
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 4. Case 1: only the data block is updated
> 
> - The data is on disk
> - Nobody ever knows, because inode and data bitmap are not updated
> - The file system itself is still consistent, it is just like nothing happened
> - No need to fix anything   
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 5. Case 2: only the inode is updated 
> 
> - `inode` has data block pointer pointing to an unwritten data block
> - If we trust the `inode`, we will read garbage data
> - Also there is inconsistency between `data bitmap` and the `inode`:
>   - `inode` says that the `data block #5` is used, but `data bitmap` say it is not.
>   - if not fixed, could allocate `block #5` again and overwrite its data by mistake  
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 6. Case 3: only data bitmap is updated
> 
> - `inode` is not pointing `data block #5`, so no risk of reading garbage data
> - `data bitmap` says `data block #5` is used, but in fact it is not
> - `data block #5` will never be used again
> - This is called a **space leak**.  
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 7. Case 4: Only inode and data bitmap updated
> 
> - The file system will read garbage data from `block #5` again.
> - The file system doesn’t even realized anything wrong, because the inode and the 
> data bitmap are consistent with each other.  
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 8. Case 5: Only inode and data block updated
> 
> - The file system will **NOT** read garbage data.
> - `Data bitmap` and `inode` are inconsistent between each other:
>   - `inode` says that the data block #5 is used, but `data bitmap` say it is not
>   - if not fixed, could allocate `block #5` again and overwrite its data by mistake
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 9. Case 6: Only data bitmap and data block updated
> 
> - Inconsistency between inode and data bitmap.
> - We know `data block #5` is used, but will never know which file uses it
>
> <img src="../fig/fsck/01.png" alt="a crash scenario" style="height:300px">
```


> ## 10. Problem!
> 
> - We wish file system updates were atomic, but they are not.
> - The there are many different problems that can occur if the computer crashes during
> a file system update.
>   - Inconsistency in file system data structure
>   - Reading garbage data
>   - Space leak
> - We call them crash-consistency problems
```


> ## 11. Solution 1: FSCK
> 
> <img src="../fig/fsck/02.png" alt="FSCK" style="height:500px">
>
```


> ## 12. FSCK (File System Check)
> 
> - A UNIX tool that scans the whole disk, finds inconsistencies ands repair them.
>   - It runs before the file system is mounted, e.g., when booting
>   - when crash happens, let it be, and fix it later (when rebooting)
> - Typical checks performed
>   - all blocks pointed to by `inode` or indirect block must be marked *used* in `bitmap`
>   - all used `inodes` must be in some directory entry
>   - `inode` reference count (link count) must match
>   - no duplicate data pointers.
>   - etc.
>
```


> ## 13. Limitation of FSCK
> 
> - A working FSCK requires very complicated and detailed knowledge of the 
> file system, and is hard to be implemented correctly. 
> - It only cares about the internal consistency of the file system, and does **NOT** 
> really care about lost data (e.g., Case 1 and Case 4)
> - Bigger problem: it is too slow
>   - with a large hard drive, it can easily take hours to finish FSCK
>   - it’s just a bit irrational: scan the whole disk no matter how small an 
>   inconsistency needs to be fixed.
>
```


> ## 14. Solution 2: Journaling (write-ahead logging)
> 
> - Additional space in the on-disk data structure
> 
> <img src="../fig/fsck/03.png" alt="Journaling" style="height:350px">
>
```


> ## 15. Journaling: what to store?
> 
> When updating the disk, before making the actual writes to disk, the FS first writes 
> a little *note* about what it is about to do, to the journal (or log, at well known 
> location on disk).  
>
> Failures become recoverable:  
> - If crash happens during actual write (journal write completed), then we can look at
> the journal and replay the actual writes hence recover the data.
> - If crash happens even before journal write finishes, then it doesn’t matter since 
> the actual write has NOT happened at all, nothing is inconsistent.
>
```


> ## 16. Journaling: the structure to be written to the journal/log
> 
> - Transaction:
>   - starts with a `transaction begin` (TxB) block, containing a `transaction id` (TID) 
>   followed by blocks with the exact content to be written.
>     - physical logging: putting exact physical content
>     - logical logging: putting more compact logical representation
>   - ends with a `transaction end` (TxE) block, containing the TID.
> <img src="../fig/fsck/04.png" alt="Journal transaction data structure" style="height:100px">
>
```


> ## 17. Journaling: sequence of operations
> 
> - Journal write: write the transaction, including the TxB, 
> all pending data and metadata updates, and the TxE, to the journal; wait for these 
> writes to complete.
> - Checkpoint: actually write the pending data and metadata to to their final locations 
> in the file system.
> - What can go wrong:
>   - Crash can occur during journal writes.
>   - When having a batch of writes, the disk may perform some disk scheduling, so 
>   the writes in the batch can happen in any order.
>
> <img src="../fig/fsck/05.png" alt="Journal transaction data structure" style="height:100px">
```


> ## 18. Journaling: a better sequence of operations
> 
> - Journal write: write the transaction, including the TxB, all pending data and 
> metadata updates, NOT including the TxE, to the journal; wait for these writes to 
> complete.
> - Journal commit: write the TxE block (a.k.a. transaction commit block); now tractions 
> is said to be committed.
> - Checkpoint: actually write the pending data and metadata to to their final locations 
> in the file system.
> - Hard disk guarantees atomic write of a 512-byte sector, the TxE block should fit in 
> a 512-byte sector, so the commit is either fully completed or not completed at all.
>
```


> ## 19. Journaling: recover from a crash
> 
> - If crash happens before the transaction is committed to the journal/log
> simply skip the pending update.
> - If crashed happens during the checkpoint step:
>   - When booting, scan the journal and lookup for committed transactions (much faster
>   than fsck scanning the whole disk).
>   - Replay these transactions.
>   - After replay the file system is guaranteed to be consistent, then we can mount 
>   it and do other stuff.
>   - This is also called redo logging.
>
```


> ## 20. Journaling: space requirement
> 
> - If we need to write something to journal for every single disk update, 
> does the journal need to be huge?
> - Not really, after checkpoint the transaction in the journal is not useful anymore, 
> so the space can be freed.
> - So there are indeed 4 steps:
>   - journal write
>   - journal commit
>   - checkpoint
>   - free 
> - Typical data structure for the journal: circular log
>
```


> ## 21. Metadata Journaling
> 
> - Recovery is fast with journaling, but the normal operations are slower, 
> because for every update we need to write to the journal first then do the update. 
> - Writing time is at least doubled, even worse if journal writing breaks sequential 
> writes and cause jump-back-and-forth between journal and data region.
> - Metadata journaling is just like data journaling (what we just described), except 
> that we only write metadata (NOT data) to the journal.
> - The journal looks like ...
>
> <img src="../fig/fsck/06.png" alt="metadata journaling" style="height:100px">
```


> ## 22. Metadata journaling
> 
> - If we write data after checkpointing metadata, then write data, if crash 
> occurs before all data is written, the `inodes` will point to garbage data.
> - How to solve this problem: Write data before writing metadata journal!
>   - write data, wait until it completes
>   - metadata journal write
>   - metadata journal commit
>   - checkpoint metadata
>   - free
> - If write data fails, then no metadata is written at all, like nothing happened. 
> - If data write succeed, but metadata write fails, still like nothing happened.
> - If metadata write succeeds, data must be available.
>
```


> ## 23. Journaling summary
> 
> - Journaling provides file system consistency
> - Time complexity of recovery is `O(size_of_journal)`, instead of 
> `O(size_of_disk_volume)` in fsck. 
> - Widely adopted by most modern file systems, including Linux’s Ext3, Ext4, ReiserFS, 
> IBM’s JFS, SGI’s XFS, and Windows’ NTFS. 
> - Metadata journaling is the most commonly used, since it reduces the amount of traffic 
> to the journal while provide reasonable consistency guarantees.
>
```

{% include links.md %}

