
# Introduction to concurrency using threads"
teaching: 0
exercises: 0
questions:
- "How to support concurrency?"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"


> ## 1. Review: process calls fork()
> 
> - New PCB (process control block) and address space.
> - New address space is a copy of the entire contents of the parent's 
> address space (up to fork).
> - Resources (file pointers) that point to parent’s resources.
> - **In general, time consuming.**
>
```


> ## 2. Review: process context switch
> 
> - Save A's registers to A's kernel stack.
> - Save A's registers to A's PCB.
> - Restore B's registers from B's PCB.
> - Switch to B's kernel stack.
> - Restore B's registers from B's kernel stack.
> - **In general, time consuming.**
>
```


> ## 3. Example: web server
> 
> - A process listens to requests.
> - When a new request comes in, a child process is created to 
> handle this request.
> - Multiple requests can be handled at the same time by 
> different child processes.
> - What is the problem?
>
> ~~~
> while (1) {
>	  int sock = accept();
>   if (0 == fork()) {
>     handle_request();
>     close(sock);
>     exit(0);
>   }
> }
> ~~~
> {: .language-c}
>
```


> ## 4. Thread: a new abstraction for running processes
> 
> - A normal process is a running program with a single point of execution, 
> i.e, a single PC (program counter).
> - A **multi-threaded** program has **multiple points of execution**, i.e., multiple PCs.
> - Each thread is very much like a separate process, except for one difference:
>   - All threads of the same process share the same address space and thus can 
>   access the same data. 
>
> <img src="../fig/10-concurrency/01.png" alt="pages" style="height:350px">
```


> ## 5. Thread: state of a single thread
> 
> - Each thread has its own PC.
> - Each thread has its own private set of registers for computation.
> - Context switching is still needed. 
> - Threads use Thread Control Blocks (TCP) to store their execution states.
> - Context switching is similar to that of processes, except for:
>   - Thread context-switching keep the same address space (i.e., no need to switch out the page table).
>
```


> ## 6. Example: web server using thread
> 
> ~~~
> int global_counter = 0;
> web_server() {
>   while (1) {
>     int sock = accept();
>     thread_create(handle_request, sock);
>   }
> }
>
> handle_request(int sock) {
>   process request;
>   ++global_counter;
>   close(sock);
> }
> ~~~
> {: .language-c}
>
```


> ## 7. API: POSIX threads (pthreads)
> 
> - Standardized C language thread programming API.
> - `pthreads` specifies the interface of using threads, but not how threads 
> are implemented in OS.
> - Different implementations include: 
>   - kernel-level threads,
>   - user-level threads, or 
>   - hybrid
> - [pthread_create](http://man7.org/linux/man-pages/man3/pthread_create.3.html)
> - [pthread_join](http://man7.org/linux/man-pages/man3/pthread_join.3.html)
```



> ## 8. Hands on: say hello to my little threads ...
>
> - Before turning on the VM, makes sure that you have two processors assigned
> to your VM. 
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
> - Create a directory named `concurrency` inside `~/csc331` and change to this directory
>
> ~~~
> $ mkdir ~/csc331/concurrency
> $ cd ~/csc331/concurrency
> ~~~ 
> {: .language-bash}
>
> - Create `thread_hello.c` with the following contents:
>
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=thread_hello.c"></script>
>
> - Compile and run `thread_hello.c`:
> 
> ~~~
> $ gcc -o thread_hello thread_hello.c -lpthread
> $ ./thread_hello 1
> $ ./thread_hello 2 
> $ ./thread_hello 4
> ~~~ 
> {: .language-bash}
> 
> <img src="../fig/10-concurrency/02.png" alt="thread hello" style="height:400px">
```



> ## 9. Hands on: threads and gdb
>
> - Recompile `thread_hello.c` with gdb support, then run `gdb`:
> 
> ~~~
> $ gcc -g -o thread_hello thread_hello.c -lpthread
> $ gdb thread_hello
> ~~~
> {: .language-bash}
>
> - We will set the breakpoint to the thread function `myThreadFun`, then run the 
> program with one command line argument. 
>
> ~~~
> gdb-peda$ b myThreadFun
> gdb-peda$ run 2
> ~~~ 
> {: .language-bash}
>
> - We are inside a thread
>
> <img src="../fig/10-concurrency/03.png" alt="gdb thread hello" style="height:600px">
>
> - Run `i threads` to see how many threads there are in total.
> - Then run `thread apply all bt` to learn more about the threads. 
> - There are a total of three threads. Thread 1 comes from the main process. The other two 
> threads (2 and 3) where created from the `pthread_create` function call. 
> - The numbered sections under the threads represent the stack frames. 
> 
> ~~~
> gdb-peda$ i threads
> gdb-peda$ thread apply all bt
> ~~~ 
> {: .language-bash}
> 
> <img src="../fig/10-concurrency/04.png" alt="gdb thread backtrace" style="height:600px">
> 
> - The outcomes of the previous command shows the stack frames of each thread. 
> - We can use `thread i` to switch to thread `i`, then `frame j` to switch to the `j`<sup>th</sup>
> of that thread. 
> - `i locals` will print out all local variables of the current stack frame. 
> - Continue running the followings:
> 
> ~~~
> gdb-peda$ thread 1
> gdb-peda$ i locals
> gdb-peda$ frame 1
> gdb-peda$ i locals
> gdb-peda$ frame 3
> gdp-peda$ i locals
> ~~~ 
> {: .language-bash}
>
> <img src="../fig/10-concurrency/05.png" alt="gdb thread backtrace" style="height:600px">
> 
> - When a thread is created, the main process also turns into a management thread and holds to 
> wait for the child threads to finish (`pthread_join`). Each thread (including the main thread)
> is located a segment on stack. 
> - We can use `thread apply i a_command` to apply `a_command` to thread `i`. 
> - Let's advance thread 2 to next commmand:
> 
> ~~~
> gdb-peda$ thread 3
> gdb-peda$ thread apply 3 n
> gdb-peda$
> ~~~
> {: .language-bash}
> 
> - Scroll up a bit and observe. You will see a thread exited. Which thread is this?
> 
> <img src="../fig/10-concurrency/06.png" alt="gdb thread" style="height:600px">
>
> - What happened?
> - Switch back to thread 1, continue running `n` until you are back to the main process. 
> 
> <img src="../fig/10-concurrency/07.png" alt="gdb thread" style="height:600px">
> 
> - Keep running `n` to finish the program. 
> 
```


> ## 10. The problem with threads
> 
> ### Edward Lee (2006). "The Problem with Threads".  Computer 39(5).
> > From a fundamental perspective, threads are seriously flawed 
> > as a computation model because they are wildly nondeterministic... 
> > The programmer’s job is to prune away that nondeterminism. We have 
> > developed tools to assist in the pruning: semaphores, monitors, and 
> > more modern overlays on threads offer the programmer ever more effective 
> > pruning. But pruning a wild mass of brambles rarely yields a satisfactory 
> > hedge. To offer another analogy, a folk definition of insanity is to do 
> > the same thing over and over again and expect the results to be different. 
> > By this definition, we in fact require that programmers of multithreaded 
> > systems be insane. Were they sane, they could not understand their programs.`
> {: .callout}
> 
```


> ## 11. Challenge
> 
> - Inside `concurrency`, change to this directory, and create `thread_matrix.c` with 
> the following contents:
>
> <script src="https://gist.github.com/linhbngo/d2f3a0b28b73a3f48c751410c6c91fd6.js?file=thread_matrix.c"></script>
>
> - Compile `thread_matrix.c` with `-g` then run the program inside `gdb` with 
> the breakpoint set to the `matrix_mul` function. 
> - The `run` command should accept 4 as a command line argument. 
> - Perform the following tasks:
>   - Identify the index of the first C cell on which thread 3 will operate ?
>   - Check the value inside this index from thread 2.
>   - Inside thread 3, advance until the value inside this cell has been modified. 
>   - Check that the value from thread 2 is modified as well. 
>   - Also check that values of start and end are different inside 2 and 3. 
> 
```





{% include links.md %}

