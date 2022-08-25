
# OpenMP: parallel regions and loop parallelism"
teaching: 0
exercises: 0
questions:
- "Do we have to manually do everything?"
objectives:
- "Know how to use parallel for pragma"
keypoints:
- "Parallel for allows simplification of code"



> ## Loop parallelism
> - Very common type of parallelism in scientific code     
> - In previous trapezoid example, we calculate the division of iteration manually.  
> - An alternative is to use `parallel for` pragma 
```


> ## Hands-on 1: Sum series implementation
>
> - In the **EXPLORER** window, right-click on `csc466/openmp` and select `New File`.
> - Type `sum_series_for.c` as the file name and hits Enter. 
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
> #include <time.h>
>
> int main (int argc, char *argv[]) {
>   int N = atoi(argv[1]);
>   int nthreads = atoi(argv[2]);
>   int partial_sum[nthreads];
>   clock_t start, end;
> 
>   omp_set_num_threads(nthreads);
>   start = clock();
>   #pragma omp parallel
>   {
>     int tid = omp_get_thread_num();
>     partial_sum[tid] = 0;
>     #pragma omp for
>     for (int i = 0; i <  N; i++) {
>       partial_sum[tid] += i;
>     }
>   }
>   end = clock();
> 
>   int sum = 0;
>   for (int i = 0; i < nthreads; i++) {
>     sum += partial_sum[i];
>   }
>   printf("The integral is: %d\n", sum);
>   printf("The run time is: %.4f\n", ((double) (end - start)) / CLOCKS_PER_SEC);
>   return 0;
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/05-loop-parallelism/01.png" alt="compile and run sum_series_for.c" style="height:300px">
```

> ## Hands-on 2: Improving sum series implementation
>
> - In the **EXPLORER** window, right-click on `csc466/openmp` and select `New File`.
> - Type `sum_series_for_2.c` as the file name and hits Enter. 
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
> #include <time.h>
>
> int main (int argc, char *argv[]) {
>   int N = atoi(argv[1]);
>   int nthreads = atoi(argv[2]);
>   int partial_sum[nthreads];
>   clock_t start, end;
> 
>   omp_set_num_threads(nthreads);
>   start = clock();
>   #pragma omp parallel
>   {
>     int tid = omp_get_thread_num();
>     partial_sum[tid] = 0;
>     int psum = 0;
>     #pragma omp for
>     for (int i = 0; i <  N; i++) {
>       psum += i;
>     }
>     partial_sum[tid] = psum;
>   }
>   end = clock();
> 
>   int sum = 0;
>   for (int i = 0; i < nthreads; i++) {
>     sum += partial_sum[i];
>   }
>   printf("The integral is: %d\n", sum);
>   printf("The run time is: %.4f\n", ((double) (end - start)) / CLOCKS_PER_SEC);
>   return 0;
> }
> ~~~
> {: .language-c}
> 
> <img src="../assets/figure/05-loop-parallelism/02.png" alt="compile and run sum_series_for_2.c" style="height:300px">
```

{% include links.md %}




