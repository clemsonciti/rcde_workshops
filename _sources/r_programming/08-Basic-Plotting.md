# Basic plotting with R

```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How to plot in R
- Objectives:
  - Learn basic plotting tools in R
  - Learn to export graphics to a file
- Keypoints:
  - Plot

```

```{admonition} Data visualization:
:class: dropdown

- Making exploratory graphs
  - To understand data properties
  - To find patterns in data
  - To suggest modeling strategies
  - To "debug" analyses
  - To communicate results
- Principles of analytic graphics
- Plotting systems and graphics devices in R
- The base, lattice, and ggplot2 plotting systems in R

```

```{admonition} Plotting system
:class: dropdown

- There are 3 main plotting systems in R:
  - The base plotting system
  - Start with blank plot and build up the plot
  - Plot is just a series of R command
  - Flexible
- The Lattice plotting system (using `package::lattice`)
  - Plots created using single function call
  - Good for putting many plots to screen
  - Cannot add to plots once created
- The `ggplot` plotting system (using `package::ggplot2`)
  - Similar to Lattice but easier
  - Many default mode
  - Flexible between Base and Lattice


![image](https://user-images.githubusercontent.com/43855029/114093880-a7515980-9889-11eb-800e-0152f2e8c207.png)
![image](https://user-images.githubusercontent.com/43855029/114093825-94d72000-9889-11eb-953f-2b232708b37d.png)
![image](https://user-images.githubusercontent.com/43855029/114093954-b932fc80-9889-11eb-8532-f3db53f6278f.png)
![image](https://user-images.githubusercontent.com/43855029/114093764-82f57d00-9889-11eb-8e8a-bb7d11340f02.png)
![image](https://user-images.githubusercontent.com/43855029/114094073-dff13300-9889-11eb-9f97-6675f7408d04.png)

- R is a data analysis language, so naturally it comes with many 
built-in functions for plotting. Let's look at some of them, in 
application to the `mtcars` data set.

~~~r
data(mtcars)
dim(mtcars)
names(mtcars)
head(mtcars)
print(mtcars)
~~~

- First, let's make a bar plot of the miles-per-gallon values of the 32 
cars. `col` specifies the color.

~~~r
barplot(mtcars$mpg, col="green")
~~~

- Now, let's make a histogram for horsepower values.

~~~r
hist(mtcars$hp, col="magenta")
~~~

- Let's display two jistorgrams on the same plot. We'll use the 
function `par` to specify that the two histograms will be plotted 
stacked to each other, one on the left and one on the right. 

~~~r
par(mfrow=c(1,2))
hist(mtcars$mpg,col="blue")
hist(mtcars$wt,col="blue")
~~~

- Let's create a box plot for miles-per-gallon data. We'll have to 
reset the plot options to let R know we don't use multiple plots 
anymore; this is done with `dev.off()`.

~~~r
dev.off()
boxplot(mtcars$mpg,col="blue",main="Boxplot for mpg")
~~~

- Now, let's make this box plot for every value of cylinders (`mtars$cyl`). 
We will use the same function `boxplot`, but with a few more parameters. 
We will specify the data explicitly, as well as `col` (for colour scheme), 
`main` (main figure title), `xlab` and `ylab` (X- and Y-axis labels). We 
will use the function `legend` to create a legend. We call `factors` to 
find out the unique cylinder values.

~~~r
factor(mtcars$cyl)
boxplot(mpg~cyl,data=mtcars,
        col=terrain.colors(3),main="MPG by car cylinders",
        xlab = "cylinders",ylab="mpg")
legend("topright",c("4","6","8"),fill = terrain.colors(3))
~~~

- And a scatter plot. We'll use the `plot` function for this purpose. 
The dots will be coloured according to the number of cylinders.

~~~r
plot(mtcars$mpg, mtcars$wt, main="Car Fuel vs Weight",
     xlab="Mileage per Gallon",ylab="Weight",
     col = mtcars$cyl,pch=16,cex=3)
legend("topright",legend=c(8,6,4),pch=16,cex=3,
       col=c(8,6,4))
~~~

- Here, `pch` is the plotting character; 16 corresponds to a circle, and 
`cex` is the size of the plotting characters. The full table of plotting characters is here:

![img](https://r-lang.com/wp-content/uploads/2021/02/plot-character-in-R.png)

- What if we want to save a plot? Let's save it as a PDF. Here's how we do it:

~~~r
pdf("myplot.pdf")
boxplot(mtcars$mpg,col="blue",main="Boxplot for mpg")
dev.off()
~~~

```

```{admonition} Graphics Devices
:class: dropdown

- A graphics device is something where you can make a plot appear When 
you make a plot in R, it has to be "sent" to a specific graphics device.

- A window on your computer (screen device): quick visualization
- A PDF, PNG, JPEG file (file device) #recommended for documents, paper, presentation

- The most common place for a plot to be "sent" is the screen device
  - On a Mac the screen device is launched with the quartz()
  - On Windows the screen device is launched with windows()
  - On Unix/Linux the screen device is launched with x11()
  - save graphic to PDF
  - save graphic to PNG, JPEG

~~~r
dev.copy(png,"filename.png") # to save the image to file
dev.off() # to close all the graphical devices
~~~

```
