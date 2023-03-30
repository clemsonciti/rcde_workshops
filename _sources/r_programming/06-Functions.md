# Functions


```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How to write functions in R
- Objectives:
  - Define functions
  - Return value(s) from functions
- Keypoints:
  - Use `function` to define a new function in R
  - Use parameters to pass value to function
  - Load function into program using `source()`

- We have seen some examples of built-in R functions. For some functions, 
you would have to install particular packages. In this chapter, we will 
show you how to write your own functions. 

```

```{admonition} Using custom functions
:class: dropdown

- There are several in-built functions in R that can be used 
to perform analytical tasks, for example: `mean, min, max, quantile,summary`.
- For example, here's the `mean` function, which computes the 
arithmetic average of a vector: 
- Using function mean with missing value

~~~r
mean (c (1, 3, 5, 3, 2))
v <- c(2,NA,4,NaN,6)
mean (v)
mean(v,na.rm=TRUE)
~~~

```


```{admonition} Writing a user-defined function with 1 argument
:class: dropdown

- Syntax:

~~~r
f <- function(arg){
  do function with argument
}
~~~

- Example:

~~~r
squareroot <- function(a){
  a^0.5
}
squareroot(49)
~~~

```

```{admonition} Writing a user-defined function with 2 or more arguments
:class: dropdown

- Syntax:

~~~r
f <- function(arg1,arg2){
  do function with arg1 & arg2
}
~~~

- Example:

~~~r
Addtwo <- function(a,b){
  a+b
}
Addtwo(1,2)
~~~

```


```{admonition} Specifying a variable for the result
:class: dropdown

- Syntax:

~~~r
f <- function(args){
  f1 <- do function with args
  return(f1)
}
~~~

- For example:

~~~r
# Function to convert oF to oC
F2C <- function(temp){
   c <- ((temp - 32) * (5 / 9))
   return(c)
}
F2C(100)
~~~

```


```{admonition} Returning several results in a list
:class: dropdown

- Syntax:

~~~r
f <- function(args){
  do function with args
  out1 <- do1
  out2 <- do2  
  output <- list(out1=out1,out2=out2)
}
~~~

- Example: a function which converts polar coordinates to 
Cartesian coordinates

~~~r
polar2cart <- function (r, phi) {
  x <- r*sin(phi)
  y <- r*cos(phi)
  return (list(x, y))
}
polar2cart(1,pi/6)[1] 
polar2cart(1,pi/6)[2] 
~~~

- Let's specify the names of the two outputs:

~~~r
polar2cart <- function (r, phi) {
  xcoord <- r*sin(phi)
  ycoord <- r*cos(phi)
  return (list(x=xcoord, y=ycoord))
}
polar2cart(1,pi/6)[1] 
polar2cart(1,pi/6)[2] 
polar2cart(1,pi/6)$x
polar2cart(1,pi/6)$y 
~~~

```


```{admonition} Nested functions
:class: dropdown

- In complex data science use cases, we may have to 
work on nested functions, which contain functions within a function.
- For example: Given dataset `mtcars`. Find the mean of fuel 
consumption `mpg` for cars that having 4 cylinders `cyl`

~~~r
data(mtcars)
names(mtcars)

# Step 1: find the cars that having 4 cylinders:
ind <- mtcars$cyl==4
# Step 2: find the fuel consumption of all the cars having 4 cylinders:
fuel_4cyl <- mtcars$mpg[ind]
# Step 3: compute the mean
mean(fuel_4cyl)
~~~

- All the 3 steps can be nested into one command line for experience user:

~~~r
mean(mtcars$mpg[mtcars$cyl==4])
~~~

```


```{admonition} Defensive programming with stopifnot() function
:class: dropdown


- Defensive programming encourages us to frequently check conditions 
and throw an error if something is wrong. 
- For example:

~~~r
F2C <- function(temp){
   stopifnot(is.numeric(temp)==TRUE)
   c <- ((temp - 32) * (5 / 9))
   return(c)
}
F2C(100a)
F2C(100)
~~~

```

 
```{admonition} Saving functions for future use
:class: dropdown

- Let's save our function so we can use it later.
- First, get your working directory by running `getwd()`. 
Then, in a file browser (Windows) or in Finder (Mac), go 
to that directory, and please create a folder "R_workshop". 
Then, in R, let's make this our working directory: `setwd ("R_workshop")`. 
Then, let's list the files in it:

~~~r
list.files (getwd())
~~~

- The result should be empty (`character(0)`) because it is 
an empty directory. If you are familiar with Linux, you can 
use the `Terminal` tab from the console for the same purpose.
- Then, in the R studio Editor, copy-and-paste the `polar2cart` 
function:

~~~r
polar2cart <- function (r, phi) {
  x <- r*sin(phi)
  y <- r*cos(phi)
  return (list(x, y))
}
~~~

...and then save it by doing `File -> Save As` and selecting the name 
`polar2cart.R`. Make sure you are saving it in the `R_workshop` folder.

```

