# Tree-based Learning Model

## Train model using Decision Tree
-   Tree based learning algorithms are considered to be one of the best and mostly used supervised learning methods.
-   Tree based methods empower predictive models with high accuracy, stability and ease of interpretation
-   Non-parametric and non-linear relationships
-   Types: Categorical and Continuous
![image](https://user-images.githubusercontent.com/43855029/114233972-198a7280-994c-11eb-9f4f-da4ed958961e.png)

### Spliting algorithm
- Gini Impurity: (Categorical)
- Chi-Square index (Categorical)
- Cross-Entropy & Information gain (Categorical)
- Reduction Variance (Continuous)

More information on how to apply the spliting algorithm to split the data can be found [here](https://clemsonciti.github.io/Workshop-Python-ML/Addon_DecisionTree/index.html)

### Pros & Cons
![image](https://user-images.githubusercontent.com/43855029/114234120-548ca600-994c-11eb-889e-e8ec6d313e52.png)

### Implementation
Here we will use `iris` data
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.6,random_state=123)
```
Next we will train using `DecisionTree` with `gini` splitting algorithm:
```python
from sklearn.tree import DecisionTreeClassifier
model_DT = DecisionTreeClassifier(max_depth=3,criterion="gini").fit(X_train,y_train)
```
Once done, we can visualize the tree:
```python
from sklearn import tree
tree.plot_tree(model_DT)
```
However, in order to have a nicer plot:
```python
import graphviz
dot_data = tree.export_graphviz(model_DT, out_file=None,                      
                      filled=True, rounded=True,
                      feature_names=iris.feature_names,
                      special_characters=True)  
graph = graphviz.Source(dot_data) 
graph
```

![image](https://user-images.githubusercontent.com/43855029/134966642-8f3d3009-3d3d-494b-890b-c1295bd01970.png)

Apply decision tree model to predic output of testing data
```python
from sklearn import metrics
y_pred_DT = model_DT.predict(X_test)
metrics.accuracy_score(y_test,y_pred_DT)
```
The **accuracy=0.95**

More information on Decision Tree can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

## Train model using Random Forest
![image](https://user-images.githubusercontent.com/43855029/115076000-f3278280-9ec9-11eb-89b4-b07f3713b105.png)

- Random Forest is considered to be a panacea of all data science problems. On a funny note, when you can’t think of any algorithm (irrespective of situation), use random forest!
- Opposite to Decision Tree, Random Forest use bootstrapping technique to grow multiple tree
- Random Forest is a versatile machine learning method capable of performing both regression and classification tasks. 
- It is a type of ensemble learning method, where a group of weak models combine to form a powerful model.
- The end output of the model is like a black box and hence should be used judiciously.
### Detail explaination
- If there are M input variables, a number m<M is specified such that at each node, m variables are selected at random out of the M. The best split on these m is used to split the node. The value of m is held constant while we grow the forest.
- Each tree is grown to the largest extent possible and  there is no pruning.
- Predict new data by aggregating the predictions of the ntree trees (i.e., majority votes for classification, average for regression).

![image](https://user-images.githubusercontent.com/43855029/114235192-d16c4f80-994d-11eb-9732-571463c2f3f5.png)

### Pros & Cons of Random Forest
![image](https://user-images.githubusercontent.com/43855029/114235213-daf5b780-994d-11eb-83f8-ac7520749dbe.png)

### Implementation of Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
model_RF = RandomForestClassifier(n_estimators=20,criterion="gini").fit(X_train,y_train)
y_pred_RF = model_RF.predict(X_test)
metrics.accuracy_score(y_test,y_pred_RF)
```
The **accuracy=0.97**

In this example, we use `n_estimators=20` to grow `n` number of trees in the forest.
We can see that Random Forest result has better prediction than Decision Tree.

More information on Random Forest can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=random#sklearn.ensemble.RandomForestClassifier)
