
# Process Control


```{dropdown} 1. Components of a process

- Represents a running program
- An address space
- A set of data structures within the kernel
  - Address space map
  - Current status of the process
  - Execution priority of the process
  - Information about resources
  - Information about files and open ports
  - Signal mask
  - Owner
  - ...


:::{image} ../fig/csc586//05-process/process.png
:alt: Mapping of a process in memory
:class: bg-primary mb-1
:height: 700px
:align: center
:::

```

```{dropdown} 2. Identifiers

- PID: process ID number
- PPID: parent PID - how is a process spawn?
- UID: user identifier of the person who created the process
- EUID: effective user identifier - what resources the process has access to at any given moment
- GID: group identifier of the person who created the process
- EGID: effective group identifier
```

```{dropdown} 3. Life cycle of a process

- When system boot, the first process is created (`init` or `systemd`) with process 
ID of 1
- All other processes are created through `fork`
  - `fork()` creates a copy of the parent process. 
  - In the copy (child), `fork()` returns 0. 
  - In the original (parent), `fork()` returns the new PID of the child process. 
```

```{dropdown} 4. Signals

- Process-level interrupt requests
- Approximately thirty signals
  - Are sent as means of communication
  - Are sent by terminal driver to kill/interrupt/suspend processes using Ctrl-C or Ctrl-Z
  - Are sent by kill to terminal processes
  - Are sent by kernel when faults happen (e.g., divided by 0)
  - Are sent by kernel to notify the process of interesting events (I/O data is available, child process is dead …)

```

```{dropdown} 5. Important signals

- [Signal description](https://man7.org/linux/man-pages/man7/signal.7.html)
- HUP
- INT
- QUIT
- KILL
- BUS
- SEGV
- TERM
- STOP
- TSTP
- CONT
- WINCH
- USR1
- USR2

```

```{dropdown} 6. Monitoring processes: ps

- `ps`: [Snapshot of current processes](https://linux.die.net/man/1/ps)
- ssh to molly and run:

~~~
$ ps aux
~~~

- `USER`, `PID`, `%CPU`, `%MEM`
- `VSZ`: Virtual size of the process
- `RSS`: Resident set size (number of pages)
- `TTY`: control terminal ID
- `STAT`: current process status (Process State Codes from manual)
- `TIME`: CPU time process consumed
- `COMMAND`: command and arguments. 

```

```{dropdown} 7. Other monitoring commands:

- `top`
- `htop` 

```


```{dropdown} 8. Hands-on:

- [Spend 10-15 minutes to read and learn how to use tmux](https://tmuxcheatsheet.com/)
- This is to be done on CloudLab
- `strace`: check what a process is doing
  -  Create a tmux session with two horitonzal panel. 
  - Run `top` in the first screen
  - In the second screen
  - Identify the process ID of top
  - Run `strace` on this process ID:

~~~  
$ sudo strace -p <top_process_ID>
~~~

```


```{dropdown} 9. Runaway processes:

- System slows down!
- Use `ps` and `top` (`htop`) to identify those that soak up CPU and memory
- Check filesystem disk usage: `df -h`
- Check directory usage: `du -h`

```



```{dropdown} 10. Periodic processes:

- The `cron` daemon allows the execution of commands on a predetermined schedule. 
- Run the followings

~~~
$ crontab -e
~~~

- Select an editor (recommend nano)
- Type `* * * * * echo $(/bin/date) >> /users/<your_username>/cron.log` into the file
- Save and quit nano (we did this before)
- Wait for a few minutes, then check the content of cron.log
- Common usage:
  - Sending mail
  - Cleaning up a file system
  - Rotating a log file
  - Running batch jobs
  - Backing up and mirroring
- [A legacy!!!](https://github.com/NARKOZ/hacker-scripts)
```