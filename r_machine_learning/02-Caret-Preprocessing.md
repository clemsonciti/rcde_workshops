---
title: "Introduction to Caret"
teaching: 40
exercises: 0
questions:
- "What is Caret"
objectives:
- "Master Caret package for Machine Learning"
keypoints:
- "Caret"
---

## 2.1 What is Caret
![image](https://user-images.githubusercontent.com/43855029/114192772-de704b00-991b-11eb-977e-d6706d4aca33.png)

The caret package (short for **C**lassification **A**nd **RE**gression **T**raining) is a set of functions that attempt to streamline the process for creating predictive models. The package contains tools for, among others:

pre-processing (cleaning up the data)
data splitting (separating the data into training and test sets)
feature selection (selecing a subset of variables for further analysis)
model tuning using resampling (adjusting model parameters)
variable importance estimation (to see which variables drive the prediction)

There are many different modeling functions in R. Some have different syntax for model training and/or prediction. The package started off as a way to provide a uniform interface the functions themselves, as well as a way to standardize common tasks (such as parameter tuning and variable importance).

The current release version can be found on CRAN and the project is hosted on github.
Caret was developed by [Max Kuhn](https://topepo.github.io/caret/index.html)
Here we only touch some of the very basic commands that are useful for our Machine Learning class.

[caret cheatsheet](https://www.analyticsvidhya.com/infographics/Caret-Package-Infographic.pdf)

## 2.2 Why using Caret
- Unified framework for a wide variety of ML algorithms, with consistent syntax
- Possibly the biggest project in R
- All in one supervised learning problem
- Uniform interface
- Standard pre & post processing

## 2.3 Install `caret`
Start R Studio on OpenOD. Lets' pick 10 CPUs, 60 GB of memory, any interconnect, no GPU, R version 4.0.3.

In R console:
```r
install.packages("caret")
```
Once installed, load the caret package to make sure that it works:
```r
library(caret)
```

## 2.4 Pre-processing using `caret`

There are several steps that we will use `caret` for. For preprocessing raw data, we gonna use `caret` in these tasks:
- Preprocessing with missing value
- Data partition: training and testing

### 2.4.1 Visualize important variables
Here we introduce the library `GGally`  with function `ggpairs` to help user in visualizing the input data
```r
install.packages('GGally')
library(GGally)
ggpairs(data=iris,aes(colour=Species))
```
![image](https://user-images.githubusercontent.com/43855029/114196055-01e8c500-991f-11eb-8eaf-816f25e6c534.png)

This image contains an extensive visual summary of the relationships between variables in our data. Interestingly, you can see an exammple of [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) in the relationship between sepal width and sepal length: the correlation is negative for all data, but positive within each data group!

### 2.4.2 Pre-processing with missing value
- Most of the time the input data has missing values (`NA, NaN, Inf`) due to data collection issue (power, sensor, personel). 
- There are three main problems that missing data causes: missing data can introduce a substantial amount of bias, make the handling and analysis of the data more arduous, and create reductions in efficiency
- These missing values need to be treated/cleaned before we can use because "Garbage in => Garbage out".
- There are several ways to treat the missing values:
- Method 1: remove all missing `NA` values
```r
data("airquality") # Here we use this sample data because it contains missing value
summary (airquality)
new_airquality1 <- na.omit(airquality)
summary (new_airquality1)
``` 
- Method 2: Set `NA` to mean value 
```r
NA2mean <- function(x) replace(x, is.na(x), mean(x, na.rm = TRUE))
new_airquality2 <-replace(airquality, TRUE, lapply(airquality, NA2mean))
summary (new_airquality2)
```
- Method 3: Use `Impute` to handle missing values
In statistics, imputation is the process of replacing missing data with substituted values. Because missing data can create problems for analyzing data, imputation is seen as a way to avoid pitfalls involved with listwise deletion of cases that have missing values. That is to say, when one or more values are missing for a case, most statistical packages default to discarding any case that has a missing value, which may introduce bias or affect the representativeness of the results. Imputation preserves all cases by replacing missing data with an estimated value based on other available information. Once all missing values have been imputed, the data set can then be analysed using standard techniques for complete data. There have been many theories embraced by scientists to account for missing data but the majority of them introduce bias. A few of the well known attempts to deal with missing data include: hot deck and cold deck imputation; listwise and pairwise deletion; mean imputation; non-negative matrix factorization; regression imputation; last observation carried forward; stochastic imputation; and multiple imputation.

Here we use `preProcess` function from `caret` to perform `bagImpute` (Bootstrap Aggregation Imputation):
```r
library(caret)
PreImputeBag <- preProcess(airquality,method="bagImpute")
DataImputeBag <- predict(PreImputeBag,airquality)
summary (DataImputeBag)
```

<!--- In addition to `bagImpute`, we also can use `knnImpute` (K-Nearest Neighbour Imputation)
`knnImpute` can also be used to impute missing value, however, it standardizes the data after Imputing:

```r
MData <- airquality[,-c(1,5,6)]
PreImputeKNN <- preProcess(MData,method="knnImpute",k=5)
DataImputeKNN <- predict(PreImputeKNN,MData)

#Convert back to original scale
RescaleDataM <- t(t(DataImputeKNN)*PreImputeKNN$std+PreImputeKNN$mean)
```

**Note** 
`bagImpute` is more powerful and computational cost than `knnImpute`
-->
