
# GDB Debugger"
teaching: 0
exercises: 0
questions:
- "Debugging C program the hard way!"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"


> ## 1. In a nutshell
> 
> - Developed in 1986 by Richard Stallman at MIT.
> - Current official maintainers come from RedHat, AdaCore, and Google.
> - Significant contribution from the open source community.
```

> ## 2. Brief Technical Details
> 
> - Allows programmers to see inside and interact/modify with all components of a programs,
> including information inside the registers.
> - Allows programmers to walk through the program step by step, including down to 
> instruction level, to debug the program.
```

> ## 3. Cheatsheet
> 
> - Study this [cheatsheet](https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf)
> - Developed by Dr. Doeppner at Brown University. 
> - Become very comfortable with terminal!
> - We will work on the terminal extensively here, say goodbye to VSCode.
> *You can certainly use VSCode, but you will miss out on a fine tool!*
```

> ## 4. tmux
> 
> - Our workspace is limited within the scope of a single terminal (a single shell) 
> to interact with the operating system. 
> - `tmux`: *terminal multiplexer*. 
> - `tmux` allows user to open multiple terminals and organize split-views (panes) 
> within these terminals within a single original terminal. 
> - We can run/keep track off multiple programs within a single terminal. 
```

> ## 5. tmux quickstart 1: multiple sessions
> 
> - Start new with a session name: `tmux new -s csc331`
> - You are now in the new tmux session. 
> - List sessions: `tmux ls`
>
> <img src="../assets/figure/gdb/01.png" alt="list tmux sessions" style="height:250px">
>
> - To go back to the main terminal, press `Ctrl-b`, then press `d`. 
>
> <img src="../assets/figure/gdb/02.png" alt="detach from tmux session" style="height:250px">
>
> - To go back into the `csc331` session: `tmux attach-session -t csc331`. 
>
> <img src="../assets/figure/gdb/03.png" alt="attach to an existing tmux session" style="height:250px">
>
> - To kill a session: 
>   - From inside the session: `exit`
>   - From outside the session: `tmux kill-session -t csc331`
```

> ## 6. Hands on: navigating among multiple tmux sessions
> 
> - Run `tmux ls` to check and `tmux kill-session` to clean up all existing 
> tmux sessions. 
> - Create a new session called `s1`. 
> - Detach from `s1` and go back to the main terminal. 
> - Create a second session called `s2`. 
> - Detach from `s2`, go back to the main terminal, and create a third session called `s3`. 
> - Use `tmux ls` to view the list of tmux sessions. 
> - Navigate back and forth between the three sessions several times. 
> - Kill all three sessions using only `exit`!
> - SCREENSHOT
```

> ## 7. tmux quickstart 2: multiple panes
>
> - Create a new session called `p1`.
> - Splits terminal into vertical panels: `Ctrl-b` then `Shift-5` (technical documents
> often write this as `Ctrl-b` and `%`).
>
> <img src="../assets/figure/gdb/04.png" alt="Vertical split a tmux session" style="height:800px">
>
> - Splits terminal (the current pane) into horizontal panels: `Ctrl-b` then `Shift-'` 
> ( technical documents often write this as `Ctrl-b` and `"`).
>
> <img src="../assets/figure/gdb/05.png" alt="Horizontal split a tmux pane" style="height:800px">
>
> - Toggle between panels: `Ctrl-b` then `Space`.
> - To move from one panel to other directionally: `Ctrl-b`then the corresponding 
> arrow key. 
> - Typing `exit` will close one pane. 
```

> ## 8. Hands on: creating multiple panes
> 
> - Run `tmux ls` to check and `tmux kill-session` to clean up all existing 
> tmux sessions. 
> - Create a new session called `p1`. 
> - Organize `p1` such that: 
>   - `p1` has four vertical panes. 
>   - The last vertical pane of `p1` has three internal horizontal panes. 
> - Kill all panes using `exit`!
>
> <img src="../assets/figure/gdb/06.png" alt="Multiple vertical/horizontal splits" style="height:800px">
>
```

> ## 9. tmux quickstart 3: resizing
>
> - What we did in Hands-on 8 was not quite usable. 
> - We need to be able to adjust the panes to the proper sizes. 
> - This can be done by issuing additional commands via tmux's command line terminal.
> - Run `tmux ls` to check and `tmux kill-session` to clean up all existing 
> tmux sessions. 
> - Create a new session called `p1`.
> - Split the session horizontally.
> - Move the active cursor to the top pane. 
> - Open tmux command by typing `Ctrl-b` then `Shift-;`
> - Use the following command for resizing the current pane down:
>   - `resize-pane -D 20`: (Resizes the current pane down by 20 cells)
>
> <img src="../assets/figure/gdb/07.png" alt="Resizing pane down" style="height:800px">
>
>
> <img src="../assets/figure/gdb/08.png" alt="Resizing pane down" style="height:800px">
>
> - Move the active cursor to the bottom pane. 
> - Open tmux command by typing `Ctrl-b` then `Shift-;`
> - Use the following command for resizing the current pane down:
>   - `resize-pane -U 20`: (Resizes the current pane up by 20 cells)
>
> <img src="../assets/figure/gdb/09.png" alt="Resizing pane up" style="height:800px">
>
>
> <img src="../assets/figure/gdb/10.png" alt="Resizing pane up" style="height:800px">
>
```


> ## 10. Hands on: creating multiple panes
> 
> - Run `tmux ls` to check and `tmux kill-session` to clean up all existing 
> tmux sessions. 
> - Create a new session called `p1`. 
> - Split `p1` once vertically. 
> - Use the following commands to resize the left pane:
>   - `resize-pane -L 20` (Resizes the current pane left by 20 cells)
>   - `resize-pane -R 20` (Resizes the current pane right by 20 cells)
```


> ## 12. Setup an application with gdb
> 
> - To use `gdb` to debug, we need to compile the program with a `-g` flag.
> - Split the `gdb` session into two horizontal panes.
> - In the top pane, run the followings command:
>
> ~~~
> $ cd ~/csc331/intro-c
> $ gcc -g -o hello hello.c
> ~~~
> {: .language-bash}
>
> - In the bottom pane, run the followings command:
>
> ~~~
> $ cd ~/csc331/intro-c
> $ gdb hello
> gdb-peda$ run
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/gdb/12.png" alt="Run gdb" style="height:800px">
>
```


> ## 13. Debugging with gdb
> 
> - We need to set a `breakpoint`:
>   - Could be a line number or
>   - Could be a function name
>
> ~~~
> gdb-peda$ b main
> gdb-peda$ run
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/gdb/13.png" alt="Run gdb with breakpoint" style="height:800px">
>
```


> ## 15. Scrolling within tmux's panes
> 
> - Mouse scrolling does not work with tmux. 
> - To enable scrolling mode in tmux, type `Ctr-b` then `[`. 
> - You can use the `Up`/`Down`/`PgUp`/`PgDn` keys to navigate. 
> - To quit scrolling mode, type `q` or `Esc`. 
>
> ~~~
> gdb-peda$ b main
> gdb-peda$ run
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/gdb/14.png" alt="Scrolling mode in gdb" style="height:800px">
>
> - At a glance
>   - Registers' contents
>   - Code
>   - Stack contents
>   - Assembly codes
> - `gdb` stops at our breakpoint, just before function `main`. 
> - The last line (before the `gdb-peda$` prompt) indicates the next line of code to 
> be executed. 
```


> ## 16. Hands on: finish running hello
> 
> - Type `q` or `Esc` to quit scrolling mode. 
> - To continue executing the next line of code, type `n` then `Enter`. 
> - Turn back into the scrolling mode and scroll back up
> to observe what happens after typing `n`. 
> - What is the next line of code to be executed?
> - Type `n` three more times to observe the line of codes being executed
> and the final warning from `gdb`. 
```


> ## 17. Examining contents of program while debugging
> 
> - In the top pane, compile `malloc_1.c` in debugging mode. 
> - In the bottom pane, quit the current gdb session and 
> rerun it on the recently created `malloc_1` executable. 
> - Setup `main` as the `breakpoint` and start running. 
> ~~~
> gdb-peda$ b main
> gdb-peda$ run
> ~~~
> {: .language-bash}
>
> - Type `n` and `Enter` to run the next line of code: `void *p = malloc(4);`
> - Type `p p`: the first `p` is short for `print` and the second `p` is the 
> void pointer variable `p` in the program. 
> - Try running `p *p`. What does that feedback mean? 
> - Type `n` and `Enter` to run the next line of code: `float *fp = (float *)p;`
> - Type `p fp`: what is the printed value?
> - Type `n` and `Enter` to run the next line of code: `int *ip = (int *)p;`
> - Type `p ip`: what is the printed value?
> - Type `n` and `Enter` to run the next line of code: `*ip = 98765;`
> - Type `p ip`: what is the printed value?
> - Type `p *ip`: what is the printed value?
> - Type `p /t *ip`: what type of data is value? what is the corresponding value in 
> decimal?
> - Keep hitting `n` until you finish stepping through all the remain lines of code. 
```

> ## 18. Examining contents of program while debugging
> 
> - In the top pane, compile `array_4.c` in debugging mode. 
> - In the bottom pane, quit the current gdb session and 
> rerun it on the recently created `array_4` executable as follows: 
>
> ~~~
> $ gdb array_4
> gdb-peda$ b main
> gdb-peda$ run
> ~~~
> {: .language-bash}
>
> - The next line of code to be run is `size = atoi(argv[1]);`
> - Run the following commands and observe the outcomes: 
>   - `p argc` 
>   - `p argv[0]` 
>   - `p argv[1]` 
>   - `p argv[2]`
>   - `p argv[3]` 
>   - `p argv[4]` 
>   - ...
> - Type `n` and `Enter` to run the next line of code: `size = atoi(argv[1]);`
> - Turn into scrolling mode to observe that dreaded `Segmentation fault` notice. 
> - Scrolling down to see if `gdb` helps identify the issue?
> - Type `q` to exit `gdb`.
>
> - Rerun gdb on `array_4` executable as follows: 
>
> ~~~
> $ gdb array_4
> gdb-peda$ b main
> gdb-peda$ run 3
> ~~~
> {: .language-bash}
>
> - The next line of code to be run is `size = atoi(argv[1]);`
> - Run the following commands and observe the outcomes: 
>   - `p argc` 
>   - `p argv[0]` 
>   - `p argv[1]` 
>   - `p argv[2]`
>   - ...
> - Type `n` and `Enter` to run the next line of code: `size = atoi(argv[1]);`
> - Run the following commands and observe the outcomes: 
>   - `p size` 
>   - `p &size`
> - Type `n` and `Enter` to run the next line of code: `printf("Before malloc, p is pointing to address (%p)\n", p);`
> - Run the following commands and observe the outcomes: `p p` 
```

> ## 19. Hands on: finish running array_4
> 
> - Step through the `for` loop and printing out values of `i`, `p[i]`, `&p[i]`, 
> and `p + i` at every iteration. 
> - Make sure that you understand the lines of code that cause these variables to 
> change value.
> - Utilize scrolling as needed. 
```

{% include links.md %}

