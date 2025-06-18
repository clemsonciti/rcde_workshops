# Working with files and directories

We now know how to explore files and directories, but how do we create them?

Let's change into the `shell-lesson-data` directory that you downloaded to your Desktop earlier.

```
$ cd ~/Desktop/shell-lesson-data
```

<!-- TODO add note about how to do so if you didn't -->

Next we’ll move to the `exercise-data/writing` directory and see what it contains:

```
$ cd exercise-data/writing/
$ ls
haiku.txt  LittleWomen.txt
```

## Viewing contents of a file

We see there are two text files. How can we see what's in them?

The simplest way is a command called `cat`. `cat` takes the name of a file as
it's argument, and prints the contents of that file:

```
$ cat haiku.txt
The Tao that is seen
Is not the true Tao, until
You bring fresh toner.

With searching comes loss
and the presence of absence:
"My Thesis" not found.

Yesterday it worked
Today it is not working
Software is like that.
```

Let's try it with `LittleWomen.txt`:

```
$ cat LittleWomen.txt
```

You'll see that this prints the entire contents of this long 19th century novel
to the screen. It's so much that you can't even scroll through it all!

There's a better way to view long files like this: the `less` command. As the
name suggests, this displays less of the file at once:

```
$ less LittleWomen.txt
```

Now you're in what's called a "pager" view of the file. Use `↑` and `↓` to move
line-by-line, or try `b` and `Spacebar` to skip up and down by a full page. To
quit and return to the shell prompt, press `q`.

<!-- TODO something about how you're still in the same world as the GUI: show accessing this stuff using Finder and Text Edit -->

## Creating directories

Let’s create a new directory called thesis using the command `mkdir thesis` (which has no output):

```
$ mkdir thesis
```

`mkdir` means "make directory".

```
$ ls
haiku.txt       LittleWomen.txt thesis
```

Since we just created it, it has nothing in it, which we can confirm with `ls`:

```
$ ls thesis
$
```

```{admonition} Challenge: mkdir and good names for directories
:class: tip

What do you think will happen if you run this command?

~~~
mkdir my directory
~~~

Think about it for a while, check `man mkdir` or `mkdir --help`, and decide what you think the result will be, then run the command.

What happened? Why do you think this is the case?

:::{admonition} Solution
:class: dropdown
This command creates *two* separate directories: `my` and `directory`:

~~~
$ mkdir my directory
$ ls
directory       haiku.txt       LittleWomen.txt my              thesis
~~~

You might have expected it to create a single directory called "my directory". It creates two because in the shell, spaces are used to separate multiple arguments. `mkdir` can create multiple directories at once if you pass it multiple arguments.

This teaches us a valuable lesson. When working with the shell, it's best to **avoid spaces in names of directories and files**. Because of the special meaning of space as the   argument separator, file and directory names with spaces can be difficult and confusing in the shell. Use characters like `-` or `_` instead.

:::
```

## Creating files

Let’s change our working directory to thesis using `cd`, then use a text editor called `nano` to create a file called `draft.txt`:

```
$ cd thesis
$ nano draft.txt
```

Let’s type in a few lines of text.

![Nano editor](../fig/intro_linux/nano-screenshot.png)

Once we’re happy with our text, we can press `Ctrl+O` (press the `Ctrl` or
`Control` key and, while holding it down, press the `O` key) to write our data
to disk. We will be asked to provide a name for the file that will contain our
text. Press `Return` to accept the suggested default of `draft.txt`.

Once our file is saved, we can use `Ctrl+X` to quit the editor and return to the
shell.

We can use `cat` to confirm that the file has been created with the right contents:

```
$ cat draft.txt
It's not publish or perish anymore,
it's share and thrive.
```

## Moving and renaming

Let's go "up" one directory, back to `shell-lesson-data/exercise-data/writing`:

```
$ cd ..
$ pwd
/Users/jjp366/Desktop/shell-lesson-data/exercise-data/writing
```

Now let's say we want to change the name of our `draft.txt` file. For this we
use the command `mv` (short for "move"):

```
$ mv thesis/draft.txt thesis/quotes.txt
```

The first argument tells mv what we’re "moving"; the second argument is where we
want it to go. In this case, we’re moving `thesis/draft.txt` to `thesis/quotes.txt`,
which is the same as renaming it.

We can see that it's been moved/renamed using `ls`:

```
$ ls thesis
quotes.txt
```

We can also use `mv` to move the file into a different directory, without
changing it's name. To do this, we pass a directory as the second argument. Here
we'll use the `.` shortcut to refer to the current directory:

```
$ mv thesis/quotes.txt .
```

This moves the `quotes.txt` file from
`shell-lesson-data/exercise-data/writing/thesis` to the current working
directory, `shell-lesson-data/exercise-data/writing`.

We can confirm that it worked by using `ls` to see that the `thesis` directory is now empty:

```
$ ls thesis
```

We can also see that `quotes.txt` is now present in our current directory:

```
$ ls
haiku.txt       LittleWomen.txt quotes.txt      thesis
```

```{admonition} Challenge: Moving files to a new folder
:class: tip

After running the following commands, Jamie realizes that she
put the files `sucrose.dat` and `maltose.dat` into the wrong folder. The
files should have been placed in the `raw` folder.

~~~bash
$ ls
analyzed raw
$ ls analyzed
fructose.dat glucose.dat maltose.dat sucrose.dat
$ cd analyzed
~~~

Fill in the blanks to move these files to the `raw` folder:

~~~bash
$ mv sucrose.data maltose.data ____/_____
~~~

:::{admonition} Solution
:class: dropdown
~~~
$ mv sucrose.data maltose.data ../raw
~~~
:::
```

## Copying

The `cp` command works like `mv`, except it copies a file instead of moving it.

```
$ cp quotes.txt thesis/quotations.txt
$ ls
haiku.txt       LittleWomen.txt quotes.txt      thesis
$ ls thesis
quotations.txt
```

We can also copy a directory and all its contents by using the `-r` option
(short for "recursive"). For example, we might want to backup a directory before
making a big change:

```
$ cp -r thesis thesis_backup
$ ls thesis thesis_backup
thesis:
quotations.txt

thesis_backup:
quotations.txt
```


```{admonition} Challenge: Moving and copying
:class: tip

What is the output of the last `ls` command in the sequence shown below?

~~~bash
$ pwd
/home/rammy/data
$ ls
proteins.dat
$ mkdir recombined
$ mv proteins.dat recombined/
$ cp recombined/proteins.dat ../proteins-saved.dat
$ ls
~~~

1. proteins-saved.dat recombined
2. recombined
3. proteins.dat recombined
4. proteins-saved.dat

:::{admonition} Solution
:class: dropdown
1. No, `proteins-saved.dat` is located at `/home/rammy/`
2. Yes
3. `proteins.dat` is located at `/home/rammy/data/recombined`
4. No, `proteins-saved.dat` is located at `/home/rammy/`
:::
```


## Removing

Let’s tidy up by removing the quotes.txt file we created. The Unix command we’ll
use for this is `rm` (short for "remove"):

```
$ rm quotes.txt
```

We can confirm the file is gone using `ls`:

```
$ ls
haiku.txt       LittleWomen.txt thesis          thesis_backup
```

If we try to remove the `thesis` directory using `rm thesis`, we get an error message:

```
$ rm thesis
rm: cannot remove 'thesis': Is a directory
```

This happens because `rm` by default only works on files, not directories.

`rm` can remove a directory *and all its contents* if we use the recursive
option `-r`, and it will do so *without any confirmation prompts*:

```
$ rm -r thesis
```

`rm -r` should be use with great caution, because it can permanently delete a
lot of files without asking for confirmation if you make a mistake.

```{admonition} Deleting is forever
:class: danger
Files deleted with `rm` cannot be recovered from a "trash bin" like files deleted using a GUI. Be very careful when deleting files using `rm`.
```

## Wildcards


`*` is a **wildcard**, which matches zero or more characters. This lets us
select subsets of files to work on using pattern matching.

Let's move to the `alkanes` directory to try it out:

```
$ cd ~/Desktop/shell-lesson-data/exercise-data/alkanes
$ ls
cubane.pdb  ethane.pdb  methane.pdb octane.pdb  pentane.pdb propane.pdb
```

This directory contains six files describing some simple organic molecules. The
`.pdb` extension indicates that these files are in Protein Data Bank format, a
text format that specifies the type and position of each atom in the molecule.

`*.pdb` matches `ethane.pdb`, `propane.pdb`, and every file that ends with `.pdb`:

```
$ ls *.pdb
cubane.pdb  ethane.pdb  methane.pdb octane.pdb  pentane.pdb propane.pdb
```

This is the same as if we just did `ls`, since every file in this directory ends in `.pdb`

`p*.pdb` only matches `pentane.pdb` and `propane.pdb`, because the ‘p’ at the front:

```
$ ls p*.pdb
pentane.pdb propane.pdb
```

`?` is also a wildcard, but it matches exactly one character. So:
- `?ethane.pdb` would match `methane.pdb`
- `*ethane.pdb` matches both `ethane.pdb`, and `methane.pdb`.


Wildcards can be used in combination with each other:
- `???ane.pdb` matches three characters followed by `ane.pdb`.
- `cubane.pdb`, `ethane.pdb`, `octane.pdb`.

Try the following commands. Try to guess what the output of each will be before you run it:

~~~bash
$ ls *t*ane.pdb
$ ls *t?ne.*
$ ls *t??ne.pdb
$ ls ethane.*
~~~


```{admonition} Challenge: wildcards
:class: tip

When run in the alkanes directory, which `ls` command(s) will produce this output?

~~~
ethane.pdb methane.pdb
~~~

1. `ls *t*ane.pdb`
2. `ls *t?ne.*`
3. `ls *t??ne.pdb`
4. `ls ethane.*`

:::{admonition} Solution
:class: dropdown
The solution is `3.`

`1.` shows all files whose names contain zero or more characters (`*`) followed by the letter `t`, then zero or more characters (`*`) followed by `ane.pdb`. This gives `ethane.pdb methane.pdb octane.pdb pentane.pdb`.

`2.` shows all files whose names start with zero or more characters (`*`) followed by the letter `t`, then a single character (`?`), then `ne.` followed by zero or more characters (`*`). This will give us `octane.pdb` and `pentane.pdb` but doesn’t match anything which ends in `thane.pdb`.

`3.` fixes the problems of `2.` by matching two characters (`??`) between t and ne. This is the solution.

`4.` only shows files starting with `ethane.`, so it will miss `methane.pdb`, because of the `m`.
:::
```