# C programming debugging and optimization


## 1. Defects and Infections
>
- A systematic approach to debugging. 
  - The programmer creates a defect 
  - The defect causes an infection 
  - The infection propagates 
  - The infection causes a failure
- Not every defect causes a failure!
- Testing can only show the presence of errors - not their absence. 
  - In other words, if you pass every tests, it means that your program has yet to fail. 
  It does not mean that your program is correct. 



## 2. Explicit debugging
>
- Stating the problem
  - Describe the problem aloud or in writing
  - A.k.a. `Rubber duck` or `teddy bear` method
- Often a comprehensive problem description is sufficient to solve the failure



## 3. Scientific debugging
>
- Before debugging, you need to construct a hypothesis as to the defect.
  - Propose a possible defect and why it explains the failure conditions
- `Ockham’s Razor`: given several hypotheses, pick the simplest/closest to current work
>
<img src="../fig/06-optimization/01.png" alt="scientific debugging" style="height:200px">
>
- Make predictions based on your hypothesis
  - What do you expect to happen under new conditions
  - What data could confirm or refute your hypothesis
- How can I collect that data?
  - What experiments?
  - What collection mechanism?
- Does the data refute the hypothesis?
  - Refine the hypothesis based on the new inputs



## 4. Hands on: bad Fibonacci
>
- Specification defined the first Fibonacci number as 1. 
- Compile and run the following `bad_fib.c` program:
- `fib(1)` returns an incorrect result. Why?
>
~~~
$ gcc -o bad_fib bad_fib.c
$ ./bad_fib
~~~
 
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=bad_fib.c"></script>
>
- Constructing a hypothesis: 
  - `while (n 1)`: did we mess up the loop in fib?
  - `int f`: did we forget to initialize `f`?
- Propose a new condition or conditions
  - What will logically happen if your hypothesis is correct?
  - What data can be 
  - fib(1) failed		// Hypothesis
    - Loop check is incorrect: Change to n >= 1 and run again.
    - f is uninitialized: Change to int f = 1;
- Experiment
  - Only change one condition at a time. 
  - fib(1) failed		// Hypothesis
    - Change to `n >= 1`: ???
    - Change to `int f = 1`: Works.  Sometimes a prediction can be a fix.



## 5. Hands on: brute force approach
>
- Strict compilation flags: `-Wall`, `-Werror`. 
- Include optimization flags (**capital letter o**): `-O3` or `-O0`. 
>
~~~
$ gcc -Wall -Werror -O3 -o bad_fib bad_fib.c
~~~
 
- Use `valgrind`, memory analyzer. 
>
~~~
$ gcc -Wall -Werror -o bad_fib bad_fib.c
$ valgrind ./bad_fib
~~~
>



## 6. Observation
>
- What is the observed result?
  - Factual observation, such as `Calling fib(1) will return 1.`
  - The conclusion will interpret the observation(s)
- Don’t interfere.
  - Sometimes `printf()` can interfere
  - Like quantum physics, sometimes observations are part of the experiment
- Proceed systematically.
  - Update the conditions incrementally so each observation relates to a specific change
- Do NOT ever proceed past first bug.
 



## 7. Learn
>
- Common failures and insights
  - Why did the code fail?
  - What are my common defects?
- Assertions and invariants
  - Add checks for expected behavior
  - Extend checks to detect the fixed failure
- Testing
  - Every successful set of conditions is added to the test suite
 



## 8. Quick and dirty
>
- Not every problem needs scientific debugging
- Set a time limit: (for example)
  - 0 minutes – -Wall, valgrind
  - 1 – 10 minutes – Informal Debugging
  - 10 – 60 minutes – Scientific Debugging
  - 60 minutes – Take a break / Ask for help
 



## 9. Performance realities
>
- There’s more to performance than asymptotic complexity.
- Constant factors matter too!
  - Easily see 10:1 performance range depending on how code is written
  - Must optimize at multiple levels: algorithm, data representations, procedures, and loops
- Must understand system to optimize performance
  - How programs are compiled and executed
  - How modern processors + memory systems operate
  - How to measure program performance and identify bottlenecks
  - How to improve performance without destroying code modularity and generality.
 



## 10. Leveraging cache blocks
>
- Check the size of cache blocks 
>
~~~
$ getconf -a | grep CACHE
~~~

>
<img src="../fig/06-optimization/02.png" alt="cache size" style="height:300px">

- We focus on cache blocks for optimization:
  - If calculations can be performed using smaller matrices of
  A, B, and C (blocks) that all fit in cache, we can further
  minimize the amount of cache misses per calculation. 

<img src="../fig/06-optimization/03.png" alt="block division" style="height:300px">
>
- 3 blocks are needed (for A, B, and C). 
- Each block has dimension B, so the total block size is B<sup>2</sup>
- Therefore: 3B<sup>2</sup< cache_size
- Based on the information above: B = 8 (so that `8 * 8 = 64` fits
in cache line).
- `3 * 8 * 8 < 32768`.




## 11. Hands-on: matrix multiplications
>
- Check the size of cache blocks 
>
~~~
$ getconf -a | grep CACHE
~~~

>
>
- Create the following two files: `matrix_mult.c` and `block_matrix_mult.c` inside a
directory called `06-optimization`. 
>
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=matrix_mult.c"></script>
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=block_matrix_mult.c"></script>
>
- Compile and run the two files:

~~~
$ gcc -o mm matrix_mult.c
$ ./mm 512
$ ./mm 1024
$ ./mm 2048
$ gcc -o bmm block_matrix_mult.c
$ ./bmm 512
$ ./bmm 1024
$ ./bmm 2048
~~~

>
<img src="../fig/06-optimization/04.png" alt="matrix run with block optimization" style="height:300px">
>
- Repeat the process with optimized compilation flag `O3`:
>
~~~
$ gcc -O3 -o mm matrix_mult.c
$ ./mm 512
$ ./mm 1024
$ ./mm 2048
$ gcc -O3 -o bmm block_matrix_mult.c
$ ./bmm 512
$ ./bmm 1024
$ ./bmm 2048
~~~

>
<img src="../fig/06-optimization/05.png" alt="matrix run with block optimization and compiler optimization" style="height:300px">
>



## 12. General optimization: you or your compiler should do it. 
>
- Reduce code motion: reduce frequency with which computation performed
  - Need to produce same results
  - Move code out of loop. 
>
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=block_matrix_mult_2.c"></script>
>
- Reduction in strength: replace costly operation with simpler ones (multiply to addition). 
  - Recognize sequence of products.
>
<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=block_matrix_mult_3.c"></script
>
- Create the following file to automate the installations. 

<script src="https://gist.github.com/linhbngo/d1e9336a82632c528ea797210ed0f553.js?file=eval.sh"></script>
>
~~~
$ chmod 755 eval.sh
$ ./eval.sh block_matrix_mult
$ ./eval.sh block_matrix_mult_2
$ ./eval.sh block_matrix_mult_3
~~~

>
<img src="../fig/06-optimization/06.png" alt="other optimizations" style="height:700px">



## 13. General optimization: when your compiler can't. 
>
- Operate under fundamental constraint
 - Must not cause any change in program behavior
 - Often prevents optimizations that affect only "edge case" behavior
- Behavior obvious to the programmer is not obvious to compiler
  - e.g., Data range may be more limited than types suggest (short vs. int)
- Most analysis is only within a procedure
  - Whole-program analysis is usually too expensive
  - Sometimes compiler does inter-procedural analysis within a file (new GCC)
- Most analysis is based only on static information
  - Compiler has difficulty anticipating run-time inputs
- When in doubt, the compiler must be conservative
>



{% include links.md %}

