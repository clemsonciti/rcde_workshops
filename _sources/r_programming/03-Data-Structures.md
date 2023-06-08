# Data Structures

```{admonition} Learning objectives
:class: dropdown

- Questions:
  - Data types / classes in R
  - Random numbers
  - Vectors
  - Missing values
- Objectives:
  - 5 data types / classes of objects
  - Working with vectors
- Keypoints:
  - Classes of objects
  - Vectors

```

```{admonition} Classes of objects
:class: dropdown

- In R, there are 5 main classes of objects:
  - characters a, b
  - numeric: 2.3
  - integer: 5 or 5L
  - complex: 2+3i #consists of real and imaginary parts
  - logical: TRUE/FALSE

~~~r
str <- "string"
class(str)
a <- 5
class(a)
b <- 4L
class(b)
c <- 1+6i 
class(c)
d <- b < 5
class(d)
~~~

```

```{admonition} Logical operations
:class: dropdown

- Logical operations `and` and `or` are computed with `&&` and `||`:

~~~r
a<-TRUE
b<-FALSE
a&&b
a||b
~~~

- Logical `not` is computed with !:

~~~r
!a
!b
a && !b
~~~

```


```{admonition} Numbers
:class: dropdown

- In R, a number is considered a numeric type:

~~~r
e <- 5
class(e)
~~~

- To get an integer, insert `L` as suffix

~~~r
f <- 5L
class(f)
~~~

- Special number: `Inf`: infinity

~~~r
g<-5/0
class(g)
5/0
-5/0
log(0)
~~~

- `NaN` (Not a Number) specifies an undefined value:

~~~r
h <- 0/0
h
log(-1)
asin(4)
~~~

- Sometimes, when you are dealing with data, you have missing values. 
In R, there is a special way to denote missing values: `NA` ("not available"). 
`NaN` is a special type of `NA`.

```

```{admonition} Random Number & seed
:class: dropdown

- Create random numeric numbers using runif

~~~r
runif(1)
runif(3)
runif(2,10,20)
~~~

- Set the seed of R's random number generator, which 
is useful for creating simulations or random objects that can be reproduced.

~~~r
set.seed(1234)
runif(3)
~~~

- Create a sample of random numbers: 

~~~r
sample(12,5)
sample(12)
sample(letters,4)
~~~

- `sample` returns a set of variables, rather than one variable. 
Sets of variables of the same type are called vectors.

```


```{admonition} Vectors
:class: dropdown

- Vectors are sets of variables of the same class, in a certain 
order. The simplest, and a very useful, type of a vector is a range 
of values, specified with a colon:

~~~r
x <- 1:5
x <- -3:3
~~~

- The same could be accomplished with the `seq` function:

~~~r
seq (from=1, to=5)
seq (from=1, to=5, by=2)
seq (1, 5, 2)
~~~

- You can also define a vector by combining a bunch of values 
(`c` stands for "combine"):

~~~r
str <- c("a", "b", "c")
a   <- c(4, 5.6, 20)
b   <- c("TRUE", "FALSE")
~~~

- To create a vector where all elements have the same value, 
use the `rep` function (for "repetition"):

~~~r
x <- rep (3, 5)
~~~

- If a vector is combined from variables of different 
types, R tries to *coerce* them into the same type. 
For example, logical values can be coerced into numbers (TRUE becomes 
1, and FALSE becomes 0):

~~~r
c(TRUE, FALSE)
c(TRUE, FALSE, 5)
~~~

- Likewise, numbers can be coerced into characters:

~~~r
c (5, "a")
~~~

- In this example, everything is ultimately coerced into characters:

~~~r
str1 <- c("a", "b", TRUE, 5, 4.5)
str1
class(str1)
~~~

```


```{admonition} Explicit Coercion
:class: dropdown

- Convert objects from one class to another, using `as.` function:

~~~r
a <- 0:5
class(a)
as.numeric(a)
as.logical(a)
as.character(a)
~~~

- How about Nonsensical Coercion?

~~~r
str <- c("a","b","c")
class(str)
as.numeric(str)
as.logical(str)
as.character(str)
~~~

```


```{admonition} Missing values
:class: dropdown

- In order to detect missing values or bad values 
(`NaN`, `NA`, `Inf`), we can use these functions:
  - is.na() test NA value
  - is.nan() test NaN value
  - is.infinite() test Inf value
  - NaN is NA but the reverse is false

~~~r
v <- c(TRUE, 6, 1/0,NA, NaN,-6/0)
v
is.na(v)
is.nan(v)
is.infinite(v)
~~~

```
