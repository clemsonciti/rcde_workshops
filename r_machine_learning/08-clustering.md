# Clustering


## 1. General problem statement: 
```{dropdown}
- Given a **set of data points**, with a notion of **distance** between points, 
**group the points** into some number of **clusters** so that:
  - Members of a cluster are close/similar to each other.
  - Members of different clusters are dissimilar.
- Usually
  - Points are in high-dimensional space (observations have many attributes).
  - Similarity is defined using a distance measure: Euclidean, Cosine, Jaccard, edit distance ...
  
```


## 2. Clustering is a hard problem
```{dropdown}
- Clustering in two dimensions looks easy.  
- Clustering small amounts of data looks easy. 
- In most cases, looks are **not** deceiving. 
- But:
  - Many applications involve not 2, but 10 or 10,000 dimensions. 
  - High-dimensional spaces look different. 

```


## 3. Example: 
```{dropdown}
- Clustering Sky Objects:
  - A catalog of 2 billion **sky objects** represents objects by their radiation in 7 dimensions (frequency bands)
  - Problem: cluster into similar objects, e.g., galaxies, stars, quasars, etc.
- Clustering music albums
  - Music divides into **categories**, and customer prefer a few categories
  - Are **categories** simply genres?
  - Similar Albums have similar sets of customers, and vice-versa
- Clustering documents
  - Group together documents on the same topic. 
  - Documents with similar sets of words maybe about the same topic. 
  - Dual formulation: a topic is a group of words that co-occur in many documents. 

```

## 4. Cosine, Jaccard, Euclidean
```{dropdown}
- Different ways of representing documents or music albums lead to 
different distance measures. 
- Document as `set of words `
  - Jaccard distance
- Document as `point in space of words`. 
  - x_i = 1 if `i` appears in doc. 
  - Euclidean distance
- Document as `vector in space of words`. 
  - Vector from origin to ...
  - Cosine distance. 

```

## 5. Overview: methods of clustering
```{dropdown}
- Hierarchical: 
  - Agglomerative (bottom up): each point is a cluster, repeatedly combining two nearest cluster. 
  - Divisive (top down): start with one cluster and recursively split it. 
- Point assignment:
  - Maintain a set of clusters
  - Points belong to `nearest` cluster

```


## 6. Point assignment: K-means clustering
```{dropdown}
- Assumes `Euclidean` space/distance 
- Pick `k`, the number of clusters. 
- Initialize clsuters by picking on point per cluster. 
- Until converge
  - For each point, place it in the cluster whose current centroid it is nearest. 
     - A cluster centroid has its coordinates calculated as the averages of all its points' coordinates. 
  - After all points are assigned, update the locations of centroids of the `k` clusters. 
  - Reassign all points to their closest centroid. 

```

## 7. The big question
```{dropdown}
- How to select `k`?
- Try different `k`, looking at the change in the average distance to centroid, as `k` increases. 
- Approach 1: sampling
  - Cluster a sample of the data using hierarchical clustering, to obtain `k` clusters.
  - Pick a point from each clsuter (e.g. point closest to centroid)
  - Sample fits in main memory.
- Approach 2: Pick `dispersed` set of points
  - Pick first point at random
  - Pick the next point to be the one whose minimum distance from the selected points is as large as possible. 
  - Repeat until we have `k` points. 

```



## 8. Clustering on Spark
```{dropdown}
- [Libraries for major clustering techniques](https://spark.apache.org/docs/latest/ml-clustering.html) 
  - [K-means](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.KMeans.html)
  - [Bisecting-Kmeans](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.BisectingKMeans.html) 

```


