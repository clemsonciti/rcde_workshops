
# OpenMP: Work sharing and controlling thread data"
teaching: 0
exercises: 0
questions:
- "How do OpenMP threads implicitly and explicitly share work among themsleves?"
- "How do data are managed?"
objectives:
- "Understand the basic work sharing constructs: for, secions, and single."
- "Understand thread-based data sharing in OpenMP"
- "Understand the outcomes of OpenMP programs with different work sharing constructs."
keypoints:
- " "


> ## 1. Work sharing constructs
> - OpenMP utilizes **work sharing constructs** to facilitate dividing 
> parallelizable work among a number of threads. 
> - The work sharing constructs are:
>   - **for**: divide loop iterations among threads. 
>   - **sections**: divide sections of codes among themselves. 
>   - **single**: the section is executed by a single thread. 
```

> ## 2. Work sharing construct: sections
> - Used when parallelize predetermined number of independent work units. 
> - Within a primary `sections` construct, there can be multiple `section`
> construct. 
> - A `section` can be executed by any available thread in the current 
> team, including having multiple sections done by the same thread. 
```

> ## 3. Hands on: sections
>
> - In the **EXPLORER** window, double-click on `csc466/openmp` and select 
> `New Dir` to create a new directory in `openmp` called `sections`. 
> - Inside `sections`, create a file named `hello_sections.c` with the
> following contents:
>
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=hello_sections.c"></script>
> 
> <img src="../assets/figure/06-work-sharing/work_01.png" alt="compile and run hello_sections.c" style="height:400px">
```

> ## 4. Challenge
> 
> Given the following functions: y=x<sup>4</sup> + 15x<sup>3</sup> + 10x<sup>2</sup> + 2x  
> develop an OpenMP program called `poly_openmp.c` with `sections`/`section` directives. Each
> section should handle the calculations for one term of the polynomial. 
>  
> > ## Solution
> > 
> > <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=poly_openmp.c"></script>
> {: .solution}
{: .challenge}

> ## 5. Work sharing construct: single
> - Limits the execution of a block to a single thread. 
> - All other threads will skip the execution of this block **but** wait until the block is finished
> before moving on. 
> - To enable proceed without waiting, a **nowait** clause can be added. 
```

> ## 6. Hands on: single
>
> - Inside `sections`, create the following files: 
>
> `hello_sections_nosingle.c`: 
>
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=hello_sections_nosingle.c"></script>
> 
> `hello_sections_single.c`: 
> 
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=hello_sections_single.c"></script>
> 
> `hello_sections_single_nowait.c`: 
>
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=hello_sections_single_nowait.c"></script>
>
> Compile and run the above files:
> 
> <img src="../assets/figure/06-work-sharing/work_02.png" alt="compile and run singles" style="height:500px">
```

> ## 7. Shared and private data
> - Data declared outside of a parallel region will be shared among all threads.  
> - Data declared inside of a parallel region will be private to individual thread. 
```

> ## 8. Hands on: problem with shared data
>
> - Inside `sections`, create a file named `counter_openmp.c` with the
> following contents:
>
> <script src="https://gist.github.com/linhbngo/05955842d2a7ce40c9723292a2ded118.js?file=counter_openmp.c"></script>
> 
> <img src="../assets/figure/06-work-sharing/work_03.png" alt="compile and run hello_sections.c" style="height:400px">
```

{% include links.md %}
