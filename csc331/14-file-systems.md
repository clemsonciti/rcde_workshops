
# Introduction to file systems"
teaching: 0
exercises: 0
questions:
- "How to manage a persistent device?"
- "How to implement a simple file system?"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"



> ## 1. File systems
>
> - Provide long-term information storage
> - Challenges:
>   - Store very large amounts of information
>   - Multiple processes must be able to access ino concurrently
>   - Information must survive (persist)
>     - termination of process using it
>     - computer crashes
>     - disk failures
>     - power outage
>     - …
>   - Easy-to-use user interface
```


> ## 2. Files and directories
>
> - It’s all illusion!
> - CPU virtualization: a **process** that has its own processor.
> - Memory virtualization: a big, contiguous, and private address space that 
> can easily be accessed through virtual addresses. 
> - Storage virtualization: a huge, persistent storage with files and directories 
> which can be accessed using some easy-to-use APIs (ls, rm, cp …).
```


> ## 3. Abstraction: files and directories
>
> - File: a linear array of bytes, each of which you can read and write.
> - A file has some high-level, user-readable name, e.g., `interceptor.c`.
>   - One file may have multiple user-readable names, as we will see.
> - Each file has a low-level name called the `inode` number.
>   - This is the real identifier of a file.
> - File system does NOT care about what type of file it is (C code, picture 
> or video, it just makes sure to store all bytes in a file **persistently**.
>
> <img src="../fig/file-system/01.png" alt="files and inodes" style="height:200px">
```


> ## 4. Abstraction: files and directories
>
> - Directory
>   - Each directory also has an `inode` number
> - Content of a directory:
>   - a list of (user-readable name, `inode` number) pairs
>   - which are the files and directories *under* this directory
> - Directory tree / hierarchy
>
> <img src="../fig/file-system/02.png" alt="files and directories" style="height:350px">
```


> ## 5. File operations: create
> - **create**: `int fd = open(“foo”, O_CREAT | O_WRONLY | O_TRUNC, S_IRUSR | S_IWUSR)`
>   - [open](http://man7.org/linux/man-pages/man2/open.2.html)
>   - `O_CREAT`: creates the file if it does not exist.
>   - `O_WRONLY`: the file can only be written to.
>   - `O_TRUNC`: if the file already exists, truncates it to zero bytes, removing 
>   any existing contents. 
>   - `S_IRUSR`: readable by the owner,
>   - `S_IWUSR`: writable by the owner.
>   - `fd`: file descriptor, starts at 3 ( Reserved values: `0` for stdin, `1` for stdout, 
>   `2` for stderr)
> - **read**: `ssize_t read(int fd, void *buf, size_t count)`
>   - [read](https://man7.org/linux/man-pages/man2/read.2.html)
>   - `fd`: file descriptor value
>   - `*bf`: memory address to store data read from file represented by `fd`. 
>   - `count`: number of bytes to be read
>   - A successful read will return the number of bytes read or a `-1` if there
>   is an error. 
> - **write**: `ssize_t write(int fd, const void *buf, size_t count)`
>   - [write](https://man7.org/linux/man-pages/man2/write.2.html)
>   - `fd`: file descriptor value
>   - `*bf`: memory address containing data to be written to the file represented by `fd`.
>   - `count`: number of bytes to be written. 
>   - A successful write will return the number of bytes written or a `-1` if there 
>   is an error.  
```


> ## 6. Hands on: file operations
>
> - Before turning on the VM, makes sure that you have two processors assigned
> to your VM. 
>
> - Open a terminal (Windows Terminal or Mac Terminal). 
> - Run the command to launch the image container for your platform:
> - Windows:
> 
> ~~~
> $ podman run --rm --userns keep-id --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it -v /mnt/c/csc331:/home/$USER/csc331:Z localhost/csc-container /bin/bash
> ~~~
> {: .language-bash}
>
> - Mac:
>
> ~~~
> $ docker run --rm --userns=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it -v /Users/$USER/csc331:/home/$USER/csc331:Z csc-container /bin/bash
> ~~~
> {: .language-bash}
>
> - Root password: `goldenrams`
>
> ~~~
> $ sudo apt-get install -y strace
> $ echo "Hello World" > hello.txt
> $ strace -t -o cat_log cat hello.txt 
> $ cat cat_log
> ~~~ 
> {: .language-bash}
> 
> <img src="../fig/file-system/03.png" alt="strace" style="height:1000px">
>
> - Search the manual of the following functions: `openat`, `fstat`, `fadvise64`, 
> and `mmap`. 
> 
```


> ## 7. Non-sequential read/write: lseek
>
> - `read()` and `write()` only do sequential read/write, there is no way to specify a 
> particular read/write position (offset).
> - For each file opened by a process, the OS keeps track of a *current* offset, which 
> determines where the next read/write happens, `read()` and `write()` updates *current* 
> offset according to how many bytes are read/written 
>   - cannot update current to wherever they want
> - If want to update *current* to wherever you want, use `lseek()`:  `off_t lseek(int fd, off_t offset, int whence)`
>   - [lseek](https://man7.org/linux/man-pages/man2/lseek.2.html)
>   - `fd`: file descriptor valur
>   - `offset`: offset value. 
>   - `whence`: 
>     - if `whence` is `SEEK_SET`, the current offset is set to `offset` bytes
>     - if `whence` is `SEEK_CUR`, the current offset is set to `current + offset` bytes
>     - if `whence` is `SEEK_END`, the current offset is set to `size_of_file + offset` bytes
> 
```


> ## 8. Implementations of file systems
>
> - There exist many, many file system implementations, literally from `AFS` to `ZFS`.
> - [File system implementations](https://en.wikipedia.org/wiki/List_of_file_systems)
> - Some famous ones: 
>   - FAT32, NTFS used by Windows
>   - HFS+ used by Mac OS X
>   - UFS, ZFS used by BSD, Solaris
>   - ext2, ext3, ext4, ReiserFS, XFS, JFS used by Linux
> - We will study a very simple example file system named VSFS: Very Simple File System
> - Analogy
>
> <img src="../fig/file-system/04.png" alt="file system implementations" style="height:500px">
>
```


> ## 9. How to implement a simple file system?
>
> - What structures are needed on the disk? 
> - What do they need to track? 
> - How are they accessed?
>
```

> ## 10. Mental model of a file system
>
> - What on-disk structures store the file system’s data and metadata? 
> - What happens when a process opens a file? 
> - Which on-disk structures are accessed during a read or write?   
> 
> By working on and improving your mental model, you develop an abstract understanding of what is going on, 
> instead of just trying to understand the specifics of some file-system code (though that is also useful, 
> of course!).
>
> > ## Unformatted raw disk
> >
> > <img src="../fig/file-system/05.png" alt="raw disk" style="height:150px">
> ```
>
> > ## Overall organization
> >
> > - The whole disk is divided into **fixed-sized blocks**.
> > - Block size: 4KB
> > - Number of blocks: 64
> > - Total size: 256KB
> >
> > <img src="../fig/file-system/06.png" alt="block divisions" style="height:150px">
> ```
> 
> > ## Data region
> >
> > - Most of the disk should be used to actually store user data, while leaving a little space for storing 
> > other things like metadata
> > - In VSFS, we reserve the last 56 blocks as data region.
> >
> > <img src="../fig/file-system/07.png" alt="data region" style="height:150px">
> ```
>
> > ## Metadata: inode table
> >
> > - The FS need to track information about each file. 
> > - In VSFS, we keep the info of each file in a struct called inode. And we use 5 blocks for storing all the inodes.
> > - Maximum number of inodes it can hold: 5 * 4KB / 128B = 160, i.e., this VSFS can store at most 160 files.
> >
> > <img src="../fig/file-system/08.png" alt="inode table" style="height:150px">
> ```
> 
> > ## Allocation structure
> >
> > - For both data region and inode region, we need to keep track of which blocks are being used and which blocks are free. 
> > - We use a data structure called bitmap for this purpose, which is just a sequence of bits, and each bit indicates whether one block is free (0) or in-use (1).
> > - We have one bitmap for the data region and one bitmap for the inode region, and reserve one block for each bitmap. (4KB = 32K bits, can keep track of 32K blocks)
> >
> > <img src="../fig/file-system/09.png" alt="allocation structure" style="height:150px">
> ```
>
> > ## Superblock
> >
> > - Superblock contains information about this particular file system, e.g., 
> >   - What type of file system it is (“VSFS” indicated by a magic number)
> >   - how many inodes and data blocks are there (160 and 56) 
> >   - Where the inode table begins (block 3)
> >   - etc. 
> > - When mounting a file system, the OS first reads the superblock, identify its type and other parameters, 
> > then attach the volume to the file system tree with proper settings.
> >
> > <img src="../fig/file-system/09.png" alt="Superblock" style="height:150px">
> ```
```

> ## 11. Example implementations
>
> - [xv6 file system](https://github.com/mit-pdos/xv6-public/blob/master/fs.h)
> - [Linux ext2](https://github.com/torvalds/linux/blob/master/fs/ext2/ext2.h)
>
```


> ## 12. Example: reading a file with inode number 32
>
> - From superblock we know
>   - inode table begins at Block 3, i.e., 12KB
>   - inode size is 128B
> - Calculate the address of inode 32
>   - 12KB + 32 * 128B = 16K
> So we have the inode, but which blocks have the data?
>
> <img src="../fig/file-system/09.png" alt="allocation structure" style="height:200px">
> 
```


> ## 13. Data structure: the inode
>
> - Short for index node
> - In `vsfs` (and other simple file systems), given an `i-number`, you should directly be able 
> to calculate where on the disk the corresponding inode is located.
>   - `blk = (inumber * sizeof(inode_t)) / blockSize` 
>   - `sector = ((blk * blockSize) + inodeStartAddr) / sectorSize`
>
> <img src="../fig/file-system/10.png" alt="allocation structure" style="height:200px">
> 
```


> ## 14. Multi-level index with indirect pointers
>
> - Direct pointers to disk blocks do not support large files, so people came up with the 
> idea of indirect pointer. 
> - Instead of pointing to block of user data, it points to a block the contains more pointers.
> - For the 15 pointers we have in an inode, use the first 14 pointers as direct pointers and the 
> 15th pointer as an indirect pointer. 
> - How big a file can we support now?
>   - 14 direct pointers in total: 14 data blocks
>   - Indirect pointer points to a block (4KB) which can hold 1K pointers (each pointer is 4B), so 
>   1K data blocks in addition. 
>   - So total size supported: 4K * (14 + 1K) = 4152KB
> - Bigger?
>
> <img src="../fig/file-system/11.png" alt="multi-level indirect pointers" style="height:500px">
>
> - Why use an imbalanced tree like this? Why not a different approach? 
> - Many researchers have studied file systems and how they are used, and virtually every 
> time they find certain “truths” that hold across the decades. 
> - One such finding is that most files are small. 
>   - This imbalanced design reflects such a reality: if most files are indeed small, it 
>   makes sense to optimize for this case.
>   - [A five-year study of file system metadata, 2007](http://static.usenix.org/event/fast07/tech/full_papers/agrawal/agrawal.pdf)
>
> <img src="../fig/file-system/12.png" alt="file system metadata study" style="height:300px">
```


> ## 15. Another approach: extent-based
>
> - An extent is a disk pointer plus a length (in blocks), i.e., it allocates a 
> few blocks in a row. 
> - Instead of requiring a pointer to every block of a file, we just need a pointer to 
> every several blocks (every extent).
> - It is less flexible than the pointer-base approach, but uses smaller amount of metadata 
> per file, and file allocation is more compact.
> - Adopted by ext4, HFS+, NTFS, XFS.
``` 



> ## 16. Yet anther approach: linked-based
>
> - Instead of having pointers to all blocks, the inode just has one pointer pointing to 
> the first data block of the file, then the first block points to the second block, etc. 
> - Works poorly if want to access the last block of a big file. To help, use an in memory file 
> allocation table which is indexed by address of data block, so finding a block can be faster.
> - This is the FAT file system, used by Windows before NTFS.
>
> <img src="../fig/file-system/13.png" alt="linked-based" style="height:300px">
```

{% include links.md %}

