# Loop

**Loops** are a programming construct which allow us to repeat a command 
or set of commands for each item in a list.
As such they are key to productivity improvements through automation.
Similar to wildcards and tab completion, using loops also reduces the
amount of typing required (and hence reduces the number of typing mistakes).

Suppose we have several hundred genome data files named `basilisk.dat`, `minotaur.dat`, 
and `unicorn.dat`. For this example, we'll use the `exercise-data/creatures` 
directory which only has three example files, but the principles can be 
applied to many many more files at once.

The structure of these files is the same: the common name, classification, 
and updated date are presented on the first three lines, with DNA sequences 
on the following lines. Let's look at the files:

~~~bash
head -n 5 basilisk.dat minotaur.dat unicorn.dat
~~~

We would like to print out the classification for each species, which is 
given on the second line of each file. For each file, we would need to execute the 
command `head -n 2` and pipe this to `tail -n 1`. We'll use a loop to solve this 
problem, but first let's look at the general form of a loop, using the pseudo-code below:

~~~bash
# The word "for" indicates the start of a "For-loop" command
for thing in list_of_things 
#The word "do" indicates the start of job execution list
do 
    # Indentation within the loop is not required, but aids legibility
    operation_using/command $thing 
# The word "done" indicates the end of a loop
done  
~~~

and we can apply this to our example like this:

~~~bash
$ for filename in basilisk.dat minotaur.dat unicorn.dat
> do
>     echo $filename
>     head -n 2 $filename | tail -n 1
> done
~~~

~~~output
basilisk.dat
CLASSIFICATION: basiliscus vulgaris
minotaur.dat
CLASSIFICATION: bos hominus
unicorn.dat
CLASSIFICATION: equus monoceros
~~~

```{admonition} 1. Write your own loop
:class: dropdown

How would you write a loop that echoes all 10 numbers from 0 to 9?

~~~bash
$ for loop_variable in 0 1 2 3 4 5 6 7 8 9
> do
>     echo $loop_variable
> done
~~~

```


```{admonition} 2. Variables in Loops
:class: dropdown

This exercise refers to the `shell-lesson-data/exercise-data/alkanes` directory.
`ls *.pdb` gives the following output:

~~~bash
cd ~/shell-lesson-data/exercise-data/alkanes
ls *.pdb
~~~

What is the output of the following code?

~~~bash
$ for datafile in *.pdb
> do
>     ls *.pdb
> done
~~~

What is the output of the following code?

~~~bash
$ for datafile in *.pdb
> do
>     ls $datafile
> done
~~~

Why do these two loops give different outputs?

```


```{admonition} 3. Limiting Sets of Files
:class: dropdown

What would be the output of running the following loop in the
`shell-lesson-data/exercise-data/alkanes` directory?

~~~bash
$ for filename in c*
> do
>     ls $filename
> done
~~~

1. No files are listed.
2. All files are listed.
3. Only `cubane.pdb`, `octane.pdb` and `pentane.pdb` are listed.
4. Only `cubane.pdb` is listed.

:::{admonition} Solution
:class: dropdown

4 is the correct answer. `*` matches zero or more characters, so any file name starting with
the letter c, followed by zero or more other characters will be matched.

:::
```


```{admonition} 4. Saving to a File in a Loop - Part One
:class: dropdown

In the `shell-lesson-data/exercise-data/alkanes` directory, what is the effect 
of this loop?

~~~bash
for alkanes in *.pdb
do
    echo $alkanes
    cat $alkanes > alkanes.pdb
done
~~~

1. Prints `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb` and
  `propane.pdb`, and the text from `propane.pdb` will be saved to a file called `alkanes.pdb`.
2. Prints `cubane.pdb`, `ethane.pdb`, and `methane.pdb`, and the text from all three files
  would be concatenated and saved to a file called `alkanes.pdb`.
3. Prints `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, and `pentane.pdb`,
  and the text from `propane.pdb` will be saved to a file called `alkanes.pdb`.
4. None of the above.

:::{admonition} Solution
:class: dropdown

1. The text from each file in turn gets written to the `alkanes.pdb` file.
  However, the file gets overwritten on each loop iteration, so the final content of
  `alkanes.pdb`
  is the text from the `propane.pdb` file.
  
:::
```


```{admonition} 5. Saving to a File in a Loop - Part Two
:class: dropdown

Also in the `shell-lesson-data/exercise-data/alkanes` directory,
what would be the output of the following loop?

~~~bash
for datafile in *.pdb
do
    cat $datafile >> all.pdb
done
~~~

1. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, and
  `pentane.pdb` would be concatenated and saved to a file called `all.pdb`.
2. The text from `ethane.pdb` will be saved to a file called `all.pdb`.
3. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb`
  and `propane.pdb` would be concatenated and saved to a file called `all.pdb`.
4. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb`
  and `propane.pdb` would be printed to the screen and saved to a file called `all.pdb`.

:::{admonition} Solution
:class: dropdown

3 is the correct answer. `>>` appends to a file, rather than overwriting it with the redirected
output from a command.
Given the output from the `cat` command has been redirected, nothing is printed to the screen.

:::
```


```{admonition} 6. Spaces in Names
:class: dropdown

Spaces are used to separate the elements of the list
that we are going to loop over. If one of those elements
contains a space character, we need to surround it with
quotes, and do the same thing to our loop variable.
Suppose our data files are named:

~~~bash
red dragon.dat
purple unicorn.dat
~~~

To loop over these files, we would need to add double quotes like so:

~~~bash
$ for filename in "red dragon.dat" "purple unicorn.dat"
> do
>     head -n 100 "$filename" | tail -n 20
> done
~~~

It is simpler to avoid using spaces (or other special characters) in filenames.

The files above don't exist, so if we run the above code, the `head` command will be unable
to find them; however, the error message returned will show the name of the files it is
expecting:

~~~
head: cannot open ‘red dragon.dat' for reading: No such file or directory
head: cannot open ‘purple unicorn.dat' for reading: No such file or directory
~~~

Try removing the quotes around `$filename` in the loop above to see the effect of the quote
marks on spaces. Note that we get a result from the loop command for unicorn.dat
when we run this code in the `creatures` directory:

```output
head: cannot open ‘red' for reading: No such file or directory
head: cannot open ‘dragon.dat' for reading: No such file or directory
head: cannot open ‘purple' for reading: No such file or directory
CGGTACCGAA
AAGGGTCGCG
CAAGTGTTCC
...
```

