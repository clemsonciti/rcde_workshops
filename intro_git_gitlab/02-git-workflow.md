# Git Version Control

Now that you understand the foundations of version control and the motivations
behind it, let's talk about one of the most popular version control systems:
**Git**.

## About Git

Git was created by Linus Torvalds in 2005 to help Linux kernel developers
collaborate on the source code. It is designed to be a **distributed** verison
control system, meaning that all copies contain a full record of the history.

The distributed design allows users to work **without a constant connection to a
central server**. Furthermore, this makes many operations **fast** since your
computer has everything it needs to perform operations locally without waiting
for information from the network.

## Repositories

Working with Git all starts with a **repository**. You can think of a repository
as a "project folder" on your computer, which contains:

- the files and directories for your project
- the **complete** history of the changes to those files and directories

## History

In Git, each **version** of your repository is called a **commit**. The history
of your project is recorded as a series of these commits.

```{figure} ../fig/intro_git_gitlab/git_history.png
---
width: 80%
---
Diagram showing history of a repository in Git as a series of commits. <br />
Source: _Pro Git_ by Scott Chacon and Ben Straub, licensed under
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
```

To save space, Git will not save a copy of each file in your repository in every
commit. Instead, each commit will record what has changed since the commit
before it.

## States of a File

Git does **not** automatically save a version for you each time you save a file
inside your repository. Instead, you must tell Git what changes you want to
include in the next version and make a commit.

To help users know which files will be included in the next version, it can
report the status of each file in the repository. Users must understand the
various states that a file can be in.

```{figure} ../fig/intro_git_gitlab/git_states_of_a_file.png
---
width: 80%
---
Diagram showing the states of a file in Git. <br /> Source: _Pro Git_ by Scott
Chacon and Ben Straub, licensed under
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
```

## The Stage

## Commits