# Unsupervised Learning

# 14. Unsupervised Learning

- No labels are given to the learning algorithm leaving it on its own to find structure in its input. 
- Unsupervised learning can be a goal in itself (discovering hidden patterns in data) or a means towards an end (feature learning).

![image](https://user-images.githubusercontent.com/43855029/114584282-82c1fc80-9c50-11eb-9342-41e5592e7b67.png) ![image](https://user-images.githubusercontent.com/43855029/114584314-89507400-9c50-11eb-9c54-5a589075fd48.png)

- Used when no feature output data
- Often used for clustering data
- Typical method:
```
K-means clustering
Hierarchical clustering
Ward clustering
Partition Around Median (PAM)
```
## 14.1. K-means clustering
### 14.1.1. Explanation of K-means clustering method:
- Given a set of data, we choose K=2 clusters to be splited:

![image](https://user-images.githubusercontent.com/43855029/114584415-a5ecac00-9c50-11eb-8919-807f83ddf23a.png)

- First select 2 random centroids (denoted as red and blue X)

![image](https://user-images.githubusercontent.com/43855029/114584573-d16f9680-9c50-11eb-9dc4-8d918919f565.png)

- Compute the distance between 2 centroid red X and blue X with all the points (for instance using Euclidean distance) and compare with each other. 2 groups are created with shorter distance to 2 centroids

![image](https://user-images.githubusercontent.com/43855029/114584860-0bd93380-9c51-11eb-9afc-3bb9510e9c34.png)

- Now recompute the **new** centroids of the 2 groups (using mean value of all points in the same groups):

![image](https://user-images.githubusercontent.com/43855029/114585002-34f9c400-9c51-11eb-83e0-b5769abf6cd3.png)

- Compute the distance between 2 **new** centroids and all the points. We have 2 new groups:

![image](https://user-images.githubusercontent.com/43855029/114585030-3b883b80-9c51-11eb-8f69-29f6e406e215.png)

- Repeat the last 2 steps until **no more new centroids** created. The model reach equilibrium:

![image](https://user-images.githubusercontent.com/43855029/114585223-6b374380-9c51-11eb-8663-27474956ec61.png)

### 14.1.2. Example with K=3
![image](https://user-images.githubusercontent.com/43855029/114585361-8e61f300-9c51-11eb-965e-dc4d57e9c0eb.png)

![image](https://user-images.githubusercontent.com/43855029/114585502-b81b1a00-9c51-11eb-8015-973216b450ce.png)

### 14.1.3. Implementation
Here we use the iris data set with only predictors
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
iris = load_iris()
X = iris.data
```

Apply Kmeans and plotting
```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

model_KMeans = KMeans(n_clusters=3)
model_KMeans.fit(X)

plt.scatter(X[:,2],X[:,3],c=model_KMeans.labels_)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title('KMeans clustering with 3 clusters')
plt.show()
```

![image](https://user-images.githubusercontent.com/43855029/115735833-c99ea900-a358-11eb-87d8-774efc7fa459.png)

### 14.1.4. How to find optimal K values:
#### 14.1.4.1. Elbow approach
- Similar to KNN method for supervised learning, for K-means approach, we are able to use Elbow approach to find the optimal K values.
- The Elbow approach ues the Within-Cluster Sum of Square (WSS) to measure the compactness of the clusters:
![image](https://user-images.githubusercontent.com/43855029/114587068-4d6ade00-9c53-11eb-932d-0de0c9edef83.png)

The optimal K-values can be found from the Elbow using **method="wss"**:
```python
wss = []
for k in range(1,10):
    model = KMeans(n_clusters=k).fit(X)
    wss.append(model.inertia_)
    
plt.scatter(range(1,10),wss)
plt.plot(range(1,10),wss)
plt.xlabel("Number of Clusters k")
plt.ylabel("Within Sum of Square")
plt.title("Optimal number of clusters based on WSS Method")
plt.show()
```
![image](https://user-images.githubusercontent.com/43855029/115737965-9b21cd80-a35a-11eb-9bcd-0d63e685ec0f.png)

#### 14.1.4.2. Gap-Statistics approach
- Developed by Prof. Tibshirani et al in Stanford
- Applied to any clustering method (K-means, Hierarchical)
- Maximize the Gap function:

![image](https://user-images.githubusercontent.com/43855029/114586376-95d5cc00-9c52-11eb-9b71-ed330cfc50bc.png)

E*n: expectation under a sample size of n from the reference distribution
![image](https://user-images.githubusercontent.com/43855029/114586396-9b331680-9c52-11eb-9b83-955aa256e623.png)

![image](https://user-images.githubusercontent.com/43855029/114586456-af771380-9c52-11eb-9fdb-99cc8df854fb.png)

**Installation:**

This version of Gap Statistics is not official. Until the moment of writing this documentation, no official Gap Statistics has been released in Python.
We use the version from [milesgranger's github](https://github.com/milesgranger/gap_statistic)
```python
!pip install git+git://github.com/milesgranger/gap_statistic.git
!pip install gapstat-rs
```
Implement Gap-Statistics:
```python
from gap_statistic import OptimalK

optimalK = OptimalK(n_jobs=1) # No parallel
n_clusters = optimalK(X[:,1:4], cluster_array=np.arange(1, 15))
print('Optimal clusters: ', n_clusters)
```

Plot Gap-Statistics:
```python
import matplotlib.pyplot as plt
plt.plot(optimalK.gap_df.n_clusters, optimalK.gap_df.gap_value, linewidth=3)
plt.scatter(optimalK.gap_df[optimalK.gap_df.n_clusters == n_clusters].n_clusters,
            optimalK.gap_df[optimalK.gap_df.n_clusters == n_clusters].gap_value, s=250, c='r')
plt.grid(True)
plt.xlabel('Cluster Count')
plt.ylabel('Gap Value')
plt.title('Gap Values by Cluster Count')
plt.show()
```
![image](https://user-images.githubusercontent.com/43855029/115745658-a298a500-a361-11eb-8071-6af68f7eb428.png)

## 14.2. Comparison between different clustering methods in sklearn:
- This is example from [sklearn](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)
- The source code for image below can be found [here](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-download-auto-examples-cluster-plot-cluster-comparison-py)

![image](https://user-images.githubusercontent.com/43855029/115748324-0f14a380-a364-11eb-8a06-6d073b4d99c4.png)

