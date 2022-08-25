
# Introduction to OpenMP"
teaching: 0
exercises: 0
questions:
- "What is the OpenMP model?"
objectives:
- "Know the target hardware architecture for OpenMP"
- "Be able to compile and run an OpenMP program."
- "Understand the concept of parallel regions."
keypoints:
- " "


> ## Target hardware
> - Single computing node, multiple sockets, multiple cores.  
> - Dell PowerEdge M600 Blade Server. 
> <img src="../assets/figure/03-intro-openmp/01.jpg" alt="multi-socket motherboard" style="height:400px">
> - Intel Sandy Bridge CPU. 
> <img src="../assets/figure/03-intro-openmp/02.jpg" alt="Intel Sandy Bridge CPU" style="height:400px">
> - In summary
>   - Node with up to four sockets.
>   - Each socker has up to 60 cores. 
>   - Each core is an independent CPU. 
>   - Each core has access to all the memory on the node. 
```


> ## Target software
> - Provide wrappers for `threads` and `fork/join` model of parallelism.   
>   - Program originally runs in sequential mode. 
>   - When parallelism is activated, multiple `threads` are `forked` from the 
>   original proces/thread (`master` thread). 
>   - Once the parallel tasks are done, `threads` are `joined` back to the original 
>   process and return to sequential execution.  
> <img src="../assets/figure/03-intro-openmp/fork-join.jpeg" alt="threads/fork-join models" style="height:400px">
> - The threads have access to all data in the `master` thread. This is `shared` data. 
> - The threads also have their own private memory stack. 
```


> ## Basic requirements to write, compile, and run an OpenMP program
> - Source code (C) needs to include `#include <omp.h>`   
> - Compiling task need to have `-fopenmp` flag.  
> - Specify the environment variable **OMP_NUM_THREADS**.   
```


> ## OMP directives
> - OpenMP must be told when to parallelize.    
> - For C/C++, `pragma` is used to annotate:
> ~~~
> #pragma omp somedirective clause(value, othervalue)
>   parallel statement;
> ~~~
> {: .language-c}
> - or
> ~~~
> #pragma omp somedirective clause(value, othervalue)
> {
>   parallel statement 1;
>   parallel statement 2;
>   ...
> }
> ~~~
> {: .language-c}  
```

> ## Hands-on 1: Setup directory
>
> - Create a directory named `csc466` inside your home directory, 
> then change into that directory.
> - Next, create a directory called `openmp`, and change into that directory
> ~~~
> $ cd
> $ mkdir csc466
> $ cd csc466
> $ mkdir openmp
> $ cd openmp
> ~~~
> {: .language-bash}
> 
> <img src="../assets/figure/03-intro-openmp/04.png" alt="create directories" style="height:200px">
>
```


> ## Hands-on 2: Create hello_omp.c
>
> - In the **EXPLORER** window, right-click on `csc466/openmp` and select `New File`.
> - Type `hello_omp.c` as the file name and hits Enter. 
> - Enter the following source code in the editor windows:
> - Save the file when you are done: 
>   - `Ctrl-S` for Windows/Linux
>   - `Command-S` for Macs
> - **Memorize your key-combos!**.
>
> ~~~
> #include <omp.h>
> #include <stdio.h>
> #include <stdlib.h>
>
> int main (int argc, char *argv[]) {
>   /* Fork a team of threads giving them their own copies of variables */
>   #pragma omp parallel 
>   {
>     /* Obtain thread number */
>     int tid = omp_get_thread_num();
>     printf("Hello World from thread = %d\n", tid);
>
>     /* Only master thread does this */
>     if (tid == 0) {
>       int nthreads = omp_get_num_threads();
>       printf("Number of threads = %d\n", nthreads);
>     }
>   } /* All threads join master thread and disband */
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/03-intro-openmp/05.png" alt="create hello_omp.c" style="height:700px">
> - Line 1: Include `omp.h` to have libraries that support OpenMP. 
> - Line 7: Declare the beginning of the `parallel` region. **Pay attention to how the curly bracket
> is setup, comparing to the other curly  brackets.**
> - Line 10: `omp_get_thread_num` gets the ID assigned to the thread and then assign
> it to a variable named `tid` of type `int`.
> - Line 15: `omp_get_num_threads` gets the value assigned to `OMP_NUM_THREADS` and return it to 
> a variable named `nthreads` of type `int`. 
```


> ## What's important?
> - `tid` and `nthreads`.    
> - They allow us to coordinate the parallel workloads.   
> - Specify the environment variable **OMP_NUM_THREADS**. 
> 
> ~~~
> $ export OMP_NUM_THREADS=4
> ~~~
> {: .language-bash}  
```


> ## Example: trapezoidal
> - Problem: estimate the integral of $$y=x^2$$ on $$[2,8]$$ using trapezoidal rule. 
> four threads.     
> - With 4 threads: `nthreads=4`. 
>   - How to decide which thread will handle which segment?
>   - How to get all results back together?    
> <img src="../assets/figure/03-intro-openmp/06.png" alt="trapezoidal rule" style="height:700px"> 
```


> ## Hands-on 3: Trapezoid implementation
>
> - In the **EXPLORER** window, right-click on `csc466/openmp` and select `New File`.
> - Type `trapezoid.c` as the file name and hits Enter. 
> - Enter the following source code in the editor windows:
> - Save the file when you are done: 
>   - `Ctrl-S` for Windows/Linux
>   - `Command-S` for Macs
> - **Memorize your key-combos!**.
>
> ~~~
> #include <omp.h>
> #include <stdio.h>
> #include <stdlib.h>
>
> int main (int argc, char *argv[]) {
>   //init parameters and evaluators
>   double a = atof(argv[1]);
>   double b = atof(argv[2]);
>   int N = atoi(argv[3]);
>   int nthreads = atoi(argv[4]);
>   double partial_sum[nthreads];
>   double h = ((b - a) / nthreads);    
>
>   omp_set_num_threads(nthreads);
>   #pragma omp parallel 
>   {
>     int tid = omp_get_thread_num();
>     /* number of trapezoids per thread */
>     int partial_n = N / nthreads;
>     double delta = (b - a)/N;
>     double local_a = a + h * tid;
>     double local_b = local_a + delta;
>     for (int i = 0; i < partial_n; i++) {
>       partial_sum[tid] += (local_a * local_a + local_b * local_b) * delta / 2;
>       local_a = local_b;
>       local_b += delta;
>     }
>   } 
>   double sum = 0;
>   for (int i = 0; i < nthreads; i++) {
>     sum += partial_sum[i];
>   }
>   printf("The integral is: %.4f\n", sum);
>   return 0;
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/03-intro-openmp/07.png" alt="create trapezoid.c" style="height:1000px">
```


> ## Hands-on 4: A bit more detailed
>
> - Modify the `trapezoid.c` so that it looks like below. 
> - Save the file when you are done: 
>   - `Ctrl-S` for Windows/Linux
>   - `Command-S` for Macs
> - **Memorize your key-combos!**.
>
> ~~~
> #include <omp.h>
> #include <stdio.h>
> #include <stdlib.h>
>
> int main (int argc, char *argv[]) {
>   //init parameters and evaluators
>   double a = atof(argv[1]);
>   double b = atof(argv[2]);
>   int N = atoi(argv[3]);
>   int nthreads = atoi(argv[4]);
>   double partial_sum[nthreads];
>   double h = ((b - a) / nthreads);    
> 
>   omp_set_num_threads(nthreads);
>   #pragma omp parallel 
>   {
>     int tid = omp_get_thread_num();
>     /* number of trapezoids per thread */
>     int partial_n = N / nthreads;
>     double delta = (b - a)/N;
>     double local_a = a + h * tid;
>     double local_b = local_a + delta;
>     for (int i = 0; i < partial_n; i++) {
>       partial_sum[tid] += (local_a * local_a + local_b * local_b) * delta / 2;
>       local_a = local_b;
>       local_b += delta;
>     }
>     printf("Thread %d calculate a partial sum of %.4f from %.4f to %.4f\n", tid, partial_sum[tid], a + h*tid, local_a);
>   } 
>   double sum = 0;
>   for (int i = 0; i < nthreads; i++) {
>     sum += partial_sum[i];
>   }
>   printf("The integral is: %.4f\n", sum);
>   return 0;
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/03-intro-openmp/08.png" alt="modify trapezoid.c" style="height:1000px">
```


> ## Challenge 1:
> 
> Alternate the `trapezoid.c` code so that the parallel region will 
> invokes a function to calculate the partial sum. 
>  
> > ## Solution
> > 
> > ~~~
> > #include <omp.h>
> > #include <stdio.h>
> > #include <stdlib.h>
> > 
> > double trap(double a, double b, int N, int nthreads, int tid) {
> >   double h = ((b - a) / nthreads);  
> >   int partial_n = N / nthreads;
> >   double delta = (b - a)/N;
> >   double local_a = a + h * tid;
> >   double local_b = local_a + delta;
> >   double p_sum = 0;
> >   for (int i = 0; i < partial_n; i++) {
> >     p_sum += (local_a * local_a + local_b * local_b) * delta / 2;
> >     local_a = local_b;
> >     local_b += delta;
> >   }
> >   return p_sum;
> > }
> > 
> > int main (int argc, char *argv[]) {
> >    //init parameters and evaluators
> >   double a = atof(argv[1]);
> >   double b = atof(argv[2]);
> >   int N = atoi(argv[3]);
> >   int nthreads = atoi(argv[4]);
> >   double partial_sum[nthreads];
> >
> >   omp_set_num_threads(nthreads);
> >   #pragma omp parallel 
> >   {
> >     int tid = omp_get_thread_num();
> >     partial_sum[tid] = trap(a, b, N, nthreads, tid) ;
> >   } 
> >   double sum = 0;
> >   for (int i = 0; i < nthreads; i++) {
> >     sum += partial_sum[i];
> >   }
> >   printf("The integral is: %.4f\n", sum);
> >   return 0;
> > } 
> > ~~~
> > {: .language-c}
> > 
> {: .solution}
{: .challenge}


> ## Challenge 2:
> 
> - Write a program called `sum_series.c` that takes a single integer `N` as a command
> line argument and calculate the sum of the first `N` non-negative integers.  
> - Speed up the summation portion by using OpenMP.  
> - Assume N is divisible by the number of threads. 
>  
> > ## Solution
> > 
> > ~~~
> > #include <omp.h>
> > #include <stdio.h>
> > #include <stdlib.h>
> > 
> > int sum(int N, int nthreads, int tid) {
> >   int count = N / nthreads;  
> >   int start = count * tid + 1;
> >   int p_sum = 0;
> >   for (int i = start; i < start + count; i++) {
> >     p_sum += i;
> >   }
> >   return p_sum;
> > }
> > 
> > int main (int argc, char *argv[]) {
> >   int N = atoi(argv[1]);
> >   int nthreads = atoi(argv[2]);
> >   int partial_sum[nthreads];
> >    
> >   omp_set_num_threads(nthreads);
> >   #pragma omp parallel 
> >   {
> >     int tid = omp_get_thread_num();
> >     partial_sum[tid] = sum(N, nthreads, tid) ;
> >   } 
> >   int sum = 0;
> >   for (int i = 0; i < nthreads; i++) {
> >     sum += partial_sum[i];
> >   }
> >   printf("The sum of series is: %.4f\n", sum);
> >   return 0;
> > } 
> > ~~~
> > {: .language-c}
> > 
> {: .solution}
{: .challenge}


> ## Challenge 3:
> 
> - Write a program called `sum_series_2.c` that takes a single integer `N` as a command
> line argument and calculate the sum of the first `N` non-negative integers.  
> - Speed up the summation portion by using OpenMP.  
> - There is no assumtion that N is divisible by the number of threads. 
>  
> > ## Solution
> > 
> > ~~~
> > #include <omp.h>
> > #include <stdio.h>
> > #include <stdlib.h>
> > 
> > int sum(int N, int nthreads, int tid) {
> >   int count = N / nthreads;  
> >   int start = count * tid;
> >   int end = start + count;
> >   int p_sum = 0;
> >
> >   for (int i = start; i < end; i++) {
> >     p_sum += i;
> >   } 
> >   if (tid < remainder) {
> >     p_sum += count * remainder + tid + 1;
> >   }
> >
> >   return p_sum;
> > }
> > 
> > int main (int argc, char *argv[]) {
> >   int N = atoi(argv[1]);
> >   int nthreads = atoi(argv[2]);
> >   int partial_sum[nthreads];
> >    
> >   omp_set_num_threads(nthreads);
> >   #pragma omp parallel 
> >   {
> >     int tid = omp_get_thread_num();
> >     partial_sum[tid] = sum(N, nthreads, tid) ;
> >   } 
> >   int sum = 0;
> >   for (int i = 0; i < nthreads; i++) {
> >     sum += partial_sum[i];
> >   }
> >   printf("The sum of series is: %.4f\n", sum);
> >   return 0;
> > } 
> > ~~~
> > {: .language-c}
> > 
> {: .solution}
{: .challenge}


> ## Hands-on 5: Trapezoid implementation with timing
>
> - In the **EXPLORER** window, right-click on `csc466/openmp` and select `New File`.
> - Type `trapezoid_time.c` as the file name and hits Enter. 
> - Enter the following source code in the editor windows (You can copy the contents of `trapezoid.c` with function from **Challenge 1** as a starting point):
> - Save the file when you are done: 
>   - `Ctrl-S` for Windows/Linux
>   - `Command-S` for Macs
> - **Memorize your key-combos!**.
>
> ~~~
> #include <omp.h>
> #include <stdio.h>
> #include <stdlib.h>
> #include <time.h>
>
> int main (int argc, char *argv[]) {
>   //init parameters and evaluators
>   double a = atof(argv[1]);
>   double b = atof(argv[2]);
>   int N = atoi(argv[3]);
>   int nthreads = atoi(argv[4]);
>   double partial_sum[nthreads];
>   double h = ((b - a) / nthreads);  
>   clock_t start, end;  
> 
>   omp_set_num_threads(nthreads);
>   start = clock();
>   #pragma omp parallel 
>   {
>     int tid = omp_get_thread_num();
>     /* number of trapezoids per thread */
>     int partial_n = N / nthreads;
>     double delta = (b - a)/N;
>     double local_a = a + h * tid;
>     double local_b = local_a + delta;
>     for (int i = 0; i < partial_n; i++) {
>       partial_sum[tid] += (local_a * local_a + local_b * local_b) * delta / 2;
>       local_a = local_b;
>       local_b += delta;
>     }
>   } 
>   end = clock();
>   double sum = 0;
>   for (int i = 0; i < nthreads; i++) {
>     sum += partial_sum[i];
>   }
>   printf("The integral is: %.4f\n", sum);
>   printf("The run time is: %.4f\n", ((double) (end - start)) / CLOCKS_PER_SEC);
>   return 0;
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/03-intro-openmp/09.png" alt="create trapezoid.c" style="height:700px">
>
> - How's the run time?
```

{% include links.md %}




