# Utilities and Useful Information

## Tab completion

Pressing `Tab` will attempt to autocomplete the command/filename/directory you are typing.
```
$ ls long_file
```
Then press `Tab`
```
$ ls long_file_name_you_cant_remember.txt
```

## history

Bash will retain a history of the previous commands you entered. The `history` command will (by default on Palmetto) display the last 1000 commands.

```
$ history
```

You can use the up arrow &uarr; and down arrow &darr; to scroll through previous commands.

`!!` will run the previous command.
```
$ ls
...

$ !!
ls
...
```
`!name` will run the last command that started with `name`.
```
$ qsub myjob.pbs
...

$ !qsub
qsub myjob.pbs
...
```

## Download Files from the Web

`wget` is a useful utility to download files from websites. 

```
$ wget https://github.com/lammps/lammps/archive/refs/tags/stable_23Jun2022_update2.tar.gz
```

## Compressing Files and Directories

### gzip

`gzip file` will compress a file to `file.gz`. Uncompress with `gunzip file.gz`.

### tar
`tar` can be used to create a (**t**ape) **ar**chive of files/folders.

```
$ tar czvf my_archive.tar.gz file1 [file2] [directory]
```
- `-c` create archive
- `-z` compress (with gzip)
- `-v` verbose (print files being placed in the archive)
- `-f` use archive name provided (*my_archive.tar.gz*)

```
$ tar xzvf my_archive.tar.gz
```
- `-x` extract archive
- `-z` uncompress (with gzip)
- `-v` verbose (print files being extracted)
- `-f` use archive name provided (*my_archive.tar.gz*)

## Convert a Windows file to Unix format

Copying a file from a Windows computer can cause issues since Windows editors like Notepad will end lines with CRLF line endings. Linux uses the Unix LF line endings.

The `dos2unix` command will convert the file to Unix format. You can confirm if a file is in the Windows format with `file`.
```
$ file copied_from_windows.txt
copied_from_windows.txt: ASCII text, with CRLF line terminators
```
```
$ dos2unix copied_from_windows.txt
dos2unix: converting file copied_from_windows.txt to Unix format...
```
```
$ file copied_from_windows.txt
copied_from_windows.txt: ASCII text
```
