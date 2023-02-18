# Parallel Computing in R

```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How to utilize multiple cores for R programming
- Objectives:
  - Installing packages
  - Utilizing multiple cores
- Keypoints:
  - foreach()

```

```{admonition} Parallel packages in R
:class: dropdown

- The `doParallel` package is a "parallel backend" for the foreach package. It provides a mechanism needed to execute foreach loops in parallel.
- The `foreach` package must be used in order to execute code in parallel.
- The user must register a parallel backend to use, otherwise foreach will execute tasks sequentially, even when the %dopar% operator is used
- User must register a parallel backend to use. To register doParallel to be used with foreach, you must call the registerDoParallel function.
- We can speed up computation by using *parallel computing*, that is, by 
running computational processes simultaneously on different cores of our computer. 
Most modern computers (laptops or desktops) are multi-cire, that is, they have more 
than one processor (CPU), so they can run more than one thing at a time. Taking 
advantage of this is the main idea behind parallel computing. Later in this workshop, 
we will try the same idea on the Palmetto cluster.
- First, we will need to install some packages. This will be a very common 
task as you start using R; there are many packages out there created by R 
users, which contain functions for specific purposes. We will need to install 
two packages: `foreach` and `doParallel`. In the console, type this:

~~~r
install.packages("foreach")
install.packages("doParallel")
~~~

- Make sure you include the parentheses around the package names. These two 
packages depend on a third package called `iterators`, which should be 
installed automatically. If not, you will need to install it manually. 
- Now, let's load these packages into memory, so we can use the functions 
defined in these packages: 

~~~r
library(foreach)
library(doParallel)
~~~

- Note that, this time, there are no quotation marks around the package names.
- Now that the packages are installed, let's write a function that is somewhat 
computationally intensive. This function will compute the largest eigenvalue of a 
random matrix:

~~~r
max.eig <- function(N) {
     d <- matrix(rnorm(N**2), nrow = N)
     E <- eigen(d)$values
     abs(E)[[1]]
 }
~~~

- Let's save it as max.eig.R in our working directory. Then, we'll need 
to run the `source` command to make sure we can use it:

~~~r
source ("max.eig.R")
~~~

- Now, let's run it in a loop to create ten random matrices, of size 
500x500 each, and compute their largest eigenvalue.

~~~r
m = rep (0, 10)
for (i in 1:10) { m[i] <- max.eig (100) }
m
~~~

- This should take several seconds, depending on the processing power 
of your computer. An alternative way to run it is to use `foreach`:

~~~r
m = foreach (n = 1:10, .combine = c) %do% max.eig (500)
~~~

- This should take about the same time. Now, let's try to run it 
in parallel. For this purpose, we'll need to replace `%do%` with 
`%dopar%`, but first we'll need to initialize the parallel library 
so we take advantage of all available CPUs:

~~~r
registerDoParallel ()
m = foreach (n = 1:10, .combine = c) %dopar% max.eig (500)
~~~

- Now, since we are running the code in parallel, it should take a 
shorter time. Let's get the accurate timing with the `system.time` command:

~~~r
system.time (foreach (n = 1:10, .combine = c) %do% max.eig (500))
system.time (foreach (n = 1:10, .combine = c) %dopar% max.eig (500))
~~~

```


```{admonition} Using foreach package
:class: dropdown

~~~r
foreach(i=1:4, .combine='c') %do% max.eig(i,1)
~~~

- **Nested foreach**

~~~r
k=1
foreach(i=1:4) %:%
   foreach(j=1:4) %do%{
      max.eig(k,1)
      k=k+1
    }      
~~~

```

```{admonition} Using doParallel
:class: dropdown

- Check the number of available cpus:

~~~r
library(doParallel)
co <- detectCores()-1
cl <- makeCluster(co)
registerDoParallel(cl)
~~~

- Apply `doParallel` to `foreach`:

~~~r
system.time(foreach(i=1:200, .combine='c') %do% max.eig(i,1))
system.time(foreach(i=1:200, .combine='c') %dopar% max.eig(i,1))
stopCluster(cl)
~~~

```


```{admonition} Using Parallel and parLapply
:class: dropdown

- Note: this does not work in Windows, mostly applicable to run in Palmetto
- Check number of available processing cpus:

~~~r
library(parallel)
co <- detectCores()-1
cl <- makecluster(co)
~~~ 

- Apply `parLapply`

~~~r
#Load necessary packages on the cluster workers
clusterExport(cl, c('max.eig'))
system.time(foreach(i=1:200, .combine='c') %do% max.eig(i,1))
system.time(parLapply(cl, 1:200, function(z) max.eig(z,1)))
stopCluster(cl)
~~~

```


```{admonition} Using built-in Parallel inside packages
:class: dropdown

- Many packages have built-in paralle function. Here we use a 
bootstraping package: `boot`

~~~r
library(boot)
# function to obtain regression weights
bs <- function(formula, data, indices) {
  d <- data[indices,] # allows boot to select sample
  fit <- lm(formula, d)
  return(coef(fit))
}
# bootstrapping with 1000 replications
system.time(results <- boot(data=mtcars, statistic=bs,
                R=10000, formula=mpg~wt+disp))

system.time(results <- boot(data=mtcars, statistic=bs,
                R=10000, formula=mpg~wt+disp,
                parallel = "snow",ncpus=2))
~~~


```
