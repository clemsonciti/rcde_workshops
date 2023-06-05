# Example

## Configure Git

## Example

Let's create an example project folder with a couple of files in our home
directory:

```sh
$ mkdir ~/myproject
$ cd ~/myproject
$ echo "Hello World!" >> file1
$ echo "Go Tigers!" >> file2
$ ls
file1 file2
```

Now that we have some example content, we can start tracking this project with
Git. The `git init` command will create a new Git repository in the current
directory.

```sh
$ git init
Initialized empty Git repository in /home/tiger/myproject/.git/
```

This new repository has **no history** yet!
