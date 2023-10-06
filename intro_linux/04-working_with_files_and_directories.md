# Working With Files and Directories

## Names for Files and Directories

Complicated names of files and directories can make your life very painful
when working on the command line. Here we provide a few useful
tips for the names of your files from now on.

1. Don't use whitespaces.

    White spaces can make a name more meaningful
    but since whitespace is used to break arguments on the command line
    is better to avoid them on name of files and directories.
    You can use `-` or `_` instead of whitespace.


    Commands treat names starting with `-` as options.

 2. Stay with letters, numbers, `.` (period), `-` (dash) and `_` (underscore).

 3. Don't begin the name with `-`.
   

 If you need to refer to names of files or directories that have whitespace
 or another non-alphanumeric character you should put quotes around the name.

## Copying, Moving, and Deleting

### Copying
Copy a file with `cp`:
```
$ cp oldfile newfile
```
To copy a file into a directory:
```
$ cp filename /path/to/directory
```
This will make a copy of *filename* with same name in *directory*.

### Moving
Move a file with `mv`:
```
$ mv oldfile newfile
```
The move command is also the command to rename a file.
```
$ mv filename directory
```
The above command will move *filename* into the existing *directory*.

```{note}
`cp` and `mv` can overwrite files which is irreversible. Using the `-i` flag with `cp` or `mv` will prompt you before overwriting an existing file.
```

### Deleting
Remove a file with `rm`:
```
$ rm filename
```
The opposite of `mkdir` is `rmdir`:
```
$ rmdir directory
```
`rmdir` only works for empty directories. To delete a directory and all it's contents pass the `-r` or `--recursive` flag to `rm`:
```
$ rm -r directory
```

### Deleting Is Forever

Files deleted with `rm` cannot be recovered from a trash bin. Be very careful when deleting files especially with `rm -r`.

## Wildcards

File globbing, known better as wildcards, uses patterns to automatically expand a file name or path. The `*` character matches any (multiple) characters. A `?` matches a single character.

**Example:**

```
$ ls
example1.txt    hello1.txt    hello2.txt    hello3.txt
```

```
$ ls *.txt
example1.txt    hello1.txt    hello2.txt    hello3.txt  hello4.csv
```

```
$ ls hello*
hello1.txt    hello2.txt    hello3.txt  hello4.csv
```

```
$ ls hello?.txt
hello1.txt    hello2.txt    hello3.txt
```
## Viewing Contents of a File

There are many different ways to view the contents of a file.

- `more` and `less` will display the file in a *buffer* 
    - contents will fill the size of your terminal, allowing you to scroll
```
$ less file
```

- `cat` will print the contents of the file to the terminal
    - not recommended with large text files, use `more` or `less` instead
```
$ cat file
```

- `head` will display the first 10 lines of the file
- `head -n X` will display the first X lines of the file
```
$ head file

$ head -n 20 file
```
- `tail` will display the last 10 lines of the file
- `tail -n X` will display the last X lines of the file
```
$ tail file

$ tail -n 20 file
```

- `tail -f` will display the last 10 lines and continue displaying lines as the file is updated
```
$ tail -f logfile
```




```{admonition} 9. Creating directories: mkdir
:class: dropdown

- Create a directory called `thesis`, and check for its existence.
  - Also check that there is nothing inside
  the newly created directory. 

~~~
$ mkdir thesis
$ ls -F
~~~


::::{admonition} Challenge: `mkdir` creating multiple directories
:class: note

- What is the role of the `-p` flag in the following 
commands:

~~~
$ mkdir ../project/data 
$ ls -F ../project
$ mkdir -p ../project/data
$ mkdir -p ../project/report ../project/results
$ ls -F ../project
~~~

:::{admonition} Solution
`-p` allows the creation of all directories
on the specified path, regardless whether any directory on 
that path exists. 
:::
::::

- **Important for directory and file names in Linux!!!**
  - Do not use spaces/special characters in file and directory names. 
  - Use `-`, `_`, and `.` for annotation, but do not begin
  the names with them. 

```


```{admonition} 10. Creating files: nano (or vim)
:class: dropdown

- Linux terminal environment is text-only, hence its editors are 
text only as well. 
  - `nano`
  - `vim`
  - `emacs`. 
- Fun read: [One does not simply exist vim](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)
- We are using nano (lowest learning curve). 
- Create a file named `draft.txt` inside `thesis`. 
  - Type in the contents shown in the screenshot. 

~~~
$ pwd
$ ls
$ cd thesis
$ nano draft.txt
~~~


:::{image} ../fig/intro-linux/nano.png
:alt: Nano editor
:class: bg-primary mb-1
:height: 200px
:align: center
:::

- To save the text, you need to press `Ctrl` + `O` keys:
  - Press and hold `Ctrl` then press `O`. 
  - You will be asked whether to keep the same file name or to edit the name. 
  Press `Enter` to confirm. 
- To quit nano, press `Ctrl` + `X`. 
  - If you have not saved the text before, nano will ask 
  if you want to save the file first and confirm the name with `Y` or `N`. 

```

```{admonition} 11. Moving files and directories:  mv
:class: dropdown

- `mv` is short for move. It will move a file/directory from 
one location to another. 

~~~
$ cd ~/shell-lesson-data/exercise-data/writing
$ ls thesis
$ mv thesis/draft.txt thesis/quotes.txt
$ ls thesis
$ mv thesis/quotes.txt .
$ ls thesis
$ ls 
~~~


::::{admonition} Challenge: Moving files to a new folder
:class: note

- After running the following commands, Jamie realizes that she 
put the files `sucrose.dat` and `maltose.dat` into the wrong folder. The 
files should have been placed in the `raw` folder.

~~~
$ ls -F
analyzed/ raw/
$ ls -F analyzed
fructose.dat glucose.dat maltose.dat sucrose.dat
$ cd analyzed
~~~


- Fill in the blanks to move these files to the `raw` folder:

~~~
$ mv sucrose.data maltose.data ____/_____
~~~

:::{admonition} Solution
~~~
$ mv sucrose.data maltose.data ../raw
~~~
:::
::::
```


```{admonition} 12. Copying files and directories: cp
:class: dropdown

- `cp` stands for copy. It copies a file or directory to a new location, 
possibly with a new name.  

~~~
$ cp quotes.txt thesis/quotations.txt
$ ls quotes.txt thesis/quotations.txt
$ cp -r thesis thesis_backup
$ ls thesis thesis_backup
~~~


::::{admonition} Challenge: Renaming files
:class: note

- Suppose that you created a plain-text file in your 
current directory to contain a list of the statistical 
tests you will need to do to analyze your data, and named 
it: `statstics.txt`
- After creating and saving this file you realize you 
misspelled the filename! You want to correct the mistake, 
which of the following commands could you use to do so?

1. cp statstics.txt statistics.txt
2. mv statstics.txt statistics.txt
3. mv statstics.txt .
4. cp statstics.txt .

:::{admonition} Solution
1. No. While this would create a file with the correct name, 
the incorrectly named file still exists in the directory and 
would need to be deleted.
2. Yes, this would work to rename the file.
3. No, the period(.) indicates where to move the file, but 
does not provide a new file name; identical file names cannot be created.
4. No, the period(.) indicates where to copy the file, but does 
not provide a new file name; identical file names cannot be created.
:::
::::

::::{admonition} Challenge: Moving and copying
:class: note

- What is the output of the last `ls` command in the sequence shown below?

~~~
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
1. No, `proteins-saved.dat` is located at `/home/rammy/`
2. Yes
3. `proteins.dat` is located at `/home/rammy/data/recombined`
4. No, `proteins-saved.dat` is located at `/home/rammy/`
:::
::::


```


```{admonition} 13. Removing files and directories: rm
:class: dropdown

- Returning to the `shell-lesson-data/exercise-data/writing` directory, 
let’s tidy up this directory by removing the quotes.txt file we created. 
- The command we’ll use for this is `rm` (short for ‘remove’): 

~~~
$ cd ~/shell-lesson-data/exercise-data/writing
$ ls 
$ rm quotes.txt
$ ls quotes.txt
$ rm thesis
$ rm -r thesis
~~~


```
 

 ```{admonition} 14. Wildcards
:class: dropdown

- `*` is a wildcard, which matches zero or more characters. 
  - Inside `shell-lesson-data/exercise-data/proteins` directory: 
    - `*.pdb` matches `ethane.pdb`, `propane.pdb`, and every file that ends with ‘.pdb’. 
    - `p*.pdb` only matches `pentane.pdb` and `propane.pdb`, because the ‘p’ at the front 
    only matches filenames that begin with the letter ‘p’.
- `?` is also a wildcard, but it matches exactly one character. So 
  - `?ethane.pdb` would match `methane.pdb`
  - `*ethane.pdb` matches both `ethane.pdb`, and `methane.pdb`.
- Wildcards can be used in combination with each other
  - `???ane.pdb` matches three characters followed by `ane.pdb`.
  - `cubane.pdb`, `ethane.pdb`, `octane.pdb`.
- When the shell sees a wildcard, it expands the wildcard to create a list of 
matching filenames before running the command that was asked for. It is the shell, 
not the other programs, that deals with expanding wildcards.
- Change into `shell-lesson-data/exercise-data/proteins` and try the following 
commands

~~~
$ ls *t*ane.pdb
$ ls *t?ne.*
$ ls *t??ne.pdb
$ ls ethane.*
~~~

:::{image} ../fig/intro-linux/wildcards.png
:alt: Outcome of various wildcards
:class: bg-primary mb-1
:height: 200px
:align: center
:::

::::{admonition} Challenge: more on wildcards
:class: dropdown

Sam has a directory containing calibration data, datasets, and descriptions of
the datasets:

~~~
.
├── 2015-10-23-calibration.txt
├── 2015-10-23-dataset1.txt
├── 2015-10-23-dataset2.txt
├── 2015-10-23-dataset_overview.txt
├── 2015-10-26-calibration.txt
├── 2015-10-26-dataset1.txt
├── 2015-10-26-dataset2.txt
├── 2015-10-26-dataset_overview.txt
├── 2015-11-23-calibration.txt
├── 2015-11-23-dataset1.txt
├── 2015-11-23-dataset2.txt
├── 2015-11-23-dataset_overview.txt
├── backup
│   ├── calibration
│   └── datasets
└── send_to_bob
    ├── all_datasets_created_on_a_23rd
    └── all_november_files
~~~


Before heading off to another field trip, Sam wants to back up her data and
send datasets created the 23rd of any month to Bob. Sam uses the following commands
to get the job done:

~~~
$ cp *dataset* backup/datasets
$ cp ____calibration____ backup/calibration
$ cp 2015-____-____ send_to_bob/all_november_files/
$ cp ____ send_to_bob/all_datasets_created_on_a_23rd/
~~~


Help Sam by filling in the blanks.

The resulting directory structure should look like this
~~~
.
├── 2015-10-23-calibration.txt
├── 2015-10-23-dataset1.txt
├── 2015-10-23-dataset2.txt
├── 2015-10-23-dataset_overview.txt
├── 2015-10-26-calibration.txt
├── 2015-10-26-dataset1.txt
├── 2015-10-26-dataset2.txt
├── 2015-10-26-dataset_overview.txt
├── 2015-11-23-calibration.txt
├── 2015-11-23-dataset1.txt
├── 2015-11-23-dataset2.txt
├── 2015-11-23-dataset_overview.txt
├── backup
│   ├── calibration
│   │   ├── 2015-10-23-calibration.txt
│   │   ├── 2015-10-26-calibration.txt
│   │   └── 2015-11-23-calibration.txt
│   └── datasets
│       ├── 2015-10-23-dataset1.txt
│       ├── 2015-10-23-dataset2.txt
│       ├── 2015-10-23-dataset_overview.txt
│       ├── 2015-10-26-dataset1.txt
│       ├── 2015-10-26-dataset2.txt
│       ├── 2015-10-26-dataset_overview.txt
│       ├── 2015-11-23-dataset1.txt
│       ├── 2015-11-23-dataset2.txt
│       └── 2015-11-23-dataset_overview.txt
└── send_to_bob
    ├── all_datasets_created_on_a_23rd
    │   ├── 2015-10-23-dataset1.txt
    │   ├── 2015-10-23-dataset2.txt
    │   ├── 2015-10-23-dataset_overview.txt
    │   ├── 2015-11-23-dataset1.txt
    │   ├── 2015-11-23-dataset2.txt
    │   └── 2015-11-23-dataset_overview.txt
    └── all_november_files
        ├── 2015-11-23-calibration.txt
        ├── 2015-11-23-dataset1.txt
        ├── 2015-11-23-dataset2.txt
        └── 2015-11-23-dataset_overview.txt
~~~


:::{admonition} Solution
~~~
$ cp *calibration.txt backup/calibration
$ cp 2015-11-* send_to_bob/all_november_files/
$ cp *-23-dataset* send_to_bob/all_datasets_created_on_a_23rd/
~~~
:::
::::
```