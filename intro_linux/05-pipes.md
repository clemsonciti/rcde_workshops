# Pipes and Redirection


```{admonition} 1. Overview
:class: dropdown

- Now that we know a few basic commands, we can finally look at the shell's most 
powerful feature: the ease with which it lets us combine existing programs in new ways.
- We'll start with the directory `shell-lesson-data/exercise-data/alkanes`
that contains six files describing some simple organic molecules.
The `.pdb` extension indicates that these files are in Protein Data Bank format,
a simple text format that specifies the type and position of each atom in the molecule.

~~~bash
cd ~/shell-lesson-data/exercise-data/alkanes
ls
~~~

- Let's run an example command:

~~~bash
wc cubane.pdb
~~~

~~~output
20  156 1158 cubane.pdb
~~~

- `wc` is the 'word count' command: it counts the number of lines, words, and characters 
in files (returning the values in that order from left to right).
- If we run the command `wc *.pdb`, the `*` in `*.pdb` matches zero or more characters,
so the shell turns `*.pdb` into a list of all `.pdb` files in the current directory:

~~~bash
wc *.pdb
~~~

~~~output
  20  156  1158  cubane.pdb
  12  84   622   ethane.pdb
   9  57   422   methane.pdb
  30  246  1828  octane.pdb
  21  165  1226  pentane.pdb
  15  111  825   propane.pdb
 107  819  6081  total
~~~

If we run `wc -l` instead of just `wc`, the output shows only the number of lines per file:

~~~bash
$ wc -l *.pdb
~~~

~~~output
  20  cubane.pdb
  12  ethane.pdb
   9  methane.pdb
  30  octane.pdb
  21  pentane.pdb
  15  propane.pdb
 107  total
~~~

```


```{admonition} 2. Capturing output from commands
:class: dropdown

Which of these files contains the fewest lines?
It's an easy question to answer when there are only six files,
but what if there were 6000?

**Redirection**

~~~bash
wc -l *.pdb > lengths.txt
~~~

The greater than symbol, `>`, tells the shell to **redirect** the command's output to a
file instead of printing it to the screen. This command prints no screen output, because
everything that `wc` would have printed has gone into the file `lengths.txt` instead.
If the file doesn't exist prior to issuing the command, the shell will create the file.
If the file exists already, it will be silently overwritten, which may lead to data loss.
Thus, **redirect** commands require caution.

`ls lengths.txt` confirms that the file exists:

~~~bash
ls lengths.txt
~~~

~~~output
lengths.txt
~~~

We can now send the content of `lengths.txt` to the screen using `cat lengths.txt`.
The `cat` command gets its name from 'concatenate' i.e. join together,
and it prints the contents of files one after another.
There's only one file in this case,
so `cat` just shows us what it contains:

~~~bash
cat lengths.txt
~~~

~~~output
  20  cubane.pdb
  12  ethane.pdb
   9  methane.pdb
  30  octane.pdb
  21  pentane.pdb
  15  propane.pdb
 107  total
~~~

```


```{admonition} 3. Filtering output
:class: dropdown

Next we'll use the `sort` command to sort the contents of the `lengths.txt` file.

::::{admonition} What Does `sort -n` Do?
:class: dropdown

View the file `shell-lesson-data/exercise-data/numbers.txt`:

~~~bash
cd ~/shell-lesson-data/exercise-data/
cat numbers.txt
~~~

Run `sort` and then `sort -n` on the file, then compare the outputs


If we run `sort` on this file, the output is:

~~~bash
sort numbers.txt
sort -n numbers.txt
~~~

::::

Running `sort` does *not* change the file; instead, it sends the sorted result to the screen:

~~~bash
sort -n lengths.txt
~~~

We can put the sorted list of lines in another temporary file 
called `sorted-lengths.txt` by putting `> sorted-lengths.txt` 
after the command, just as we used `> lengths.txt` to put the 
output of `wc` into `lengths.txt`. Once we've done that, we can 
run another command called `head` to get the first few lines in 
`sorted-lengths.txt`:

~~~bash
sort -n lengths.txt > sorted-lengths.txt
head -n 1 sorted-lengths.txt
~~~

Using `-n 1` with `head` tells it that we only want the first line 
of the file; `-n 20` would get the first 20, and so on.
Since `sorted-lengths.txt` contains the lengths of our files ordered 
from least to greatest, the output of `head` must be the file with 
the fewest lines.

```


```{admonition} 4. Appending to the same file
:class: dropdown

- We have seen the use of `>`, but there is a similar operator `>>`
which works slightly differently.
- We can use the `echo` command to print strings e.g.

~~~bash
echo The echo command prints text
~~~

Now test the commands below to reveal the difference between the two operators:

~~~bash
echo hello > testfile01.txt
echo hello > testfile01.txt
echo hello >> testfile02.txt
echo hello >> testfile02.txt
cat textfile01.txt
cat textfile02.txt
~~~

```


```{admonition} 5. Passing output to another command
:class: dropdown

In our example of finding the file with the fewest lines,
we are using two intermediate files `lengths.txt` and `sorted-lengths.txt` to store output.
This is a confusing way to work because
even once you understand what `wc`, `sort`, and `head` do,
those intermediate files make it hard to follow what's going on.
We can make it easier to understand by running `sort` and `head` together:

~~~bash
sort -n lengths.txt | head -n 1
~~~

The vertical bar, `|`, between the two commands is called a **pipe**.
It tells the shell that we want to use
the output of the command on the left
as the input to the command on the right.

This has removed the need for the `sorted-lengths.txt` file.

```


```{admonition} 6. Combining multiple commands
:class: dropdown

Nothing prevents us from chaining pipes consecutively.
We can for example send the output of `wc` directly to `sort`,
and then send the resulting output to `head`.
This removes the need for any intermediate files.

We'll start by using a pipe to send the output of `wc` to `sort`:

~~~bash
wc -l *.pdb | sort -n
~~~

We can then send that output through another pipe, to `head`, so that the full pipeline becomes:

~~~bash
wc -l *.pdb | sort -n | head -n 1
~~~

This is exactly like a mathematician nesting functions like *log(3x)*
and saying 'the log of three times *x*'. 
In our case, the algorithm is 'head of sort of line count of `*.pdb`'.

The redirection and pipes used in the last few commands are illustrated below:

![Redirects and Pipes](../fig/redirects-and-pipes.svg)

```


```{admonition} 7. Challenge: Piping Commands Together
:class: dropdown

In our current directory, we want to find the 3 files which have the 
least number of lines. Which command listed below would work?

1. `wc -l * > sort -n > head -n 3`
2. `wc -l * | sort -n | head -n 1-3`
3. `wc -l * | head -n 3 | sort -n`
4. `wc -l * | sort -n | head -n 3`

:::{admonition} Solution
:class: dropdown

Option 4 is the solution.
The pipe character `|` is used to connect the output from one command to
the input of another.
`>` is used to redirect standard output to a file.
Try it in the `shell-lesson-data/exercise-data/alkanes` directory!
:::
```


```{admonition} 8. Tools designed to work together
:class: dropdown

This idea of linking programs together is why Unix has been so successful.
Instead of creating enormous programs that try to do many different things,
Unix programmers focus on creating lots of simple tools that each do one job well,
and that work well with each other.

This programming model is called 'pipes and filters'.
We've already seen pipes;
a **filter** is a program like `wc` or `sort`
that transforms a stream of input into a stream of output.
Almost all of the standard Unix tools can work this way.
Unless told to do otherwise,
they read from standard input,
do something with what they've read,
and write to standard output.

The key is that any program that reads lines of text from standard input
and writes lines of text to standard output
can be combined with every other program that behaves this way as well.
You can *and should* write your programs this way
so that you and other people can put those programs into pipes to multiply their power.

```


```{admonition} 9. Pipe Reading Comprehension
:class: dropdown

A file called `animals.csv` (in the `shell-lesson-data/exercise-data/animal-counts` folder)
contains the following data:

~~~bash
2012-11-05,deer,5
2012-11-05,rabbit,22
2012-11-05,raccoon,7
2012-11-06,rabbit,19
2012-11-06,deer,2
2012-11-06,fox,4
2012-11-07,rabbit,16
2012-11-07,bear,1
~~~

What text passes through each of the pipes and the final redirect in the pipeline below?
Note, the `sort -r` command sorts in reverse order.

~~~bash
$ cat animals.csv | head -n 5 | tail -n 3 | sort -r > final.txt
~~~

Hint: build the pipeline up one command at a time to test your understanding

:::{admonition} Solution
:class: dropdown

The `head` command extracts the first 5 lines from `animals.csv`.
Then, the last 3 lines are extracted from the previous 5 by using the `tail` command.
With the `sort -r` command those 3 lines are sorted in reverse order.
Finally, the output is redirected to a file: `final.txt`.
The content of this file can be checked by executing `cat final.txt`.
The file should contain the following lines:

~~~
2012-11-06,rabbit,19
2012-11-06,deer,2
2012-11-05,raccoon,7
~~~

:::
```


```{admonition} 10. Which Pipe?
:class: dropdown

The file `animals.csv` contains 8 lines of data formatted as follows:

~~~
2012-11-05,deer,5
2012-11-05,rabbit,22
2012-11-05,raccoon,7
2012-11-06,rabbit,19
...
~~~

The `uniq` command has a `-c` option which gives a count of the
number of times a line occurs in its input.  Assuming your current
directory is `shell-lesson-data/exercise-data/animal-counts`,
what command would you use to produce a table that shows
the total count of each type of animal in the file?

1. `sort animals.csv | uniq -c`
2. `sort -t, -k2,2 animals.csv | uniq -c`
3. `cut -d, -f 2 animals.csv | uniq -c`
4. `cut -d, -f 2 animals.csv | sort | uniq -c`
5. `cut -d, -f 2 animals.csv | sort | uniq -c | wc -l`

:::{admonition} Solution
:class: dropdown

Option 4. is the correct answer.
If you have difficulty understanding why, try running the commands, or sub-sections of
the pipelines (make sure you are in the `shell-lesson-data/exercise-data/animal-counts`
directory).

:::
```


