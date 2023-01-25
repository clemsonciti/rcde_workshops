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
example1.txt    hello1.txt    hello2.txt    hello3.txt  hello4.csv
```

```
$ ls *.txt
example1.txt    hello1.txt    hello2.txt    hello3.txt
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
