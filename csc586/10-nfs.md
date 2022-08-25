
# Networked File System

```{dropdown} 1. Anyone knows/remembers?

:::{image} ../fig/csc586//10-nfs/sun.png
:alt: Sun Microsystem Logo
:class: bg-primary mb-1
:height: 200px
:align: center
:::

*Sandberg, R., Goldberg, D., Kleiman, S., Walsh, D., & Lyon, B. (1985, June)*. [Design and implementation of the Sun network filesystem](http://www.cs.cornell.edu/courses/cs6411/2018sp/papers/nfs.pdf). In Proceedings of the Summer USENIX conference (pp. 119-130)

```

```{dropdown} 2. Design goal

- Machine and operating system independence
- Crash recovery
- Transparent access
- UNIX semantics maintained on client
- Reasonable performance (target 80% as fast as local disk)

```

```{dropdown} 3. NSF design components

- NFS protocol
- Server side implementation
- Client side implementation
 
```

```{dropdown} 4. NFS protocol

- Remote Procedure Call (RPC) mechanism
  - Simplify the definition, organization, and implementation of remote services. 
- Stateless protocol
  - Parameters to each procedure call contain all the information
  necessary to complete the call.
  - The server does not keep track of past requests. This makes crash recovery easy. 
- Transport independent (works with both TCP and UDP). 
- Key procedure parameter: a file handler (`fh`)

```

```{dropdown} 5. NFS Server

- Commit modified data to stable storage before returning RPC calls
  - Write to disk
- New parameter, generation number, for inode and file system id. 

```

```{dropdown} 6. NFS Client

- Allow `mount` to attach remote file system
- New Unix kernel interface for all file system types: Virtual FileSystem (VFS)
  - Allows system calls to be unified
  - VFS will automatically determine/interact with the correct file system types, 
  including networked file systems. 

```


```{dropdown} 7. Architectural Design

:::{image} ../fig/csc586//10-nfs/nfs.png
:alt: Networked File System Design
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```