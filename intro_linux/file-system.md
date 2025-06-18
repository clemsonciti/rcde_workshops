# Navigating files and directories

The **filesystem** is the part of your computer's operating system that
organized stored data into files and directories (a.k.a. folders[^directories]).
Files hold data, and directories hold files and other directories.

Some of the most common and useful shell commands are used to look at and modify
 the filesystem.

```{admonition} Other ways to navigate the filesystem
:class: note
The word "filesystem" might sound unfamiliar, but you've probably worked with the filesystem before without realizing it. Most operating systems come with GUI apps for filesystem navigation: Finder on macOS, or File Explorer on Windows. Anytime you use these apps (e.g. double-clicking on a folder to open it, or dragging files into a different folder to move them )you're using the filesystem.

The shell commands we're about to learn are just a different way of doing the same thing.
```

## Where are we?

First, let’s find out where we are. Directories are like places. Whenever we're
using the shell, we are in exactly one place called our **current working
directory**. Commands mostly read and write files in the current working
directory, i.e. ‘here’, so knowing where you are before running a command is
important.

To find out where you are, you use the `pwd` command (`pwd` stands for "print
working directory"):

```
$ pwd
```

This will print the **path** of the current working directory:

```
$ pwd
/Users/jjp366
```

A path is a way of describing a location in the filesystem. It's a list of
directories separated by `/` characters. The first `/` represents the root
directory, which is the top-level directory that contains everything else.

In the example above, the path is `/Users/jjp366`, which means we're in the
`jjp366` directory, which is inside the `Users` directory, which is inside the
root directory.

```{figure} ../fig/intro_linux/file_system/home-directories.svg
---
name: home-directories-fig
---
A diagram of an example filesystem.
```

The filesystem looks like an upside down tree, with the root directory at the
base, and the other directories branching out from it[^tree].

Typically, when you first open a shell, you will be in your **home directory**,
which is a directory assigned to you to keep your personal files[^files] in. The
name of the directory is your username. The rest of the path will look a little
different, depending on your operating system.

## What's here?

To see what's in your current directory, use the `ls` (short for "list") command:

```
$ ls
Applications Documents    Library      Music        Public
Desktop      Downloads    Movies       Pictures
```

This is the same list as what you'll see if you open your home directory in Finder or File Explorer.

## How do we go somewhere else?

To change the current working directory, use the `cd` (short for "change directory") command.

Let's change to the highest-level, or, "root" directory of the filesystem, and see what's there:

<!-- TODO I'm not convinced `/` is the best place to cd to here. What's positive is that everyone will definitely have it. What's negative is that it's a weird and confusing path. -->

```
$ cd /
```

Your prompt might change after running this command to show that you're in a
different working directory. Most prompts include the working directory so it's
easy to see where you are at a glance.

We can confirm that we've changed working directories by running `pwd` again and
seeing that the output is different:

```
$ pwd
/
```

And run `ls` to see what files are here:

```
$ ls
Applications dev          Library      private      tmp          var
bin          etc          Network      sbin         Users        Volumes
cores        home         opt          System       usr
```

## Using arguments and options

Most commands accept input in the form of **arguments** and **options** (also
called **flags**), which can change their behavior.

### Arguments

Arguments are inputs that a command operates on. We just used our first argument in our `cd` command:

```
$ cd /
```

Arguments are separated from commands by spaces. So here `cd` is the command,
and `/` is the argument. Arguments have different meanings to different
commands. For `cd`, the first argument is the directory we want to change to.

Let's pass a different argument to change back to the home directory. The path
to your home directory will be different depending on your operating system,
username, etc. Fortunately, there's a shortcut we can use. The `~` ("tilde")
character means "my home directory". So to go back to our home directory, we can
use:

```
$ cd ~
$ pwd
/Users/jjp366
```

#### Other shortcuts

The shell supports a few more of these shortcuts in addition to `~`.

`..` means “the directory containing this one”. This is called the **parent directory**. For example:

```
$ pwd
/Users/jjp366
$ cd ..
$ pwd
/Users
```

We can see that `cd ..` moved us "up" one directory to `/Users`.

`.` means the current directory, so `cd .` moves us to where we already are (does nothing):

```
$ pwd
/Users
$ cd .
$ pwd
/Users
```

This might seem useless now, but we will see some uses for it shortly.

### Options

Options (also called flags) are settings that modify the behavior of a command.
They typically start with `-` or `--`. They're similar to the settings menu in a
GUI program. Options change how a command works, whereas arguments give the
command the data it needs to function.

A common example is the `-l` option to `ls`. This tells `ls` to give its output
in "long" format, which contains much more detail:

```
$ ls -l
[Desktop] ls -l
total 30608
total 6208
-rw-------@  1 jjp366  DREXEL\Domain Users   202057 Mar 19 15:57 NW-19207 Estimate IT Approved by Network Mgmt..pdf
-rw-r--r--@  1 jjp366  DREXEL\Domain Users     4736 May  6 15:49 quotas.csv
drwxr-xr-x  24 jjp366  DREXEL\Domain Users      768 Jun 16 15:46 screenshots
-rw-r--r--@  1 jjp366  DREXEL\Domain Users  2964549 Mar 28 10:36 URCF.pdf
```

Some of this output is about properties that we do not cover in this workshop
(such as file permissions and ownership). It still has some useful output
though, like the modification time and file size.

<!-- TODO have a picture showing where those two things are -->

```{admonition} Challenge: exploring more ls options
:class: hint, dropdown

You can use two options at the same time. What does the `-h` option when used together with the `-l` option? Like this:

~~~
$ ls -l -h
~~~

:::{admonition} Solution
:class: dropdown

If you use both the `-h` option and the `-l` option, this makes the file
size *human readable*, i.e. displaying something like 5.3K instead of 5369.
:::
```

```{admonition} Challenge: listing in reverse chronological order
:class: hint, dropdown

- By default, ls lists the contents of a directory in alphabetical
order by name. The command `ls -t` lists items by time of last change
instead of alphabetically. The command `ls -r` lists the contents of a
directory in reverse order.
- Which file is displayed last when you combine the `-t` and `-r` options?
Hint: You may need to use the -l option to see the last changed dates.

:::{admonition} Solution
:class: dropdown

The most recently changed file is listed last when using `-rt`.
This can be very useful for finding your most recent edits or
checking to see if a new output file was written.
:::
```


```{admonition} Challenge: ls reading comprehension
:class: hint, dropdown

- Using the filesystem diagram below.
- If `pwd` displays `/Users/backup` and  `-r` tells `ls` to display things in
reverse order, what command(s) will result in the following output:

~~~bash
pnas_sub pnas_final original
~~~

![Change directories](../fig/intro_linux/file_system/filesystem-challenge.svg)

1. `ls pwd`
2. `ls -r`
3. `ls -r /Users/backup`

:::{admonition} Solution
:class: dropdown

1. No: `pwd` is not the name of a directory.
2. Yes: `ls` without directory argument lists files and directories in the current directory.
3. Yes: uses the absolute path explicitly.
:::
```

## Getting help

`ls` has lots of other options. There are two common ways to find out how to use
a command and what options it accepts—**depending on your environment, you might
find that only one of these ways works**:

1. The `--help` flag (on Linux and Git Bash for Windows):

```
$ ls --help
```

2. The "manual page", accessed with the `man` command:

```
$ man ls
```

Running `ls --help` will print help information:

```
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                               e.g., '--block-size=M'; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
 ...
```

`man ls` will instead turn your terminal into a page with a description of the ls
command and its options.

To navigate through the man pages, use `↑` and `↓` to move line-by-line,
or try `b` and `Spacebar` to skip up and down by a full page.

To quit the man pages, press `q`.


```{admonition} General syntax of a shell command
:class: note

![Structure of shell command](../fig/intro_linux/file_system/shell_command_syntax.svg)

- `ls` is the command, with an option `-F` and an argument `/`.
- **Option**:
  - either start with a single dash (`-`) or two dashes (`--`),
  - change the behavior of a command.
  - can be referred to as either `switches` or `flags`.
- **Arguments** tell the command what to operate on (e.g. files and directories).
- Sometimes `options` and `arguments` are referred to as parameters.
  - The shell is in fact just a process/function and these `options` and `arguments`
  are being passed as parameters to the shell's function that is responsible for
  executing the **command**.
- A command can be called with more than one option and more than one argument, but a
command doesn’t always require an argument or an option.
- Each part is separated by spaces: if you omit the space between `ls` and `-F` the
shell will look for a command called `ls-F`, which doesn’t exist.
- Capitalization can be important.
  - `ls -s` will display the size of files and directories alongside the names
  - `ls -S` will sort the files and directories by size

```

[^directories]: "Directory" is a more technical term for "folder". Folders are
    usually called directories in technical computing contexts like using the
    shell or programming, but they're the same thing.
[^files]: As opposed to files that are part of the operating system, or other
    users' files.
[^tree]: This "tree" metaphor is where the name "root" for the topmost directory comes from.