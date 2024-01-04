# File Permissions and Atrributes

Working as part of a team in Linux environment require us to know 
how to share your files/directories with others. 

Use `ls -l` (**l**ong format) to list files and their attributes.

~~~bash
-rw-r--r-- 1 user group 1002287 Oct 20 15:49 example.csv
~~~

Explanation of output:
- `-rw-r--r--`: Permissions of file
- `1`: hard link count (out of scope)
- `user`: name of file owner
- `group`: name of group owner
- `1002287`: file size in **bytes**
- `Oct 20 15:49`: last time file was **modified**
- `example.csv`: name of file

Permissions are grouped into 3 categories: 
- user
- group
- other 

Each category has 3 permissions:
- `r` (read)
- `w` (write)
- `x` (execute)
- A dash means no permission.

The command `chmod` (**ch**ange **mod**e) is used to edit file permissions. 
There are 2 ways to represent the permissions: *numeric* and *symbolic*.

**Numeric mode**

The `rwx` permissions are represented by octal numbers (0-7). The following table explains 
each value (credit: [Wikipedia](https://en.wikipedia.org/wiki/Chmod#Numerical_permissions)):

\#  |	       Sum         | rwx    |        Permission       |
--- | ------------------ | ------ | ----------------------- |
7   | 4(r) + 2(w) + 1(x) |	rwx   |	read, write and execute |
6   | 4(r) + 2(w)        |	rw-   |	read and write          |
5   |	4(r) + 1(x)        |	r-x   |	read and execute        |
4   |	4(r)               |	r--   |	read only               |
3   |	2(w) + 1(x)        |	-wx   |	write and execute       |
2   |	2(w)               |	-w-   |	write only              |
1   |	1(x)               |	--x   |	execute only            |
0   |	0                  |	`---` |	none                    |

**Common file permissions:**

- `644` - owner can read and write file, all others can read
- `755` - owner can read, write, and execute, all others can read and execute
- `600` - owner can read and write, no access to anyone else

**Symbolic mode**

Use symbolic notation for finer grained control of permissions. Symbolic notation 
requires a `reference`, `operator`, and `mode`. From 
[Wikipedia](https://en.wikipedia.org/wiki/Chmod#Symbolic_modes):

| Reference | Class | Description |
| --------- | ----- | ----------- |
| u         | user  | file owner  |
| g         | group | member's of the files's group |
| o         | others | users who are neither the file's owner nor members of the file's group |
| a         | all   | all three of the above, same as `ugo` |
| (empty)   | default | same as "all", except that bits in the umask will be unchanged |

| Operator | Description |
| -------- | ----------- |
| + | adds the specified modes to the specified classes |
| - | removes the specified modes from the specified classes |
| = | the modes specified are to be made the exact modes for the specified classes |

| Mode | Name | Description |
| ---- | ---- | ----------- |
| r | read | read a file or list a directory's contents |
| w | write | write to a file or directory |
| x | execute | execute a file or recurse a directory tree |

**Common commands:**

Make file executable by all:

~~~bash 
chmod +x file
~~~
