# Control Structure

```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How do I use If-Then-Else structure?
  - How do I use For loops?
  - How do I use While loops?
- Objectives:
  - Write conditional statement with `if...else` and `elseif()`
  - Write and understand `for()` loop
- Keypoints:
  - "Use `if` and `else`"
  - "Use `for` loop "

```


```{admonition} if-else
:class: dropdown

- **if**

~~~r
if (condition){
  do task
}
~~~

- **if...else**

~~~r
if (condition1){
  do task 1
} else {
  do the rest
}
~~~

- **if...elseif...else**

~~~r
if (condition1){
  do task 1
} else if (condition2) {
  do task 2
} else {
  do the rest
}
~~~

- **ifelse()**

~~~r
ifelse(condition,action if true,action if false)
~~~

- **Examples**

~~~r
a <- 5
if (a>3){
  print("a is bigger than 3")
}
~~~

~~~r
a <- 5
if (a>3){
  print("a is bigger than 3")
} else {
  print("a is NOT bigger than 3")
}
~~~

~~~r
a <- 5
if (a>3){
  print("a is bigger than 3")
} else if (a==3) {
  print("a equals to 3")
} else {
  print("a is less than 3")
}
~~~

~~~r
a <- 5
response <- ifelse(a>3,"a is bigger than 3","a is not bigger than 3")
response
class(response)
~~~

```

```{admonition} For Loop
:class: dropdown

- Full Syntax:

~~~r
for (iterator in sequence){
  do task
}
~~~

- Example:

~~~r
for (i in 1:5){
  print(i)
}
~~~

~~~r
for (i in seq(1,5,2)){
  print(i)
}
~~~

- Short Syntax

~~~r
for (i in 1:5) print(i)
~~~

~~~r
for (i in seq(1,5)) print(letters[i])
~~~

```


```{admonition} While Loop
:class: dropdown

- Syntax

~~~r
while (this condition is true){
  do a task
}
~~~

- Example:

~~~r
a <- 1
while (a<5){
  print(a)
  a <- a+1
}
~~~

```

