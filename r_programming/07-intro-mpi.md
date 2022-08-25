
# Introduction to MPI"
teaching: 0
exercises: 0
questions:
- " "
objectives:
- "Understand the origin of message passing interface (MPI)"
- "Know the basic MPI routines to identify rank and get total number of participating processes."
- "Understand how to leverage process rank and total process count for work assignment."
keypoints:
- " "


> ## 1. Message passing
> - Processes communicate via messages
> - Messages can be:
>   - Raw data used in actual calculations
>   - Signals and acknowledgements for the receiving processes regarding the workflow.
```


> ## 2. History of MPI: early 80s
> - Various message passing environments were developed.
> - Many similar fundamental concepts:
>   - Cosmic Cube and nCUBE/2 (Caltech), 
>   - P4 (Argonne), 
>   - PICL and PVM (Oakridge), 
>   - LAM (Ohio SC)
```


> ## 3. History of MPI: 1991-1992
> - More than 80 researchers from different institutions in US and Europe agreed 
> to develop and implement a common standard for message passing.
> - Follow-up first meeting of the working group hosted at Supercomputing 1992 in 
> Minnesota. 
>
> <img src="../assets/figure/07-intro-mpi/01.png" alt="MPI letters" style="height:600px">
```


> ## 4. After finalization of working technical draft
> - MPI becomes the *de-facto* standard for distributed memory parallel 
> programming.
> - Available on every popular operating system and architecture.
> - Interconnect manufacturers commonly provide MPI implementations optimized 
> for their hardware.
> - MPI standard defines interfaces for C, C++, and Fortran.
> - Language bindings available for many popular languages (quality varies)
>   - Python (mpi4py)
>   - Java (no longer active)
```


> ## 5. 1994: MPI-1
> - Communicators
>   - Information about the runtime environments
>   - Creation of customized topologies
> - Point-to-point communication
>   - Send and receive messages
>   - Blocking and non-blocking variations
> - Collectives
>   - Broadcast and reduce
>   - Gather and scatter
```


> ## 6. 1998: MPI-2
> - One-sided communication (non-blocking)
>   - Get & Put (remote memory access)
> - Dynamic process management
>   - Spawn
> - Parallel I/O
>   - Multiple readers and writers for a single file
>   - Requires file-system level support (LustreFS, PVFS)
```


> ## 7. 2012: MPI-3
> - Revised remote-memory access semantic
> - Fault tolerance model
> - Non-blocking collective communication
> - Access to internal variables, states, and counters for performance 
> evaluation purposes
```


> ## 8. Hands-on: taz and submitty
> - Your account (login/password) will work on both `taz` and `submitty`. 
> - `USERNAME` represents the login name that you received in email.
> - To access `taz` from a terminal:
> 
> ~~~
> $ ssh USERNAME@taz.cs.wcupa.edu
> ~~~
> {: .language-bash}
>
> - To access `submitty` from a terminal: 
> 
> ~~~
> $ ssh USERNAME@submitty.cs.wcupa.edu
> ~~~
> {: .language-bash}
>
> - The environments on `taz` and `submitty` are similar to one another. 
> In the remainder of these lectures, example screenshots will be taken 
> from `submitty`, but all commands will work on `taz` as well. 
```


> ## 9. Hands-on: create and compile MPI codes
> - Create a directory named `intro-mpi`
> - Change into `intro-mpi`
>
> ~~~
> $ cd
> $ mkdir intro-mpi
> $ cd intro-mpi
> ~~~
> {: .language-bash}
>
> - To create a file from terminal, run `nano -c file_name`. 
> - When finish editing, press `Ctrl-X` to select `Quit and Save`. 
> - Press `Y` to confirm that you want to save. 
> - Press `Enter` to confirm that you are saving to `file_name`. 
> - Inside `intro-mpi`, create a file named `first.c` with the following
> contents
> 
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=first.c"></script>
> 
> - Compile and run `first.c`:
> 
> ~~~
> $ mpicc -o first first.c
> $ mpirun -np 1 ./first
> $ mpirun -np 2 ./first
> $ mpirun -np 4 ./first
> ~~~
> {: .language-bash}
>
> - Both `taz` and `submitty` only have four computing cores, therefore we can (should) 
> only run to a maximum of four processes. 
>
> <img src="../assets/figure/07-intro-mpi/02.png" alt="compile and run first.c" style="height:350px">
```


> ## 10. MPI in a nutshell
> - All processes are launched at the beginning of the program execution.
>   - The number of processes are user-specified
>   - This number could be modified during runtime (MPI-2 standards)
>   - Typically, this number is matched to the total number of cores 
>   available across the entire cluster
> - All processes have their own memory space and have access to the same source codes.
> - `MPI_Init`: indicates that all processes are now working in message-passing mode.
> - `MPI_Finalize`: indicates that all processes are now working in sequential mode 
> (only one process active) and there are no more message-passing activities. 
```


> ## 11. MPI in a nutshell
> - `MPI_COMM_WORLD`: Global communicator
> - `MPI_Comm_rank`: return the rank of the calling process
> - `MPI_Comm_size`: return the total number of processes that are part of 
> the specified communicator. 
> - `MPI_Get_processor_name`: return the name of the processor (core) running the process. 
```


> ## 12. MPI communicators (first defined in MPI-1)
> MPI defines communicator groups for point-to-point and collective 
> communications:
> - Unique IDs (rank) are defined for individual processes within a communicator 
> group.
> - Communications are performed based on these IDs.
> - Default global communication (`MPI_COMM_WORLD`) contains all processes.
> - For `N` processes, ranks go from `0` to `N−1`. 
```


> ## 13. Hands-on: hello.c
>
> - Inside `intro-mpi`, create a file named `hello.c` with the following
> contents
> 
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=hello.c"></script>
> 
> - Compile and run `hello.c`:
> 
> ~~~
> $ mpicc -o hello hello.c
> $ mpirun -np 1 ./hello
> $ mpirun -np 2 ./hello
> $ mpirun -np 4 ./hello
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/07-intro-mpi/03.png" alt="compile and run hello.c" style="height:350px">
```


> ## 14. Hands-on: evenodd.c
>
> - In MPI, processes' ranks are used to enforce execution/exclusion of code 
> segments within the original source code. 
> - Inside `intro-mpi`, create a file named `evenodd.c` with the following
> contents
> 
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=evenodd.c"></script>
> 
> - Compile and run `evenodd.c`:
> 
> ~~~
> $ mpicc -o evenodd evenodd.c
> $ mpirun -np 1 ./evenodd
> $ mpirun -np 2 ./evenodd
> $ mpirun -np 4 ./evenodd
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/07-intro-mpi/04.png" alt="compile and run evenodd.c" style="height:350px">
```


> ## 15. Hands-on: rank_size.c
>
> - In MPI, the values of ranks and size can be used as means to calculate 
> and distribute workload (data) among the processes. 
> - Inside `intro-mpi`, create a file named `rank_size.c` with the following
> contents
> 
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=rank_size.c"></script>
> 
> - Compile and run `rank_size.c`:
> 
> ~~~
> $ mpicc -o rank_size rank_size.c
> $ mpirun -np 1 ./rank_size
> $ mpirun -np 2 ./rank_size
> $ mpirun -np 4 ./rank_size
> ~~~
> {: .language-bash}
>
> <img src="../assets/figure/07-intro-mpi/05.png" alt="compile and run rank_size.c" style="height:800px">
```


{% include links.md %}




