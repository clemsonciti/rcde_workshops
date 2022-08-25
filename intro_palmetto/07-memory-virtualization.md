
# Memory virtualization"
teaching: 0
exercises: 0
questions:
- "How can an illusion of infinite and isolated memory space be managed?"
objectives:
- "Understand how a process' components are organized in memory."
- "Understand the idea of address space and memory virtualization."
keypoints:
- "Memory virtualization is how the OS provides an abstraction of physical 
memory to process in order to facilitate transparency, efficiency, and protection."


> ## 0. Midterm Exam...
> 
> - **Wednesday, March 24 , 2021**
> - 24-hour windows range: 12:00AM - 11:59PM March 24, 2021. 
> - 75 minutes duration.
> - 20 questions  (similar in format to the quizzes).
> - Everything (including source codes) up to today (Wednesday, March 3, 2021).
```


> ## 1. In the beginning ...
> 
> - Users didn't expect much. 
> - To be honest, most, if not all, users are also developers ...
```


> ## 2. Early systems
> 
> - Computers run **one job** at a time. 
> - The OS was preloaded into memory and consisted of a set of routines. 
> - There was one running program that uses the rest of memory. 
>
> <img src="../assets/figure/memory-virtualization/01.png" alt="Early systems" style="height:500px">
```


> ## 3. Multiprogramming and time sharing
> 
> - Demands for
>   - Utilization
>   - Efficiency
>   - Interactivity
> - Multiple processes ready to run at a given time. 
> - The OS switches between them. 
> - One approach is to run one process at a time and still give it full access to all memory 
> (just like the early days ...).
> - This requires switch processes from memory.
```


> ## 4. Multiprogramming and time sharing
> 
> - This solution does not scale as memory grows. 
> 
> | System event | Size    | Latency | 
> | ------------ | ------- | ------- |  
> | CPU          |         | <1ns    |  
> | L1 cache     | 32KB    | 1ns     |  
> | L2 cache     | 256KB   | 4ns     |  
> | L3 cache     | >8MB    | 40ns    |  
> | DDR RAM      | 4GB-1TB | 80ns    |  
>
```

> ## 5. Multiprogramming and time sharing
> 
> What we want to do  
>
> - Leave processes in memory and let OS implement an efficient time sharing/switching 
> mechanism. 
> - A new demand: **protection** (through isolation)
>
> <img src="../assets/figure/memory-virtualization/02.png" alt="multiprogramming" style="height:500px">
```


> ## 6. Address space
> 
> - Provide users (programmers) with an **easy-to-use** abstarction of physical memory. 
> - The running program's **view of memory in the system**. 
> - Contains all memory states of the running program:
>   - `Stack` to keep track of where it is in the function call chain 
>   (stack frames), allocate local variables, and pass parameters and 
>   return values to and from routines. 
>   - `Heap` is used for dynamically allocated, user-managed memory 
>   (i.g., malloc()). 
>   - `BSS` (block started by symbols) contains all global variables and static 
>   variables that are initialized to zero or do not have explicit initialization 
>   in source code.
>   - `Data` contains the global variables and static variables that are initialized 
>   by the programmer.
>   - `Code` (binary) of the program.
>
> > ## One visual representation of address space
> > <img src="../assets/figure/memory-virtualization/03.png" alt="address space 1" style="height:500px">
> ```
>
> > ## Another visual representation of address space
> > <img src="../assets/figure/memory-virtualization/04.png" alt="address space 2" style="height:500px">
> > *Image taken from [Geeksforgeeks](https://www.geeksforgeeks.org/memory-layout-of-c-program/)*
> ```
```




> ## 7. Hands on: what is in your binary?
>
> - Open a terminal (Windows Terminal or Mac Terminal). 
> - Run the command to launch the image container for your platform:
> - Windows:
> 
> ~~~
> $ podman run --rm --userns keep-id --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it -v /mnt/c/csc331:/home/$USER/csc331:Z localhost/csc-container /bin/bash
> ~~~
> {: .language-bash}
>
> - Mac:
>
> ~~~
> $ docker run --rm --userns=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it -v /Users/$USER/csc331:/home/$USER/csc331:Z csc-container /bin/bash
> ~~~
> {: .language-bash}
>
> - Navigate to `/home/$USER/csc331`
> - Change to directory `ostep-code/cpu-api`, then run `make` to build the programs. 
>
> - Launch a tmux session called `m1` with two vertical panels.  
> - In the left panel, run the following commands:
>
> ~~~
> $ mkdir ~/memory 
> $ cd ~/memory 
> ~~~ 
> {: .language-bash}
>   
> - Create a C program named `simple.c` inside directory `memory`. 
> - **Reminder**: The sequence to create/edit files using `nano` is as follows:
>   - Run `nano -c ile_name`
>   - Type in the contents
>   - When done, press `Ctrl-X`
>   - Press `y` to confirm that you want to save modification
>   - Press `Enter` to confirm the file name to save to. 
> - Create `simple.c` with the following contents:
>   
> > <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=simple.c"></script>
> 
> - In the left panel, run the followings:
>
> ~~~
> $ gcc -g -o simple simple.c 
> $ gdb simple 
> gdb-peda$ info files
> ~~~ 
> {: .language-bash}
>
> - In the right panel, run the followings:
>
> ~~~
> $ cd ~/memory 
> $ gdb simple
> gdb-peda$ b main
> gdb-peda$ run
> gdb-peda$ info files
> ~~~ 
> {: .language-bash}
> 
>
> - The left panel shows the binary file, which is basically a packing list. 
> - The right panel shows how the contents are loaded from static libraries (with memory changed)
> 
> <img src="../assets/figure/memory-virtualization/05.png" alt="view binary contents" style="height:800px">
>
> - Move to the right panel and press `Enter` to continue going through the list.
> - Go through the remaining steps (using `n`) of the debugging process until finish. 
> - Quit `gdb` instances in both panels.  
```


> ## 8. Hands on: what is in your binary?
> 
> - Disable address randomization (permanently). 
> - You only need to do this once using either tmux panels. 
>
> ~~~
> $ echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
> ~~~ 
> {: .language-bash}
>   
> - In the left panel, create `simple2.c` inside `memory` with the following contents:
>   
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=simple2.c"></script>
> 
> - In the right panel, create `simple3.c` inside `memory` with the following contents:
>
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=simple3.c"></script>
>
> - Compile and run `simple2.c` and `simple3.c` normally. 
> - Compare the output. 
> 
> <img src="../assets/figure/memory-virtualization/06.png" alt="view binary contents" style="height:250px">
>
> - But Dr. Ngo just said the stack grows downward ...?
```


> ## 9. Hands on: where the stack grows?  
> 
> - Add one more vertical panel to your tmux session. 
> - Adjust the panels' width (`resize-pane -L/-R`) so that they balance.
> - In the new panel, create `simple4.c` inside `memory` with the following contents:
>   
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=simple4.c"></script>
> 
> - Stack grows downward (high to low) relative to stack frames …
> - Within a stack frame, memory reserved for data are 
> allocated in order of declaration from low to high
> 
> <img src="../assets/figure/memory-virtualization/07.png" alt="where the stack grows" style="height:250px">
>
```


> ## 10. Hands on: observing inner growth (of the stacks)?
> 
> - In the first or second panel (the one next to the result from running 
> `simple4`, create a copy of `simple4.c` called `simple5.c`.
> - Modify `simple5.c` to print out one or two additional variables in each 
> of the functions `f1` and `f2`. 
> - Compile and run `simple5.c` to observe how within each stack frame, 
> memory are allocated in the order from low to high. 
> - In the new panel, create `simple4.c` inside `memory` with the following contents:
>
```


> ## 11. What is address space, really?
> 
> - The **abstraction of physical memory** that the OS is providing to the 
> running program. 
> - How can the OS build this abstraction of a private, potentially large 
> address space for multiple running processes on top of a single physical memory?
>   - This is called **memory virtualization**.
>
```


> ## 12. Goals of memory virtualization
> 
> - `Transparency`: The program should not be aware that memory is virtualized 
> (did you feel anything different when programming?). The program should perceive 
> the memory space as its own private physical memory. 
> - `Efficiency`: The virtualization process should be as efficient as possible
>   - `Time`: not making processes run more slowly
>   - `Space`: not using too much memory for supporting data structures
> - `Protection`: Protection enable the property of isolation: each process should be running 
> in its own isolated memory space, safe against other processes. 
>
```


> ## 13. Dr. Ngo loves his analogies
> 
> - In the firgure to the right, what represents the heap?
> 
> <img src="../assets/figure/memory-virtualization/08.png" alt="foods" style="height:250px">
>
```


> ## 14. Hands on: is memory unlimited?
> 
> - Reduce the number of vertical panels down to 2 and adjust the sizes 
> (see screenshot below).
> - In one of the panels, create `largemem.c` inside `memory` with the following 
> contents, then compile.
> 
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=largemem.c"></script>
>
> - Split the right vertical panel to four (or more) horizontal panels. 
> - In the left panel, first run `free -hm` and study the output. 
> - In the top right panel, inside `memory`, run `largemem` with a command line 
> argument of `200`. 
> - In the left panel, rerun `free -hm` and study the new output.  
> - Subsequently, alternatve between running `largemem` in the right panels and 
> `free -hm` in the left panel, adjusting the command line argument of `largemem`
> such that you run into a segmentation fault in the last panel. 
> - This is the impact of memory allocation (reservation). 
>
> <img src="../assets/figure/memory-virtualization/09.png" alt="foods" style="height:800px">
>
```



{% include links.md %}

