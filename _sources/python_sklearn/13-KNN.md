# K-Nearest Neighbour

## 13. K-Nearest Neighbour
- Simplicity but powerful and fast for certain task
- Work for both classification and regression
- Named as Instance Based Learning; Non-parametrics; Lazy learner
- Work well with small number of inputs

![image](https://user-images.githubusercontent.com/43855029/114582045-3d043480-9c4e-11eb-8698-e1c31840401a.png)

### 13.1. Explanation

![image](https://user-images.githubusercontent.com/43855029/114582162-573e1280-9c4e-11eb-8a17-e0d91a38452e.png)

- In KNN, the most important parameter is the K group and the distance computed between points.
- Euclide distance:

![image](https://user-images.githubusercontent.com/43855029/114582319-7a68c200-9c4e-11eb-93f2-37324c034784.png)

### 13.2. Implementation
Here we gonna use the **iris** dataset again:
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.6,random_state=123)
```

Train the model using KNN model with 3 nearest neighbors
```python
from sklearn.neighbors import KNeighborsClassifier
model_KNN = KNeighborsClassifier(n_neighbors=3).fit(X_train,y_train)

model_KNN.score(X_train,y_train)
model_KNN.score(X_test,y_test)
```
![image](https://user-images.githubusercontent.com/43855029/114583370-86a14f00-9c4f-11eb-96a0-59b3c5376952.png)

### 13.3. Other similar models from sklearn.neighbors:
- KNeighborsRegressor: KNN estimators for Regression problem with continuous data
- NearestCentroid
- and [more](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors)
