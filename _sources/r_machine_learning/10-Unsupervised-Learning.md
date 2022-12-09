---
title: "Unsupervised Learning"
teaching: 20
exercises: 0
questions:
- "What is Unsupervised Learning in Machine Learning model"
objectives:
- "Learn how to use K-mean clustering in ML model"
keypoints:
- "K-mean"
---


## K-means clustering
### Explanation of K-means clustering method:
- Given a set of data, we choose K=2 clusters to be split into:

![image](https://user-images.githubusercontent.com/43855029/114584415-a5ecac00-9c50-11eb-8919-807f83ddf23a.png)

- First select 2 random centroids (denoted as red and blue X)

![image](https://user-images.githubusercontent.com/43855029/114584573-d16f9680-9c50-11eb-9dc4-8d918919f565.png)

- For both centroids, compute the distance to all the points and compare with each other. 2 groups are created with shorter distance to 2 centroids

![image](https://user-images.githubusercontent.com/43855029/114584860-0bd93380-9c51-11eb-9afc-3bb9510e9c34.png)

- Now recompute the **new** centroids of the 2 groups (using mean value of all points in the same groups):

![image](https://user-images.githubusercontent.com/43855029/114585002-34f9c400-9c51-11eb-83e0-b5769abf6cd3.png)

- Compute the distance between 2 **new** centroids and all the points. We have 2 new groups:

![image](https://user-images.githubusercontent.com/43855029/114585030-3b883b80-9c51-11eb-8f69-29f6e406e215.png)

- Repeat the last 2 steps until **no more new centroids** created. The model reach equilibrium:

![image](https://user-images.githubusercontent.com/43855029/114585223-6b374380-9c51-11eb-8663-27474956ec61.png)

### Example with K=3
![image](https://user-images.githubusercontent.com/43855029/114585361-8e61f300-9c51-11eb-965e-dc4d57e9c0eb.png)

![image](https://user-images.githubusercontent.com/43855029/114585502-b81b1a00-9c51-11eb-8015-973216b450ce.png)

### Implementation
```r
library(ggplot2)
library(factoextra)
library(purrr)
data(iris)
ggplot(iris,aes(x=Sepal.Length,y=Petal.Width))+
      geom_point(aes(color=Species))
set.seed(123)
km <- kmeans(iris[,3:4],3,nstart=20)

table(km$cluster,iris$Species)
fviz_cluster(km,data=iris[,3:4])
```
![image](https://user-images.githubusercontent.com/43855029/114585677-e567c800-9c51-11eb-8cb4-6db443f0698b.png)

### How to find optimal K values:
#### Elbow approach
- Similar to KNN method for supervised learning, for K-means approach, we are able to use Elbow approach to find the optimal K values.
- The Elbow approach ues the Within-Cluster Sum of Square (WSS) to measure the compactness of the clusters:
![image](https://user-images.githubusercontent.com/43855029/114587068-4d6ade00-9c53-11eb-932d-0de0c9edef83.png)

The optimal K-values can be found from the Elbow using **method="wss"**:
```r
fviz_nbclust(iris[,3:4], kmeans, method = "wss")
```
![image](https://user-images.githubusercontent.com/43855029/114586165-5e671f80-9c52-11eb-9ad1-e9170fd6b5ef.png)

<!---
#### 14.1.4.2 Gap-Statistics approach
- Developed by Prof. Tibshirani et al in Stanford
- Applied to any clustering method (K-means, Hierarchical)
- Maximize the Gap function:

![image](https://user-images.githubusercontent.com/43855029/114586376-95d5cc00-9c52-11eb-9b71-ed330cfc50bc.png)

E*n: expectation under a sample size of n from the reference distribution
![image](https://user-images.githubusercontent.com/43855029/114586396-9b331680-9c52-11eb-9b83-955aa256e623.png)

![image](https://user-images.githubusercontent.com/43855029/114586456-af771380-9c52-11eb-9fdb-99cc8df854fb.png)

```r
library(cluster)
# B is number of Monte Carlo bootstrap samples
gap_stat <- clusGap(iris[,3:4], FUN = kmeans, nstart=20, K.max = 10, B = 50)
fviz_gap_stat(gap_stat)
```
![image](https://user-images.githubusercontent.com/43855029/114586485-b9007b80-9c52-11eb-9aae-24effc612e09.png)

-->
