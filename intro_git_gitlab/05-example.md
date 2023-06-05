# Practice With a Local Repository

For this portion of the workshop, let's try working with a practice repository
on your computer.

## Configure Git

Before you can make commits, you will need to tell Git who you are, so it
attribute your work to you. You can do this using the `git config` command.

```sh
$ git config --global user.name "The Tiger"
$ git config --global user.email "imatiger@clemson.edu"
```

In this case, we are using the `--global` option to configure this option for
your entire user account. If you would like to do this on a per-repository
basis, you can run the commands inside your repository directory after
`git init` and omit the global flag.

## Getting Started

Let's create an example project folder with a couple of files in our home
directory:

```sh
$ mkdir ~/myproject
$ cd ~/myproject
$ echo "Hello World" > file1
$ echo "Go Tigers" > file2
$ echo "Clemson" > file3
$ ls
file1 file2 file3
```

### Initializing the Repository

Now that we have some example content, we can start tracking this project with
Git. The `git init` command will create a new Git repository in the current
directory.

```sh
$ git init
Initialized empty Git repository in /home/tiger/myproject/.git/
```

This new repository has **no history** yet!

```sh
$ git log
fatal: your current branch 'master' does not have any commits yet
```

Even though we had three files, (`file1`, `file2`, and `file3`) in the directory
at the time of `git init`, they have not yet been saved into the history of the
project. To do this, you will need to make a commit.

You can check the current status of the files using `git status`.

```sh
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	file1
	file2
	file3

nothing added to commit but untracked files present (use "git add" to track)
```

In this case, you can see that all three of the files are currently
**untracked** since they have not been committed to the repository before.

### Our First Commit

Let's move these files onto the stage using `git add` and then check the status
again.

```sh
$ git add file1
$ git add file2
$ git add file3
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   file1
	new file:   file2
	new file:   file3
```

After staging, these files are listed as **new files** under the **changes to be
committed** section.

Now, we are ready to make a commit and save a version of the code in the
repository using the `git commit` command. To help us remember why these changes
were made later, we'll add a descriptive message to the commit.

```sh
[master (root-commit) eaf6009] Created three example files.
 3 files changed, 3 insertions(+)
 create mode 100644 file1
 create mode 100644 file2
 create mode 100644 file3
```

If you check the `git log` again, you will now see one commit in the history.

```sh
$ git log
commit eaf6009a08f24c6a90f0658d060bf5411fb64fba (HEAD -> master)
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 10:39:44 2023 -0400

    Created three example files.
```

If you check the `git status` again, you will see that there are no changes,
since nothing has changed since the last version.

```sh
$ git status
On branch master
nothing to commit, working tree clean
```

### Making a Change

Now, let's modify one of the original files that we committed. We can add a new
line to `file3` that says "University" so we have the full school name.

```sh
$ cat file3
Clemson
$ echo "University" >> file3
$ cat file3
Clemson
University
```

After this change, we can check the status again.

```sh
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   file3

no changes added to commit (use "git add" and/or "git commit -a")
```

Notice that this time, the file is listed as **modified**, since we have changed
it since the last commit. However, since we have not **staged** the file yet, it
is listed as **changes not staged for commit**.

Let's stage this change to be committed.

```sh
$ git add file3
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   file3
```

Now, you can see that the change is listed under **changes to be committed**. We
are ready to make our second commit!

```sh
$ git commit -m "Write the full school name in the file."
[master af39f95] Write the full school name in the file.
 1 file changed, 1 insertion(+)
```

We can check the status and log to see the results.

```sh
$ git status
On branch master
nothing to commit, working tree clean
$ git log
commit af39f9579b71c7ae9551761ffbb929e5cae75b1f (HEAD -> master)
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 11:09:55 2023 -0400

    Write the full school name in the file.

commit eaf6009a08f24c6a90f0658d060bf5411fb64fba
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 10:39:44 2023 -0400

    Created three example files.
```

## Deleting a File

Now, let's delete a file that we have tracked in Git. You can use the same
command you usually would to remove the file.

```sh
$ ls
file1 file2 file3
$ rm file2
remove file2? y
$ ls
file1 file3
```

After removing the file, we can check the status again.

```sh
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    file2

no changes added to commit (use "git add" and/or "git commit -a")
```

We can see the **deleted** file listed under **changes not staged for commit**.

To stage the change, we must use `git add` again. This may seem
counterintuitive, since you are "adding" a file that you just "removed" from the
directory.

However, it is important to remember that you are adding **changes** to the
commit. We are adding the "change of deletion" to the commit.

```sh
$ git add file2
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    file2
```

You can see that now the **deleted** change is now under **changes to be
committed**. We can now make our commit, just like we have with previous
changes.

```sh
$ git commit -m "Remove unnecessary file."
[master 23c977f] Remove unnecessary file.
 1 file changed, 1 deletion(-)
 delete mode 100644 file2
```

Let's take a look at the file list, status of the repository, and log again.

```sh
$ ls
file1 file3
$ git status
On branch master
nothing to commit, working tree clean
$ git log
commit 23c977fc6ff575c43c8e65ddb1ba2ad2f90be394 (HEAD -> master)
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 11:15:26 2023 -0400

    Remove unnecessary file.

commit af39f9579b71c7ae9551761ffbb929e5cae75b1f
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 11:09:55 2023 -0400

    Write the full school name in the file.

commit eaf6009a08f24c6a90f0658d060bf5411fb64fba
Author: The Tiger <imatiger@clemson.edu>
Date:   Mon Jun 5 10:39:44 2023 -0400

    Created three example files.
```
