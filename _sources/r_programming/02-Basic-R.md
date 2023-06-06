# Basics of R


```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How to do basic arithmetics
  - How to initialize a variable
  - How to get help
- Objectives:
  - R built-in functions
- Keypoints:
  - Use RStudio to write and run R programs.
  - R has the usual arithmetic operators and mathematical functions.
  - Use `<-` to assign values to variables.
  - Use `ls()` to list the variables in a program.
  - Use `rm()` to delete objects in a program.
  - Use `sessionInfo()` to get detail of the current loaded environment and packages

```

```{admonition} Input to R
:class: dropdown

- In R console, the symbol `>` stands for `R prompt`.
- The `#` is for comment insert.
- To clean the existing environment, remove all memory in previous sessions:

~~~r
> rm(list=ls())
~~~

```

```{admonition} Using R as calculator
:class: dropdown

- When using R as a calculator, the order of operations is the same as you
would have learned back in school.
- From highest to lowest precedence:
  - Parentheses: `(`, `)`
  - Exponents: `^` or `**`
  - Multiply: `*`
  - Divide: `/`
  - Add: `+`
  - Subtract: `-`
  - Other math functions: `sin, cos, log(), log10(), exp`

~~~r
a <- (1+2)*3-4^5
b <- sin(1)+log10(20)*exp(2)
~~~

```

```{admonition} Comparisons in R
:class: dropdown

- `==`: equality
- `!=`: inequality 
- `<`& `<=`: less than & less than or equal to
- `>`& `>=`: more than & more than or equal to

~~~r
1==1
~~~

```

```{admonition} Assign Variables
:class: dropdown

- To assign variable in R, we can use both `<-` and `=` sign

~~~r
a <- 1
b = 2
~~~

- Note that assignment does not print out value to R console. It saves the variable in Environment section:

![image](https://user-images.githubusercontent.com/43855029/114053543-09479a00-985d-11eb-965a-88462449ea89.png)

- To print the variable to console

~~~r
a
print(a)
~~~

- The output will be like this:

~~~r
> a
[1] 1
> print(a)
[1] 1
~~~

- Do not to worry about the `[1]` in front. We will be learning about that later.

```

```{admonition} Working directory
:class: dropdown

One important step in R is to define the working directory. It is particularly useful 
when you are working with files in the working directory and working in Linux 
environment in Palmetto:

~~~r
# print working directory
getwd()
# set working directory on your local computers
setwd('C:/R/') # for Windows
setwd('/user/home/R') # for Macs
~~~

```

```{admonition} Seeking Help
:class: dropdown

- In order to look for help files for function:
  - Put `?` in front of function name, for example `rnorm` 

~~~r
?rnorm
help(rnorm)
str(rnorm)
~~~

- The help section will display:

![image](https://user-images.githubusercontent.com/43855029/114055446-c981b200-985e-11eb-8207-1347edd1f62f.png)

- If you don't kow the exact function name, you can use `??` and R will try 
to find the appropriate function for you. For example, I want to know how 
to compute a correlation coefficient. I can do `??correlation`, and it 
will give me a list of functions that are, one way or another, related 
to correlation, and the first result on the list is the function `corr`, 
which is Pearson's correlation coefficient.

```
