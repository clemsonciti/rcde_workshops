# Git Commands

This sheet provides a quick reference for what the basic git commands are and
what they do.

## `git init`

The `git init` command will initialize a new Git repository in the current
directory. This command should be used

## `git status`

The `git status` command will show you the current status of the repository.

If the stage is not empty, a list of staged files will be shown.

If there are any modified files that have not been staged, a list of them will
also be shown.

## `git add`

The `git add` command will add a file to the stage.

For example, to stage the file `abc.txt`, you could run `git add abc.txt`. You
can also add all files by running `git add -A`.

## `git commit`

The `git commit` command will create a new commit on the repository.

It is a good idea to provide a message explaining your changes, like this:

```sh
git commit -m "Added images for the ski lift and cypress trees."
```

## `git log`

The `git log` command shows an overview of previous commits made to the
repository and their messages.

## `git push`

The `git push` command will send commits from your local computer to the remote
server you have configured.

## `git fetch`

The `git fetch` command will search for information about new commits on the
remote server, but will **not** integrate the changes into your copy.

## `git pull`

The `git pull` command will download new commits from the remote server you have
selected to your local computer and integrate the changes into your copy.

## `git merge`

The `git merge` command can be used to integrate changes from another branch
into yours. For example, `git merge origin/feature-calculator`.

## `git help`

For a more comprehensive list of commands and what they do, you can use the
`git help` command.

This command can also retrieve manual pages for other Git commands. For example,
if you would like to know more about `git clone`, you can run `git help clone`.
