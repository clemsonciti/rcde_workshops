# Pipes and Redirection

## Pipes
**Pipes** are used to redirect output from one command into the input of another. When a command outputs text to the screen, that is called **standard out** (stdout). A pipe will redirect the standard output of a process to the **standard in** (stdin) of another program.
```
$ ls | wc -l
```
The above example pipes the output of `ls` to the input of `wc -l`.

 `wc` stands for **w**ord **c**ount and `-l` tells `wc` to count lines instead of characters. This command will output the number of files in the directory.

## Redirect Input and Output

A program's output can be redirected to a file instead of stdout using `>`.
```
$ ls > list-of-files.txt
```

The content of a file can be sent as stdin to a program with `<`.
```
$ wc -l < list-of-files.txt
```

`>` will overwrite the contents of an existing file. Use `>>` to **append** to a file.
```
$ some-command > logfile

$ other-command >> logfile
```

![Redirects and Pipes](../fig/redirects-and-pipes.svg)