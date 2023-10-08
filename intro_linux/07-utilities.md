# Shell Scripts


We are finally ready to see what makes the shell such a powerful programming 
environment. We are going to take the commands we repeat frequently and save 
them in files so that we can re-run all those operations again later by typing 
a single command. For historical reasons, a bunch of commands saved in a file 
is usually called a **shell script**, but make no mistake --- these are 
actually small programs.

Not only will writing shell scripts make your work faster, but also you won't 
have to retype the same commands over and over again. It will also make it more 
accurate (fewer chances for typos) and more reproducible. If you come back to 
your work later (or if someone else finds your work and wants to build on it), 
you will be able to reproduce the same results simply by running your script, 
rather than having to remember or retype a long list of commands.


```{admonition} 1. Our first shell script
:class: dropdown

Let's start by going back to `alkanes/` and creating a new file, `middle.sh` 
which will become our shell script:

~~~bash
cd alkanes
nano middle.sh
~~~

The command `nano middle.sh` opens the file `middle.sh` within the text editor 
'nano' (which runs within the shell). If the file does not exist, it will be 
created. We can use the text editor to directly edit the file by inserting the 
following line:

~~~
head -n 15 octane.pdb | tail -n 5
~~~

This is a variation on the pipe we constructed earlier, which selects lines 11-15 of
the file `octane.pdb`. Remember, we are *not* running it as a command just yet;
we are only incorporating the commands in a file.

Then we save the file (`Ctrl-O` in nano) and exit the text editor (`Ctrl-X` in nano).
Check that the directory `alkanes` now contains a file called `middle.sh`.

Once we have saved the file,
we can ask the shell to execute the commands it contains.
Our shell is called `bash`, so we run the following command:

~~~bash
bash middle.sh
~~~

Sure enough, our script's output is exactly what we would get if we ran that 
pipeline directly.

```


```{admonition} 2. Command line arguments
:class: dropdown

What if we want to select lines from an arbitrary file?
We could edit `middle.sh` each time to change the filename,
but that would probably take longer than typing the command out again
in the shell and executing it with a new file name.
Instead, let's edit `middle.sh` and make it more versatile:

~~~
nano middle.sh
~~~

Now, within "nano", replace the text `octane.pdb` with the special variable called `$1`:

~~~
head -n 15 "$1" | tail -n 5
~~~

Inside a shell script,
`$1` means 'the first filename (or other argument) on the command line'.
We can now run our script like this:

~~~bash
bash middle.sh octane.pdb
~~~

or on a different file like this:

~~~bash
$ bash middle.sh pentane.pdb
~~~

Currently, we need to edit `middle.sh` each time we want to adjust the range of
lines that is returned.
Let's fix that by configuring our script to instead use three command-line arguments.
After the first command-line argument (`$1`), each additional argument that we
provide will be accessible via the special variables `$1`, `$2`, `$3`,
which refer to the first, second, third command-line arguments, respectively.

Knowing this, we can use additional arguments to define the range of lines to
be passed to `head` and `tail` respectively:

~~~bash
nano middle.sh
~~~

~~~
head -n "$2" "$1" | tail -n "$3"
~~~

We can now run:

~~~bash
bash middle.sh pentane.pdb 15 5
~~~

By changing the arguments to our command, we can change our script's
behaviour:

~~~bash
bash middle.sh pentane.pdb 20 5
~~~

```


```{admonition} 3. Putting comments in the code
:class: dropdown

We can improve our script by adding some **comments** at the top:

~~~bash
nano middle.sh
~~~

~~~source
# Select lines from the middle of a file.
# Usage: bash middle.sh filename end_line num_lines
head -n "$2" "$1" | tail -n "$3"
~~~

A comment starts with a `#` character and runs to the end of the line.
The computer ignores comments, but they're invaluable for helping people (including your 
future self) understand and use scripts. The only caveat is that each time you 
modify the script, you should check that the comment is still accurate. 
An explanation that sends the reader in the wrong direction is worse than none at all.

```


```{admonition} 4. Multiple command line arguments
:class: dropdown

What if we want to process many files in a single pipeline?
For example, if we want to sort our `.pdb` files by length, we would type:

~~~bash
$ wc -l *.pdb | sort -n
~~~

because `wc -l` lists the number of lines in the files
(recall that `wc` stands for 'word count', adding the `-l` option means 'count lines' instead)
and `sort -n` sorts things numerically.
We could put this in a file,
but then it would only ever sort a list of `.pdb` files in the current directory.
If we want to be able to get a sorted list of other kinds of files,
we need a way to get all those names into the script.
We can't use `$1`, `$2`, and so on
because we don't know how many files there are.
Instead, we use the special variable `$@`,
which means,
'All of the command-line arguments to the shell script'.
We also should put `$@` inside double-quotes
to handle the case of arguments containing spaces
(`"$@"` is special syntax and is equivalent to `"$1"` `"$2"` ...).

Here's an example:

~~~bash
nano sorted.sh
~~~

~~~source
# Sort files by their length.
# Usage: bash sorted.sh one_or_more_filenames
wc -l "$@" | sort -n
~~~

~~~bash
bash sorted.sh *.pdb ../creatures/*.dat
~~~

~~~output
9 methane.pdb
12 ethane.pdb
15 propane.pdb
20 cubane.pdb
21 pentane.pdb
30 octane.pdb
163 ../creatures/basilisk.dat
163 ../creatures/minotaur.dat
163 ../creatures/unicorn.dat
596 total
~~~
```


```{admonition} 5. Challenge: List Unique Species
:class: dropdown

Leah has several hundred data files, each of which is formatted like this:

~~~source
2013-11-05,deer,5
2013-11-05,rabbit,22
2013-11-05,raccoon,7
2013-11-06,rabbit,19
2013-11-06,deer,2
2013-11-06,fox,1
2013-11-07,rabbit,18
2013-11-07,bear,1
~~~

An example of this type of file is given in
`shell-lesson-data/exercise-data/animal-counts/animals.csv`.

We can use the command `cut -d , -f 2 animals.csv | sort | uniq` to produce
the unique species in `animals.csv`.
In order to avoid having to type out this series of commands every time,
a scientist may choose to write a shell script instead.

Write a shell script called `species.sh` that takes any number of
filenames as command-line arguments and uses a variation of the above command
to print a list of the unique species appearing in each of those files separately.

:::{admonition} Solution
:class: dropdown

~~~bash
# Script to find unique species in csv files where species is the second data field
# This script accepts any number of file names as command line arguments

# Loop over all files
for file in $@
do
    echo "Unique species in $file:"
    # Extract species names
    cut -d , -f 2 $file | sort | uniq
done
~~~
:::
```


```{admonition} 6. Executable script
:class: dropdown

Edit the `middle.sh` file to be as follows:

~~~source
#!/bin/bash
# Select lines from the middle of a file.
# Usage: bash middle.sh filename end_line num_lines
head -n "$2" "$1" | tail -n "$3"
~~~

To make shell file executable, we need to change the permission on the file

~~~bash
chmod 755 middle.sh
./middle.sh
~~~

```