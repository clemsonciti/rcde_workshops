# Ploting with ggplot

```{admonition} Learning objectives
:class: dropdown

- Questions:
  - How to plot in R using ggplot2 package
- Objectives:
  - Learn advanced plotting using ggplot2
- Keypoints:
  - ggplot2

```

```{admonition} ggplot
:class: dropdown

- `ggplot2` is a graphics package, written by Hadley Wickham, a 
grad student at Iowa State, based on the ideas from the book 
"Grammar of Graphics" by Leland Wilkinson. Let's install it (it 
will install multiple additional packages that it requires):

~~~r
install.packages("ggplot2")
library(ggplot2)
~~~

```


```{admonition} Basic component of ggplot
:class: dropdown

- A data frame
- aes: aesthetic mappings showing how data are mapped to color, size
- geoms: geometric objects like points, lines, shapes.
- facets: for conditional plots.
- stats: statistical transformations like binning, quanti les, smoothing.
- scales: what scale an aesthetic map uses
- coordinate system

![image](https://user-images.githubusercontent.com/43855029/114095124-0fed0600-988b-11eb-924c-868236195c2a.png)

```


```{admonition} Type of ggplot
:class: dropdown

- Basic qplot
  - Same as plot in Base plot
  - Nicer graphics than Base plot
  - Difficult for customize
- Advanced ggplot
  - Flexible with many built-in function
- A quick way to get familiar with `ggplot2` is the 
`qplot` function, which stands for *quick plot*. 
Let's do a quick scatter plot from the `iris` dataset, 
plotting sepal length versus petal length:

~~~r
qplot(Sepal.Length, Petal.Length, data=iris)
~~~

- Notice that it already looks nicer than the basic R plots 
we did in the last chapter. Now, let's plot different species 
of iris with different colors and shapes:

~~~r
qplot(Sepal.Length, Petal.Length, data=iris,
      color=factor(Species),
      shape=factor(Species))
~~~

![image](https://user-images.githubusercontent.com/43855029/114095545-8ab62100-988b-11eb-8383-38d4a0802423.png)

- Now, let's add smooth lines which show trends in the data:

~~~r
qplot(Sepal.Length, Petal.Length, data=iris,
      color=factor(Species),
      shape=factor(Species),
      geom=c("point","smooth"))
~~~

![image](https://user-images.githubusercontent.com/43855029/114095674-b507de80-988b-11eb-8a9f-852ed19ed08a.png)

- Let's make these lines straight -- that is, let's fit a linear 
model to each species' data:

~~~r
qplot(Sepal.Length, Petal.Length, data=iris,
      color=factor(Species),
      shape=factor(Species),
      geom=c("point","smooth"), method="lm")
~~~

![image](https://user-images.githubusercontent.com/43855029/114095642-aae5e000-988b-11eb-925b-91336205073d.png)

- Let's make a density plot (a smoothed histogram) of 
sepal lengths of each species:

~~~r
qplot(Sepal.Length,data=iris,geom="density",
      color=Species)
~~~

- There are many more ways to use ggplot2. Some useful (and beautiful) 
examples of code are here:
http://r-statistics.co/Top50-Ggplot2-Visualizations-MasterList-R-Code.html

![image](https://user-images.githubusercontent.com/43855029/114096068-3c555200-988c-11eb-849a-1332fcf7c8f5.png)

```


```{admonition} Basic qplot: Facets
:class: dropdown

~~~r
qplot(Sepal.Length,Petal.Length,facets=.~Species, data=iris)
~~~

![image](https://user-images.githubusercontent.com/43855029/114096115-4d9e5e80-988c-11eb-8b75-c2a4d88282da.png)

```

```{admonition} Advanced ggplot
:class: dropdown

- Sample plot

~~~r
gp <- ggplot(mpg, aes(hwy, cty))

gp+geom_point(aes(color=cyl))
gp+geom_point(aes(color=factor(cyl)))
gp+geom_point(aes(color=factor(cyl)))+geom_smooth(method="lm")
gp+geom_point(aes(color=factor(cyl)))+geom_smooth(method="lm")
  +facet_grid(.~cyl)
# Save plot to file
ggsave("plot.png",width=5,height=5)
~~~

![image](https://user-images.githubusercontent.com/43855029/114114690-5a807980-98af-11eb-94b2-ae870139819d.png)

```

```{admonition} Annotation
:class: dropdown

- Labels: xlab(), ylab(), labs(), ggtitle()
- global annotation: use theme()
- Standard appearance: theme_bw()

~~~r
gp+geom_point(aes(color=factor(cyl),
              size=factor(cyl)))+
  geom_smooth(method="lm")+
  xlab("Highway miles per gallon")+
  ylab("city miles per gallon")+
  ggtitle("Scatter plot for cty & hwy")+
  xlim(10,40)+ylim(10,40)+
  theme_bw(base_size = 15)
~~~

![image](https://user-images.githubusercontent.com/43855029/114114812-a16e6f00-98af-11eb-91be-aad368dedb50.png)

```


```{admonition} Some nice ggplots featuring
:class: dropdown

- Boxplot

~~~r
ggplot(mpg,aes(x=manufacturer,y=hwy,
               fill=factor(manufacturer)))+
  geom_boxplot()+
  geom_jitter()+
  labs(title="Boxplot for Hwy per manufacturer",x="Manufacturer",y="Highway milage")+
  theme_bw()+coord_flip()+
  theme(legend.position = "none")
~~~

![image](https://user-images.githubusercontent.com/43855029/114114879-c19e2e00-98af-11eb-8ce8-000f14ac24ae.png)

- Violin plot

~~~r
g <- ggplot(mpg, aes(class, cty))
g + geom_violin(aes(fill=class)) + 
  labs(title="Violin plot", 
       subtitle="City Mileage vs Class of vehicle",
       caption="Source: mpg",
       x="Class of Vehicle",
       y="City Mileage")
~~~

![image](https://user-images.githubusercontent.com/43855029/114114954-e7c3ce00-98af-11eb-8040-4dbb0800b5e7.png)

- Histogram

~~~r
g <- ggplot(mpg, aes(displ)) + scale_fill_brewer(palette = "Spectral")
g + geom_histogram(aes(fill=class), 
                   bins=10, 
                   col="black", 
                   size=.1) +   # change number of bins
  labs(title="Histogram with Fixed Bins", 
       subtitle="Engine Displacement across Vehicle Classes",
       x="enginer displacement (m)",
       y="Frequency count") 
~~~

![image](https://user-images.githubusercontent.com/43855029/114115027-0629c980-98b0-11eb-8f8b-2c9bb4c5d6e6.png)

- Scatter plot

~~~r
data("midwest")
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) + 
  xlim(c(0, 0.1)) + 
  ylim(c(0, 500000)) + 
  labs(subtitle="Area Vs Population", 
       y="Population", 
       x="Area", 
       title="Scatterplot", 
       caption = "Source: midwest")
plot(gg)
~~~

![image](https://user-images.githubusercontent.com/43855029/114115089-278ab580-98b0-11eb-96f4-1d3adc70b511.png)

- Density

~~~r
g <- ggplot(mpg, aes(cty))
g + geom_density(aes(fill=factor(cyl)), alpha=0.8) + 
    labs(title="Density plot", 
         subtitle="City Mileage Grouped by Number of cylinders",
         caption="Source: mpg",
         x="City Mileage",
         fill="# Cylinders")+
    theme_bw()
~~~

![image](https://user-images.githubusercontent.com/43855029/114115140-47ba7480-98b0-11eb-87c9-922ae8970516.png)

- Density 2D

~~~r
gg <- ggplot(faithful,aes(x=eruptions,y=waiting))
gg + stat_density_2d(aes(fill=..level..),
                     geom="polygon",color="black")+
     geom_smooth(method="lm",linetype=2,color="red")+
     scale_fill_continuous(low="green",high="red")+
     geom_point() +
     theme_bw()
~~~

![image](https://user-images.githubusercontent.com/43855029/114115221-63be1600-98b0-11eb-86b5-c0f6f0d8ecff.png)

- Geographic visualization with ggplot

~~~r
library(maps)
states <- map_data("state")
ggplot(data = states)+
  geom_polygon(aes(x=long,y=lat,fill=region),
               color="black")+
  coord_fixed(1.3)+
  guides(fill=FALSE)
~~~

![image](https://user-images.githubusercontent.com/43855029/114115281-84866b80-98b0-11eb-9706-0b07e1472a54.png)

~~~r
counties <- map_data("county")
SC_counties <- subset(counties,region == "south carolina")
ggplot(data = SC_counties)+
  geom_polygon(aes(x=long,y=lat,fill=subregion),
               color="black")+
  coord_fixed(1.3)+
  guides(fill=FALSE)
~~~

![image](https://user-images.githubusercontent.com/43855029/114115313-9700a500-98b0-11eb-8771-58631bdc3e54.png)

~~~r
some.eu.countries <- c(
  "Portugal", "Spain", "France", "Switzerland", "Germany",
  "Austria", "Belgium", "UK", "Netherlands",
  "Denmark", "Poland", "Italy", 
  "Croatia", "Slovenia", "Hungary", "Slovakia",
  "Czech republic"
)
# Retrievethe map data
some.eu.maps <- map_data("world", region = some.eu.countries)

ggplot(some.eu.maps, aes(x = long, y = lat)) +
  geom_polygon(aes( group = group, fill = region))+
  scale_fill_viridis_d()+
  theme_void()+
  theme(legend.position = "none")
~~~

![image](https://user-images.githubusercontent.com/43855029/122972677-6633f600-d35e-11eb-9c3c-4b90db22b25e.png)

- Plot Shapefile for geography study
  - Download shape file data [here](https://opendata.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1.zip)
  - Store it in your folder: c:/R/GIS/ in Windows or /user/R/GIS in MacOS
  - Unzip it and rename all files to `Countries_WGS84.*` under `C:/GIS/`
- Install additional packages:

~~~r
install.packages("rgdal")
install.packages("colorspace")
~~~

- Perform plotting

~~~r
library(rgdal)
library(colorspace)
library(maps)

setwd('c:/R/GIS/')
gfile <- readOGR(dsn="Countries_WGS84.shp")
names(gfile)
gfile$CNTRY_NAME

plot(gfile)
plot(gfile,col=rainbow_hcl(50))
llgridlines(gfile,lty=5)
~~~

![image](https://user-images.githubusercontent.com/43855029/114115693-4e95b700-98b1-11eb-8f93-0a27c0922e35.png)

- Plot raster
  - Here we will plot a raster data base using Global land cover data set. 
  The data can be downloaded from [here](http://due.esrin.esa.int/files/Globcover2009_V2.3_Global_.zip).
- Unzip and put the raster data to working directory:

~~~r
install.packages("raster")
library(raster)
library(rgdal)

setwd('c:/R/GIS/')
#import raster
Gcover <- raster("GLOBCOVER_L4_200901_200912_V2.3.tif")
#plot raster
plot(Gcover,main="GLobal Land cover")
~~~

![image](https://user-images.githubusercontent.com/43855029/114116438-b7316380-98b2-11eb-91d0-0ca5a7b2c3d0.png) 

```
