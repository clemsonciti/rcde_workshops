# Navigating Files and Directories

teaching: 15
exercises: 0
questions:
- "How can I move around on Palmetto?"
- "How can I see what files and directories I have?"
- "How can I specify the location of a file or directory on my computer?"
objectives:
- "Explain the similarities and differences between a file and a directory."
- "Translate an absolute path into a relative path and vice versa."
- "Construct absolute and relative paths that identify specific files and directories."
keypoints:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which forms a directory tree."
- "`cd path` changes the current working directory."
- "`ls path` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- "`pwd` prints the user's current working directory."
- "`whoami` shows the user's current identity."
- "`/` on its own is the root directory of the whole file system."
- "A relative path specifies a location starting from the current location."
- "An absolute path specifies a location from the root of the file system."
- "'..' means 'the directory above the current one'; '.' on its own means 'the current directory'."
---

The part of the operating system responsible for managing files and directories
is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called "folders"),
which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories.
The first command that we will look at is called `pwd` (print working directory). Let's type it in:

~~~
$ pwd
~~~
{: .bash}

~~~
/home/<your Palmetto username>
~~~
{: .output}

To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  
On Palmetto, the filesystem looks something like this: 

![The File System](../fig/filesystem.png)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own.

Inside that directory are several other directories:
`home` (where users' personal directories are located),
`bin` (which is where some built-in programs are stored),
`tmp` (for temporary files that don't need to be stored long-term),
`etc` (for miscellaneous data files),
and so on.  

We know that our current working directory is stored inside `/home`
because `/home` is the first part of its name.
Similarly,
we know that `/home` is stored inside the root directory `/`
because its name begins with `/`.

> ## Slashes
>
> Notice that there are two meanings for the `/` character.
> When it appears at the front of a file or directory name,
> it refers to the root directory. When it appears *inside* a name,
> it's just a separator.
{: .callout}

Underneath `/home`,
we find one directory for each user with an account on Palmetto. 

Now let's learn the command that will let us see the contents of our 
own filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing":

~~~
$ ls
~~~
{: .bash}

~~~
Applications Documents    Library      Music        Public
Desktop      Downloads    Movies       Pictures
~~~
{: .output}

Your results might be completely different, depending on the ontents of your home directory. In fact, if you are just starting to use Palmetto, your home directory might be empty.


`ls` prints the names of the files and directories in the current directory in 
alphabetical order,
arranged neatly into columns.
We can make its output more comprehensible by using the **flag** `-F`,
which tells `ls` to add a trailing `/` to the names of directories:

~~~
$ ls -F
~~~
{: .bash}

~~~
Applications/ Documents/    Library/      Music/        Public/
Desktop/      Downloads/    Movies/       Pictures/
~~~
{: .output}

And note that there is a space between `ls` and `-F`:
without it,
the shell thinks we're trying to run a command called `ls-F`,
which doesn't exist.

`ls` has lots of other options. To find out what they are, we can type:

~~~
$ ls --help
~~~
{: .bash}

~~~
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      scale sizes by SIZE before printing them; e.g.,
                               '--block-size=M' prints sizes in units of
                               1,048,576 bytes; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and/or -s, print human readable sizes
                               (e.g., 1K 234M 2G)
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage
  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                               link, show information for the file the link
                               references rather than for the link itself
  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print raw entry names (don't treat e.g. control
                               characters specially)
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=STYLE     with -l, show times using style STYLE:
                               full-iso, long-iso, iso, locale, or +FORMAT;
                               FORMAT is interpreted like in 'date'; if FORMAT
                               is FORMAT1<newline>FORMAT2, then FORMAT1 applies
                               to non-recent files and FORMAT2 to recent files;
                               if STYLE is prefixed with 'posix-', STYLE
                               takes effect only outside the POSIX locale
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help     display this help and exit
      --version  output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'
~~~
{: .output}

Many Linux commands, and programs that people have written that can be
run from within the shell, support a `--help` flag to display more
information on how to use the commands or programs.

For more information on how to use `ls` we can type `man ls`.
`man` is the Unix "manual" command:
it prints a description of a command and its options,
and (if you're lucky) provides a few examples of how to use it.


To navigate through the `man` pages,
you may use the up and down arrow keys to move line-by-line,
or try the "b" and spacebar keys to skip up and down by full page.
Quit the `man` pages by typing "q".


We can also use `ls` to see the contents of a different directory. Let's list the directories of all the Palmetto users (note that you cannot actually go inside other people's directories):  
~~~
$ ls /home
~~~
{: .bash}

Note that on Palmetto you cannot access other people's directories. 

The next command we will discuss is `mkdir`, which creates a new directory. Let's create a directory with the name `linux_workshop`:

~~~
$ mkdir linux_workshop
~~~
{: .bash}

Now, if you type `ls`, you should see `linux_workshop` lited among the contents of your home directory. 

The next command that we will discuss is `cd` ("change directory"), which changes our location to a different directory, so 
we are no longer located in
our home directory. Let's enter the directory we have just created:
~~~
$ cd linux_workshop
~~~
{: .bash}

Now, our current directory is `linux_workshop`:
~~~
$ pwd
~~~
{: .bash}

~~~
/home/<your Palmetto username>/linux_workshop
~~~
{: .output}

If you type `ls`, you won't see anything, because we have just created this directory and it is empty.

To go back to your home directory, you need to go one level up on the directory tree. There is a shortcut in the shell to move up one directory level
that looks like this: 

~~~
$ cd ..
~~~
{: .bash}

`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we're back in your home directory:

~~~
$ pwd
~~~
{: .bash}

~~~
/home/<your Palmetto username>
~~~
{: .output}

The special directory `..` doesn't usually show up when we run `ls`.  If we want 
to display it, we can give `ls` the `-a` flag:

~~~
$ ls -F -a
~~~
{: .bash}


`-a` stands for "show all";
it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which in our case is the `/home` directory).
As you can see,
it also displays another special directory that's just called `.`,
which means "the current working directory".
It may seem redundant to have a name for it,
but we'll see some uses for it soon.

> ## Other Hidden Files
> 
> In addition to the hidden directories `..` and `.`, you may also see a file
> called `.bash_profile`. This file usually contains shell configuration
> settings. You may also see other files and directories beginning
> with `.`. These are usually files and directories that are used to configure
> different programs on your computer. The prefix `.` is used to prevent these
> configuration files from cluttering the terminal when a standard `ls` command
> is used.
{: .callout}


These  are the basic commands for navigating the filesystem on your computer: 
`pwd`, `ls` and `cd`.  Let's explore some variations on those commands.  What happens 
if you type `cd` on its own, without giving 
a directory?  

~~~
$ cd
~~~
{: .bash}

How can you check what happened?  `pwd` gives us the answer!  

~~~
$ pwd
~~~
{: .bash}

~~~
/home/<your Palmetto username>
~~~
{: .output}

It turns out that `cd` without an argument will return you to your home directory, 
which is great if you've gotten lost in your own filesystem.  

Let's try returning to the `linux_workshop` directory from before.  We can actually string together the list of directories 
to move to `linux_workshop` in one step: 

~~~
$ cd /home/<your Palmetto username>/linux_workshop
~~~
{: .bash}

Check that we've moved to the right place by running `pwd`.  

This is probably a good time to mention a couple of things which make Bash a convenient shell. The first one is *tab completion*. Most of the times, you don't need to type in the full name of the folders; you can to type the first few characters and press the TAB key. If there are files or folders that match the pattern you have entered, it will be completed for you. Let's go to the home directory, then type `cd linu` and press TAB instead of ENTER, and see what happens:

~~~
$ cd 
$ cd linu
~~~
{: .bash}
The shell should automatically complete `linu` to `linux_workshop`. The second useful feature is the *command history*. If you press the UP &uarr; or DOWN &darr; arrow keys, you can go through the previously typed commands. Try it. 


If we want to move up one level from the shell directory, we could use `cd ..`.  But 
there is another way to move to any directory, regardless of your 
current location.  

So far, when specifying directory names, or even a directory path (as above), 
we have been using **relative paths**.  When you use a relative path with a command 
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by 
including its entire path from the root directory, which is indicated by a 
leading slash.  The leading `/` tells the computer to follow the path from 
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to any directory from anywhere on
the filesystem.  To find the absolute path 
we're looking for, we can use `pwd` and then extract the piece we need 
to move to `linux_workshop`.  



> ## Two More Shortcuts
>
> The shell interprets the character `~` (tilde) at the start of a path to
> mean "the current user's home directory". For example, `~/linux_workshop` is equivalent to
> `/home/<your Palmetto username>/linux_workshop`. This only works if it is the first character in the
> path: `here/there/~/elsewhere` is *not* `here/there/Users/nelle/elsewhere`. 
> 
> Another shortcut is the `-` (dash) character.  `cd` will translate `-` into
> *the previous directory I was in*, which is faster than having to remember, 
> then type, the full path.  This is a *very* efficient way of moving back 
> and forth between directories. The difference between `cd ..` and `cd -` is 
> that the former brings you *up*, while the latter brings you *back*. 
{: .callout}



