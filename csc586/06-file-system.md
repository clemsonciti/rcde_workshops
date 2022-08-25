
# The Filesystem


```{dropdown} 1. In Linux, everything is a file

- Processes
- Audio devices
- Kernel data structures and tuning parameters
- Interprocess communication channels

```

```{dropdown} 2. Main components

- A namespace
- An API
- Securiy models
- An implemenation
```

```{dropdown} 3. Path names

- Single unified hierarchy start at root: `/`
- Absolute path: path name starts from root
- Relative path: path name starts from current directory: . or subdirectory name
 
```

```{dropdown} 4. Mouning and unmounting

- The root filesystem is composed of smaller trunks (smaller filesystems)
- Smaller filesystems are attached to the tree with the mount command, which ...
  - Maps a directory within the existing filesystem tree, called the mount 
  point, to the root of the newly attached filesystem. 

```

```{dropdown} 5. Who is doing what on which file system?

- [fuser](https://man7.org/linux/man-pages/man1/fuser.1.html)

~~~
$ man fuser
$ sudo fuser -cv /users
~~~

- Instead of rebooting, perhaps unmounting/remounting of offending device drivers.
```

```{dropdown} 6. Organizaion of the file system tree

:::{image} ../fig/csc586//06-file-system/filesystem.png
:alt: Standard directories and their contents
:class: bg-primary mb-1
:height: 700px
:align: center
:::

```

```{dropdown} 7. Filetype encoding

- Character/block device file: standard communication interface 
provided by device drivers.
- Local domain sockets: connections between processes that allow them 
to communicate hygienically.
- Named pipes allow communication between two processes running 
on the same host. 
- Symbolic links: point to a file by name
- Hard links: create an illusion that a file exists in more than one 
place at the same time. 


:::{image} ../fig/csc586//06-file-system/encoding.png
:alt: File type encoding used by ls
:class: bg-primary mb-1
:height: 300px
:align: center
::: 

```


```{dropdown} 8. File attributes

- Traditionally 12 bits for each file: the file's mode (plus 4 more bits : 
file's type)
- 9 permission bits - read, write, execute for owner, group, others
- setuid & setgid bits (4000 , 2000)
  - setgid on directory - newly created file has group 
  ownership of the directory (not group ownership of a user creating it)
- sticky bit (1000)
  - on regular files ignored (original meaning: keep program text on swap device)
  - on directories - only the owner of the file and the owner of that directory may remove the file from that directory

:::{image} ../fig/csc586//06-file-system/chmod-encoding.png
:alt: File type permission
:class: bg-primary mb-1
:height: 300px
:align: center
::: 



:::{image} ../fig/csc586//06-file-system/mnemonic-syntax.png
:alt: File type permission using mnemonic syntax
:class: bg-primary mb-1
:height: 300px
:align: center
::: 




```


```{dropdown} 9. Access control lists:

- supported for ext2, ext3, ext4, reiserfs, XFS, JFS: `mount -o [no]acl`
- allows rwx to be set independently for any user.group combination: `getfacl`, `setfacl` ( plus man acl)
- NFSv4 - superset of POSIX ACLs plus all permission bits and most semantics 
from Windows


```

