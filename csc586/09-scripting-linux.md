# Linux Scripting

```{dropdown} 1. Pipes and Filters     
 
- It is possible to combine multiple Linux commands into one
- Settings:
  - Data are stored in `shell-lesson-data/excercise-data/proteins` on `molly`. 
  - Data files have `.pdb` extension. 
- Question:
  - Which of these files contains the fewest lines?

```

```{dropdown} 2. Capturing output from commands

- SSH to `molly`. 
- Run the following commands to prepare the environment.

~~~
$ clear
$ cd
$ pwd
$ cd ~/shell-lesson-data/exercise-data/proteins
$ ls -l *.pdb
~~~

:::{image} ../fig/csc586//09-scripting-linux/pdb-list.png
:alt: List files in current directory
:class: bg-primary mb-1
:height: 200px
:align: center
:::

- To get counts of characters, words, and lines in a file, we use `wc`. 

~~~
$ man wc
$ wc *.pdb
$ wc -l *.pdb
~~~

:::{image} ../fig/csc586//09-scripting-linux/wc-cli.png
:alt: Running wc command
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- We can use the `>` to redirect output to a file
  - `>` redirects output and creates a new file. 
  - `>>` appends output to a file (if the file already exists, else creates a new file)

~~~
$ ls
$ wc -l *.pdb > lengths.txt
$ ls
$ cat lengths.txt
$ wc -l *.pdb >> lengths.txt
$ cat lengths.txt
$ wc -l *.pdb > lengths.txt
$ cat lengths.txt
~~~


:::{image} ../fig/csc586//09-scripting-linux/wc-redirect.png
:alt: Redirect outputs to a file
:class: bg-primary mb-1
:height: 600px
:align: center
:::

```

```{dropdown} 3. Filtering output

- We can sort the contents of `lengths.txt` using `sort`

~~~
$ man sort
~~~


::::{admonition} Challenge: what does `sort -n` do?
:class: note

- Explain what does `-n` do by observing the following two commands

~~~
$ sort ~/shell-lesson-data/exercise-data/numbers.txt
10
19
2
22
6
~~~

~~~
$ sort -n ~/shell-lesson-data/exercise-data/numbers.txt
2
6
10
19
22
~~~

:::{dropdown} Solution
- The `-n` option specifies a numerical rather than an alphanumerical sort.
:::
::::

- Let's look at `lengths.txt`:

~~~
$ sort -n lengths.txt
$ sort -n lengths.txt > sorted-lengths.txt
$ cat sorted-lengths.txt
~~~

:::{image} ../fig/csc586//09-scripting-linux/sort-cli.png
:alt: Redirect sorted outputs to a file
:class: bg-primary mb-1
:height: 200px
:align: center
:::

- We can use the `head` command to get the first line

~~~
$ head -n 1 sorted-lengths.txt
~~~

:::{image} ../fig/csc586//09-scripting-linux/head-cli.png
:alt: Run head to get the first line
:class: bg-primary mb-1
:height: 50px
:align: center
:::

```

```{dropdown} 4. Passing output to another command

- We used intermediate files to store output. We can use a pipe (`|`) to 
combine them together. 

~~~
$ sort -n lengths.txt | head -n 1
~~~

- We can combine multiple commands

~~~
$ wc -l *.pdb | sort -n | head -n 1
~~~

:::{image} ../fig/csc586//09-scripting-linux/pipe-multiple.png
:alt: Multiple commands connection via pipes
:class: bg-primary mb-1
:height: 100px
:align: center
:::


::::{admonition} Challenge: piping commands together
:class: note
- In our current directory, we want to find the 3 files which have the least 
number of lines. Which command listed below would work?

1. `wc -l * > sort -n > head -n 3`
2. `wc -l * | sort -n | head -n 1-3`
3. `wc -l * | head -n 3 | sort -n`
4. `wc -l * | sort -n | head -n 3`

:::{dropdown} Solution
- Option 4 is the solution. The pipe character `|` is used to connect the output 
from one command to the input of another. `>` is used to redirect standard output 
to a file. Try it in the `shell-lesson-data/exercise-data/proteins` directory!
:::
::::

::::{admonition} Challenge: pipe reading comprehension
:class: note
- A file called animals.csv (in the `shell-lesson-data/exercise-data/animal-counts` folder) 
contains the following data: 

~~~
$ cat ~/shell-lesson-data/exercise-data/animal-counts/animals.csv
2012-11-05,deer,5
2012-11-05,rabbit,22
2012-11-05,raccoon,7
2012-11-06,rabbit,19
2012-11-06,deer,2
2012-11-06,fox,4
2012-11-07,rabbit,16
2012-11-07,bear,1
~~~

- What text passes through each of the pipes and the final redirect in the 
pipeline below? Note, the `sort -r` command sorts in reverse order.

~~~
$ cat animals.csv | head -n 5 | tail -n 3 | sort -r > final.txt
~~~

:::{dropdown} Solution
~~~
2012-11-06,rabbit,19
2012-11-06,deer,2
2012-11-05,raccoon,7
~~~
:::
::::


::::{admonition} Challenge: pipe construction

- For the file `animals.csv` from the previous exercise, consider the following command:

~~~
$ man cut
$ cut -d , -f 2 animals.csv
~~~

:::{image} ../fig/csc586//09-scripting-linux/cut-pipe.png
:alt: Piping the cut command
:class: bg-primary mb-1
:height: 100px
:align: center
:::

- The `uniq` command filters out adjacent matching lines in a file. How could you 
extend this pipeline (using uniq and another command) to find out what animals the 
file contains (without any duplicates in their names)?


:::{dropdown} Solution
~~~
$ cut -d , -f 2 animals.csv | sort | uniq
~~~
:::
::::


::::{admonition} Challenge: which pipe?

- The file `animals.csv` contains 8 lines of data formatted as follows::

~~~
2012-11-05,deer,5
2012-11-05,rabbit,22
2012-11-05,raccoon,7
2012-11-06,rabbit,19
...
~~~


The `uniq` command has a `-c` option which gives a count of the number of 
times a line occurs in its input. Assuming your current directory is 
`shell-lesson-data/exercise-data/animal-counts`, what command would you 
use to produce a table that shows the total count of each type of animal in the file?

1. `sort animals.csv | uniq -c`
2. `sort -t, -k2,2 animals.csv | uniq -c`
3. `cut -d, -f 2 animals.csv | uniq -c`
4. `cut -d, -f 2 animals.csv | sort | uniq -c`
5. `cut -d, -f 2 animals.csv | sort | uniq -c | wc -l`


:::{dropdown} Solution
Option 4. is the correct answer.
:::
::::

```

```{dropdown} 5. Nelle’s Pipeline: Checking Files

- Nelle has run her samples through the assay machines and created 17 files 
in the `north-pacific-gyre` directory described earlier. Let's check the 
integrity of this data:

~~~
$ cd ~/shell-lesson-data/north-pacific-gyre
$ ls -l 
~~~

- How do we check for data integrity? Imagine if you have thousands of files?

~~~
$ wc -l *.txt | sort -n | head -n 5
~~~

- This is possible by looking at metadata (line counts, word counts, etc)
- There are also files containing `Z` in their names, 

~~~
$ ls *Z.txt
~~~

- It is important to be careful when using wildcards if we don't want to 
include these strange files in our calculations. 

```

```{dropdown} 6. Loop

Suppose we have several hundred genome data files named `basilisk.dat`, `minotaur.dat`, and
`unicorn.dat`. For this example, we'll use the `exercise-data/creatures` directory which only 
has three example files, but the principles can be applied to many many more files at once.

The structure of these files is the same: 

- The common name, classification, and updated date are
presented on the first three lines
- The DNA sequences on the following lines.

Let's look at the files:


~~~
$ cd ~/shell-lesson-data/exercise-data/creatures/
$ head -n 5 basilisk.dat minotaur.dat unicorn.dat
~~~

:::{image} ../fig/csc586//09-scripting-linux/loop-creatures.png
:alt: Viewing DNA contents of mystical creatures
:class: bg-primary mb-1
:height: 300px
:align: center
:::


- We would like to print out the classification for each species, which is given on 
the second line of each file.
- For each file, we would need to execute the command `head -n 2` and pipe this to `tail -n 1`.
- We’ll use a loop to solve this problem, but first let’s look at the general form of a loop:

~~~
for thing in list_of_things
do
    operation_using $thing    # Indentation within the loop is not required, but aids legibility
done
~~~

and we can apply this to our example like this:

~~~
$ for filename in basilisk.dat minotaur.dat unicorn.dat
> do
>   head -n 2 $filename | tail -n 1
> done
~~~

:::{image} ../fig/csc586//09-scripting-linux/loop-classifications.png
:alt: Looping through the dat files to view creature classifications
:class: bg-primary mb-1
:height: 100px
:align: center
:::

::::{admonition} Follow the prompt
:class: note

The shell prompt changes from `$` to `>` and back again as we were
typing in our loop. The second prompt, `>`, is different to remind
us that we haven't finished typing a complete command yet. A semicolon, `;`,
can be used to separate two commands written on a single line.

::::


- When the shell sees the keyword `for`, it knows to repeat a command (or group of commands) once 
for each item in a list.
- Inside the loop, we call for the variable's value by putting `$` in front of it. The `$` tells 
the shell interpreter to treat the variable as a variable name and substitute its value in its place,
rather than treat it as text or an external command.
- In this example, the list is three filenames: `basilisk.dat`, `minotaur.dat`, and `unicorn.dat`.
Each time the loop iterates, it will assign a file name to the variable `filename` and run 
the `head` command.
  - The first time through the loop, `$filename` is `basilisk.dat`. The interpreter runs the 
  command `head` on `basilisk.dat` and pipes the first two lines to the `tail` command, 
  which then prints the second line of `basilisk.dat`.
  - For the second iteration, `$filename` becomes `minotaur.dat`. This time, the shell runs 
  `head` on `minotaur.dat` and pipes the first two lines to the `tail` command, which then 
  prints the second line of `minotaur.dat`. 
  - For the third iteration, `$filename` becomes `unicorn.dat`, so the shell runs the `head` 
  command on that file, and `tail` on the output of that.
  - Since the list was only three items, the shell exits the `for` loop.

```

```{dropdown} 7. Challenges: loop


::::{admonition} Same symbols, different meanings
:class: note

- Here we see `>` being used as a shell prompt, whereas `>` is also 
used to redirect output.
- Similarly, `$` is used as a shell prompt, but, as we saw earlier, 
it is also used to ask the shell to get the value of a variable.
- If the *shell* prints `>` or `$` then it expects you to type something, 
and the symbol is a prompt.
- If *you* type `>` or `$` yourself, it is an instruction from you that 
the shell should redirect output or get the value of a variable.
- When using variables it is also possible to put the names into curly 
braces to clearly delimit the variable name: 
  - `$filename` is equivalent to `${filename}`, but is different from
  `${file}name`. You may find this notation in other people's programs.

::::

::::{admonition} Challenge: write your own loop
:class: note
- How would you write a loop that echoes all 10 numbers from 0 to 9?

:::{dropdown} Solution
~~~
$ for loop_variable in 0 1 2 3 4 5 6 7 8 9
> do
>   echo $loop_variable
> done
~~~
:::
::::

::::{admonition} Challenge: variables in loops
:class: note

- This exercise refers to the `shell-lesson-data/exercise-data/proteins` directory.
- Run the following commands, observe the outputs, and answer the questions:

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins/
$ ls *.pdb
~~~

- What is the output of the following code?

~~~
$ for datafile in *.pdb
> do
>   ls *.pdb
> done
~~~

- Now, what is the output of the following code?

~~~
$ for datafile in *.pdb
> do
>   ls $datafile
> done
~~~

- Why do these two loops give different outputs?

:::{dropdown} Solution
- The first code block gives the same output on each iteration through 
the loop.
  - Bash expands the wildcard `*.pdb` within the loop body (as well as 
  before the loop starts) to match all files ending in `.pdb` and then 
  lists them using `ls`.
- The second code block lists a different file on each loop iteration.
The value of the `datafile` variable is evaluated using `$datafile`, 
and then listed using `ls`.
:::
::::

::::{admonition} Challenge: limiting sets of files
:class: note
- What would be the output of running the following loop in the
`shell-lesson-data/exercise-data/proteins` directory?

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins/
$ for filename in c*
> do
>   ls $filename
> done
~~~

1.  No files are listed.
2.  All files are listed.
3.  Only `cubane.pdb`, `octane.pdb` and `pentane.pdb` are listed.
4.  Only `cubane.pdb` is listed.

- How would the output differ from using this command instead?

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins/
$ for filename in *c*
> do
>   ls $filename
> done
~~~

5.  The same files would be listed.
6.  All the files are listed this time.
7.  No files are listed this time.
8.  The files `cubane.pdb` and `octane.pdb` will be listed.
9.  Only the file `octane.pdb` will be listed.


:::{dropdown} Solution
- 4 is the correct answer. `*` matches zero or more characters, so any file name 
starting with the letter c, followed by zero or more other characters will be matched.
- 8 is the correct answer. `*` matches zero or more characters, so a file name with zero or more
characters before a letter c and zero or more characters after the letter c will be matched.
:::
::::


::::{admonition} Challenge: saving to a file in a Loop
:class: note
- In the `shell-lesson-data/exercise-data/proteins` directory, what is the 
effect of this loop?

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins/
$ for alkanes in *.pdb
> do
>   echo $alkanes
>   cat $alkanes > alkanes.pdb
> done
~~~

1.  Prints `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb` and 
`propane.pdb`, and the text from `propane.pdb` will be saved to a file called `alkanes.pdb`.
2.  Prints `cubane.pdb`, `ethane.pdb`, and `methane.pdb`, and the text from all three files 
would be concatenated and saved to a file called `alkanes.pdb`.
3.  Prints `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, and `pentane.pdb`, 
and the text from `propane.pdb` will be saved to a file called `alkanes.pdb`.
4.  None of the above.

- Also in the `shell-lesson-data/exercise-data/proteins` directory,
what would be the output of the following loop?

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins/
$ for datafile in *.pdb
> do
>   cat $datafile >> all.pdb
> done
~~~

5. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, and 
`pentane.pdb` would be concatenated and saved to a file called `all.pdb`.
6. The text from `ethane.pdb` will be saved to a file called `all.pdb`. 
7. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb` 
and `propane.pdb` would be concatenated and saved to a file called `all.pdb`. 
8. All of the text from `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb` 
and `propane.pdb` would be printed to the screen and saved to a file called `all.pdb`.


:::{dropdown} Solution
- 1. The text from each file in turn gets written to the `alkanes.pdb` file. 
However, the file gets overwritten on each loop iteration, so the final content of 
`alkanes.pdb` is the text from the `propane.pdb` file.
- 7 is the correct answer. `>>` appends to a file, rather than overwriting it with the 
redirected output from a command. Given the output from the `cat` command has been 
redirected, nothing is printed to the screen.
:::
::::

```

```{dropdown} 8. More complicated loop

- Run the following loop
  - The shell starts by expanding `*.dat` to create the list of files it will process.
  - The **loop body** then executes two commands for each of those files.
    - The first command, `echo`, prints its command-line arguments to standard output.
    In this case, since the shell expands `$filename` to be the name of a file, 
    `echo $filename` prints the name of the file.
    - Finally, the `head` and `tail` combination selects lines 81-100 
    from whatever file is being processed (assuming the file has at least 100 lines).

~~~
$ cd ~/shell-lesson-data/exercise-data/creatures
$ for filename in *.dat
> do
>   echo $filename
>   head -n 100 $filename | tail -n 20
> done
~~~

- We would like to modify each of the files in `shell-lesson-data/exercise-data/creatures`,
but also save a version of the original files, naming the copies `original-basilisk.dat` 
and `original-unicorn.dat`.
- We can't use:

~~~
$ cp *.dat original-*.dat
~~~
{: .language-bash}

because that would expand to:

~~~
$ cp basilisk.dat minotaur.dat unicorn.dat original-*.dat
~~~
{: .language-bash}

This wouldn't back up our files, instead we get an error:

~~~
cp: target `original-*.dat' is not a directory
~~~
{: .error}

- This problem arises when `cp` receives more than two inputs. When this happens, it
expects the last input to be a directory where it can copy all the files it was passed.
Since there is no directory named `original-*.dat` in the `creatures` directory we get an
error.
- Instead, we can use a loop:

~~~
$ for filename in *.dat
> do
>   cp $filename original-$filename
> done
~~~
{: .language-bash}

- Since the `cp` command does not normally produce any output, it's hard to check
that the loop is doing the correct thing. However, we learned earlier how to print strings 
using `echo`, and we can modify the loop to use `echo` to print our commands without 
actually executing them. As such we can check what commands *would be* run in the unmodified loop.

The following diagram
shows what happens when the modified loop is executed, and demonstrates how the
judicious use of `echo` is a good debugging technique.

```

```{dropdown} 9. Nelle's Pipeline: Processing Files

Nelle is now ready to process her data files using `goostats.sh` ---
a shell script written by her supervisor.
This calculates some statistics from a protein sample file, and takes two arguments:

1. an input file (containing the raw data)
2. an output file (to store the calculated statistics)

Since she's still learning how to use the shell,
she decides to build up the required commands in stages.
Her first step is to make sure that she can select the right input files --- remember,
these are ones whose names end in 'A' or 'B', rather than 'Z'.
Starting from her home directory, Nelle types:

~~~
$ cd ~/shell-lesson-data/north-pacific-gyre
$ for datafile in NENE*A.txt NENE*B.txt
> do
>     echo $datafile
> done
~~~

Her next step is to decide
what to call the files that the `goostats.sh` analysis program will create.
Prefixing each input file's name with 'stats' seems simple,
so she modifies her loop to do that:

~~~
$ for datafile in NENE*A.txt NENE*B.txt
> do
>     echo $datafile stats-$datafile
> done
~~~

She hasn't actually run `goostats.sh` yet,
but now she's sure she can select the right files and generate the right output filenames.

Typing in commands over and over again is becoming tedious,
though, and Nelle is worried about making mistakes, so instead of re-entering her loop,
she presses <kbd>↑</kbd>. In response, the shell redisplays the whole loop on one line
(using semi-colons to separate the pieces):

~~~
$ for datafile in NENE*A.txt NENE*B.txt; do echo $datafile stats-$datafile; done
~~~

Using the left arrow key,
Nelle backs up and changes the command `echo` to `bash goostats.sh`:

~~~
$ for datafile in NENE*A.txt NENE*B.txt; do bash goostats.sh $datafile stats-$datafile; done
~~~

When she presses <kbd>Enter</kbd>, the shell runs the modified command.
However, nothing appears to happen --- there is no output. After a moment, Nelle realizes 
that since her script doesn't print anything to the screen any longer, she has no idea whether 
it is running, much less how quickly. She kills the running command by typing 
<kbd>Ctrl</kbd>+<kbd>C</kbd>, uses <kbd>↑</kbd> to repeat the command,
and edits it to read:

~~~
$ for datafile in NENE*A.txt NENE*B.txt; do echo $datafile;
bash goostats.sh $datafile stats-$datafile; done
~~~

::::{admonition} Beginning and End
:class: note

- We can move to the beginning of a line in the shell by typing 
<kbd>Ctrl</kbd>+<kbd>A</kbd> and to the end using <kbd>Ctrl</kbd>+<kbd>E</kbd>.

::::


When she runs her program now, it produces one line of output every five seconds or so
1518 times 5 seconds, divided by 60, tells her that her script will take about two hours to run.
As a final check, she opens another terminal window, goes into `north-pacific-gyre`,
and uses `cat stats-NENE01729B.txt` to examine one of the output files.
It looks good, so she decides to get some coffee and catch up on her reading.

::::{admonition} Those Who Know History Can Choose to Repeat It
:class: note

Another way to repeat previous work is to use the `history` command to 
get a list of the last few hundred commands that have been executed, and 
then to use `!123` (where '123' is replaced by the command number) to 
repeat one of those commands. For example, if Nelle types this:

~~~
$ history | tail -n 5
   456  ls -l NENE0*.txt
   457  rm stats-NENE01729B.txt.txt
   458  bash goostats.sh NENE01729B.txt stats-NENE01729B.txt
   459  ls -l NENE0*.txt
   460  history
~~~

then she can re-run `goostats.sh` on `NENE01729B.txt` simply by typing
`!458`.

::::

::::{admonition} Challenge: doing a dry run
:class: note
- A loop is a way to do many things at once --- or to make many mistakes at
once if it does the wrong thing. One way to check what a loop *would* do
is to `echo` the commands it would run instead of actually running them.
- Suppose we want to preview the commands the following loop will execute
without actually running those commands:

~~~
$ for datafile in *.pdb
> do
>   cat $datafile >> all.pdb
> done
~~~

- What is the difference between the two loops below, and which one would we
want to run?

~~~
# Version 1
$ for datafile in *.pdb
> do
>   echo cat $datafile >> all.pdb
> done
~~~

~~~
# Version 2
$ for datafile in *.pdb
> do
>   echo "cat $datafile >> all.pdb"
> done
~~~

:::{dropdown} Solution
- The second version is the one we want to run.
This prints to screen everything enclosed in the quote marks, expanding the 
loop variable name because we have prefixed it with a dollar sign. 
It also *does not* modify nor create the file `all.pdb`, as the `>>` 
is treated literally as part of a string rather than as a 
redirection instruction.
- The first version appends the output from the command `echo cat $datafile` 
to the file, `all.pdb`. This file will just contain the list; 
`cat cubane.pdb`, `cat ethane.pdb`, `cat methane.pdb` etc. 
- Try both versions for yourself to see the output! Be sure to change to the 
proper directory and open `all.pdb` file to view its contents.
:::
::::


::::{admonition} Challenge: nested loops
:class: note

- Suppose we want to set up a directory structure to organize 
some experiments measuring reaction rate constants with different compounds 
*and* different temperatures.  What would be the result of the following code:

~~~
$ for species in cubane ethane methane
> do
>    for temperature in 25 30 37 40
>    do
>       mkdir $species-$temperature
>     done
> done
~~~

:::{dropdown} Solution
- We have a nested loop, i.e. contained within another loop, so for each species
in the outer loop, the inner loop (the nested loop) iterates over the list of
temperatures, and creates a new directory for each combination.
- Try running the code for yourself to see which directories are created!
:::
:::: 

```

```{dropdown} 10. Shell scripting

- Let's start by going back to `~/shell-lesson-data/exercise-data/proteins$` and creating a new file, 
`middle.sh` which will become our shell script:

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins
$ nano middle.sh
$ cat middle.sh
~~~

- Add the following line to `middle.sh` and save:
  - `head -n 15 octane.pdb | tail -n 5`
- Once we have saved the file, we can ask the shell to execute the commands it contains.
Our shell is called `bash`, so we run the following command:

~~~
$ bash middle.sh
~~~

:::{image} ../fig/csc586//09-scripting-linux/script-middle.png
:alt: First simple script
:class: bg-primary mb-1
:height: 200px
:align: center
:::


::::{admonition} Text vs. Whatever
:class: note

We usually call programs like Microsoft Word or LibreOffice Writer *text 
editors*, but we need to be a bit more careful when it comes to 
programming. By default, Microsoft Word uses `.docx` files to store not 
only text, but also formatting information about fonts, headings, and so 
on. This extra information isn't stored as characters and doesn't mean 
anything to tools like `head`: they expect input files to contain 
nothing but the letters, digits, and punctuation on a standard computer 
keyboard. When editing programs, therefore, you must either use a plain 
text editor, or be careful to save files as plain text.
::::

- What if we want to select lines from an arbitrary file? We could edit 
`middle.sh` each time to change the filename, but that would probably 
take longer than typing the command out again in the shell and 
executing it with a new file name. Instead, let's edit `middle.sh` 
and make it more versatile:
  - Edit `middle.sh` and replace the text `octane.pdb` with the special variable called `$1`. 
    - Wrap `$1` inside double quotes: `"$1"`. 
  - `$1` means 'the first filename (or other argument) on the command line'.

~~~
$ nano middle.sh
$ cat middle.sh
$ bash middle.sh octane.pdb
$ bash middle.sh pentane.pdb
~~~
{: .language-bash}

:::{image} ../fig/csc586//09-scripting-linux/script-arguments.png
:alt: script with command line arguments
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Currently, we need to edit `middle.sh` each time we want to adjust the range of
lines that is returned. Let's fix that by configuring our script to instead use three 
command-line arguments.
- After the first command-line argument (`$1`), each additional argument that we
provide will be accessible via the special variables `$1`, `$2`, `$3`,
which refer to the first, second, third command-line arguments, respectively.
- Edit `middle.sh` and replace `15` with `"$2"` and `5` with `"$3"`

~~~
$ nano middle.sh
$ cat middle.sh
$ bash middle.sh pentane.pdb 15 5
~~~

- By changing the arguments to our command we can change our script's
behaviour:

~~~
$ bash middle.sh pentane.pdb 20 5
~~~
{: .language-bash}

- This works, but it may take the next person who reads `middle.sh` a moment to 
figure out what it does. We can improve our script by adding some **comments** at the top:
  - A comment starts with a `#` character and runs to the end of the line.
  - Add the following comments to `middle.sh` at the top:
    - `# Select lines from the middle of a file.`
    - `#Usage: bash middle.sh filename end_line num_lines`
- What if we want to process many files in a single pipeline?
For example, if we want to sort our `.pdb` files by length, we would type
the following command because `wc -l` lists the number of lines in the files 
and `sort -n` sorts things numerically.

~~~
$ wc -l *.pdb | sort -n
~~~

- We could put this in a file, but then it would only ever sort a list of `.pdb` files 
in the current directory. If we want to be able to get a sorted list of other kinds of files,
we need a way to get all those names into the script.
- We can't use `$1`, `$2`, and so on because we don't know how many files there are.
- Instead, we use the special variable `$@`, which means, 
'All of the command-line arguments to the shell script'.
- We also should put `$@` inside double-quotes to handle the case of arguments 
containing spaces (`"$@"` is special syntax and is equivalent to `"$1"` `"$2"` ...).
- Create a file called `sorted.sh` inside `shell-lesson-data/exercise-data/proteins` with 
the following contents:


~~~
# Sort files by their length.
# Usage: bash sorted.sh one_or_more_filenames
wc -l "$@" | sort -n
~~~

- Observe the following commands:

~~~
$ cd ~/shell-lesson-data/exercise-data/proteins
$ nano sorted.sh
$ cat sorted.sh
$ bash sorted.sh *.pdb ../creatures/*.dat
~~~
{: .language-bash}

- To turn your script into an `executable file` (run without `bash` command), the 
following line must be at the top of your script:
~~~
#!/bin/bash
~~~

- and your script file must have executable permission:

~~~
$ chmod 755 sorted.sh
$ ./sorted.sh
~~~

::::{admonition} Challenge: list unique species
:class: note

- Leah has several hundred data files, each of which is formatted like this:

~~~
2013-11-05,deer,5
2013-11-05,rabbit,22
2013-11-05,raccoon,7
2013-11-06,rabbit,19
2013-11-06,deer,2
2013-11-06,fox,1
2013-11-07,rabbit,18
2013-11-07,bear,1
~~~

- An example of this type of file is given in 
`shell-lesson-data/exercise-data/animal-counts/animals.csv`.
- We can use the command `cut -d , -f 2 animals.txt | sort | uniq` to produce 
the unique species in `animals.txt`.
- In order to avoid having to type out this series of commands every time, 
a scientist may choose to write a shell script instead.
- Write a shell script called `species.sh` that takes any number of 
filenames as command-line arguments, and uses a variation of the above command 
to print a list of the unique species appearing in each of those files separately.

:::{dropdown} Solution
~~~
#!/bin/bash
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
::::

- Suppose we have just run a series of commands that did something useful --- for example,
that created a graph we'd like to use in a paper. We'd like to be able to re-create the 
graph later if we need to, so we want to save the commands in a file. 
- Instead of typing them in again (and potentially getting them wrong) we can do this:

~~~
$ history | tail -n 5 > redo-figure-3.sh
~~~

The file `redo-figure-3.sh` now *could* contains:

~~~
297 bash goostats.sh NENE01729B.txt stats-NENE01729B.txt
298 bash goodiff.sh stats-NENE01729B.txt /data/validated/01729.txt > 01729-differences.txt
299 cut -d ',' -f 2-3 01729-differences.txt > 01729-time-series.txt
300 ygraph --format scatter --color bw --borders none 01729-time-series.txt figure-3.png
301 history | tail -n 5 > redo-figure-3.sh
~~~

- After a moment's work in an editor to remove the serial numbers on the commands,
and to remove the final line where we called the `history` command, 
we have a completely accurate record of how we created that figure.
- In practice, most people develop shell scripts by running commands at the shell prompt a few 
times to make sure they're doing the right thing, then saving them in a file for re-use.
- This style of work allows people to recycle what they discover about their data and their 
workflow with one call to `history` and a bit of editing to clean up the output
and save it as a shell script.

```


```{dropdown} 11. Nelle's Pipeline: Creating a Script

- Nelle's supervisor insisted that all her analytics must be reproducible.
The easiest way to capture all the steps is in a script.

- First we return to Nelle's project directory:

~~~
$ cd ../../north-pacific-gyre/
~~~

- then creates a file using `nano` ...

~~~
$ nano do-stats.sh
~~~

- ...which contains the following:

~~~
#!/bin/bash
# Calculate stats for data files.
for datafile in "$@"
do
    echo $datafile
    bash goostats.sh $datafile stats-$datafile
done
~~~

- ... saves this in a file called `do-stats.sh` and set executable mode so that
she can now re-do the first stage of her analysis by typing:

~~~
$ ./do-stats.sh NENE*A.txt NENE*B.txt
~~~

- She can also do the following so that the output is just the number of files processed
rather than the names of the files that were processed.

~~~
$ ./do-stats.sh NENE*A.txt NENE*B.txt | wc -l
~~~

- One thing to note about Nelle's script is that it lets the person running it decide what 
files to process. She could have written it as:

~~~
#!/bin/bash
# Calculate stats for Site A and Site B data files.
for datafile in NENE*A.txt NENE*B.txt
do
    echo $datafile
    bash goostats.sh $datafile stats-$datafile
done
~~~

- The advantage is that this always selects the right files: 
  - she doesn't have to remember to exclude the 'Z' files.
- The disadvantage is that it *always* selects just those files --- she can't run it on all files
(including the 'Z' files), or on the 'G' or 'H' files her colleagues in Antarctica are producing, 
without editing the script.
- She could modify her script to check for command-line arguments, and use `NENE*A.txt NENE*B.txt` 
if none were provided. Of course, this introduces another tradeoff between flexibility and complexity.

::::{admonition} Challenge: variables in shell scripts
:class: note

- In the `proteins` directory, imagine you have a shell script called `script.sh` 
containing the following commands:

~~~
#!/bin/bash
head -n $2 $1
tail -n $3 $1
~~~

While you are in the `proteins` directory, you type the following command:

~~~
$ ./script.sh '*.pdb' 1 1
~~~

Which of the following outputs would you expect to see?

1. All of the lines between the first and the last lines of each file ending in `.pdb`
   in the `proteins` directory
2. The first and the last line of each file ending in `.pdb` in the `proteins` directory
3. The first and the last line of each file in the `proteins` directory
4. An error because of the quotes around `*.pdb`

:::{dropdown} Solution
- The correct answer is 2.
- The special variables $1, $2 and $3 represent the command line arguments given to the 
script, such that the commands run are: 

~~~
$ head -n 1 cubane.pdb ethane.pdb octane.pdb pentane.pdb propane.pdb
$ tail -n 1 cubane.pdb ethane.pdb octane.pdb pentane.pdb propane.pdb
~~~

- The shell does not expand `'*.pdb'` because it is enclosed by quote marks.
- As such, the first argument to the script is `'*.pdb'` which gets expanded within the
script by `head` and `tail`.
:::
::::


::::{admonition} Challenge: find the longest file with a given extension
:class: note

- Write a shell script called `longest.sh` that takes the name of a 
directory and a filename extension as its arguments, and prints 
out the name of the file with the most lines in that directory 
with that extension. For example: 

~~~
$ ./longest.sh shell-lesson-data/data/pdb pdb
~~~

would print the name of the `.pdb` file in `shell-lesson-data/data/pdb` that has
the most lines.

Feel free to test your script on another directory e.g.
~~~
$ bash longest.sh shell-lesson-data/writing/data txt
~~~


:::{dropdown} Solution
~~~
#!/bin/bash
# Shell script which takes two arguments:
#    1. a directory name
#    2. a file extension
# and prints the name of the file in that directory
# with the most lines which matches the file extension.
wc -l $1/*.$2 | sort -n | tail -n 2 | head -n 1
~~~
- The first part of the pipeline, `wc -l $1/*.$2 | sort -n`, counts 
the lines in each file and sorts them numerically (largest last). When 
there's more than one file, `wc` also outputs a final summary line, 
giving the total number of lines across _all_ files.  We use 
`tail -n 2 | head -n 1` to throw away this last line. 
- With `wc -l $1/*.$2 | sort -n | tail -n 1` we'll see the final summary 
line: we can build our pipeline up in pieces to be sure we understand the output.
:::
::::


::::{admonition} Challenge: script reading comprehension
:class: note

- For this question, consider the `shell-lesson-data/exercise-data/proteins` 
directory once again. This contains a number of `.pdb` files in addition to any other 
files you may have created.
- Explain what each of the following three scripts would do when run as 
`bash script1.sh *.pdb`, `bash script2.sh *.pdb`, and `bash script3.sh *.pdb` respectively.

~~~
# Script 1
echo *.*
~~~

~~~
# Script 2
for filename in $1 $2 $3
do
  cat $filename
done
~~~

~~~
# Script 3
echo $@.pdb
~~~

:::{dropdown} Solution
In each case, the shell expands the wildcard in `*.pdb` before passing the resulting 
list of file names as arguments to the script. 
- Script 1 would print out a list of all files containing a dot in their name. 
The arguments passed to the script are not actually used anywhere in the script. 
- Script 2 would print the contents of the first 3 files with a `.pdb` file extension.
`$1`, `$2`, and `$3` refer to the first, second, and third argument respectively. 
- Script 3 would print all the arguments to the script (i.e. all the `.pdb` files), 
followed by `.pdb`. `$@` refers to *all* the arguments given to a shell script.

~~~
 cubane.pdb ethane.pdb methane.pdb octane.pdb pentane.pdb propane.pdb.pdb
~~~
:::
::::


::::{admonition} Challenge: debugging scripts
:class: note

- Suppose you have saved the following script in a file called 
`do-errors.sh` in Nelle's `north-pacific-gyre/scripts` directory:

~~~
# Calculate stats for data files.
for datafile in "$@"
do
  echo $datfile
  bash goostats.sh $datafile stats-$datafile
done
~~~

- When you run it from the `north-pacific-gyre` directory, the output
is blank. 

~~~
$ bash do-errors.sh NENE*A.txt NENE*B.txt
~~~

- To figure out why, re-run the script using the `-x` option:

~~~
$ bash -x do-errors.sh NENE*A.txt NENE*B.txt
~~~

- What is the output showing you?
- Which line is responsible for the error?

:::{dropdown} Solution
- The `-x` option causes `bash` to run in debug mode.
- This prints out each command as it is run, which will help you to locate errors. 
- In this example, we can see that `echo` isn't printing anything. We have made a typo
in the loop variable name, and the variable `datfile` doesn't exist, hence returning 
an empty string.
:::
::::

```