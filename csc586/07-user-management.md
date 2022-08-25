
# User Management


```{dropdown} 1. What is a user?

- Nothing more than a number (user ID - UID)
- Everything else revolves around this number
- System maps UID to additional set of information based on an API. 

```

```{dropdown} 2. /etc/passwd

- login names: ≤ 32 chars, case sensitive and (in some cases) even special chars (☹, ...)
- encrypted password ( or *) - do NOT leave empty
  - DES, MD5($1$..), Blowfish($2y$), SHA-256 ($5$), SHA-512 ($6$), 
  - check `/etc/login.defs` or (was) `/etc/default/passwd` plus `PAM` and on RHEL/CentoS `authconfig`.
- UID (32-bit integer)
  - 0 for root by default
  - do not recycle them (or as late as possible) - ? why
  - should be unique in the whole organization ( else NFS problems, ..)
- GID
- GECOS (finger's interpretation)
- `home` dir
- `login` shell

```

```{dropdown} 3. /etc/group

- Contains the names of UNIX groups and list of each group’s members
 
```

```{dropdown} 4. System utility commands

- useradd
- userdel 
- usermod
- pwconv 
- pwunconv
- groupadd
- groupmod
- groupdel 

```

