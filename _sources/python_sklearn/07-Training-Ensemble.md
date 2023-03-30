# Ensemble-based Learning


## 7.1 Why Ensemble:
Ensemble is a method in Machine Learning that **combine decision from several ML models** to obtain optimum output.
This espisode get information from [here](https://www.pluralsight.com/guides/ensemble-methods:-bagging-versus-boosting)

![image](https://user-images.githubusercontent.com/43855029/115078334-7b5b5700-9ecd-11eb-93fb-c3f69e740a5c.png)
[Source: Patheos.com](https://www.patheos.com/blogs/driventoabstraction/2018/07/blind-men-elephant-folklore-knowledge/)

Ensemble approaches can reduce variance & Avoid Overfitting by combining results of multiple classifiers on different sub-samples

![image](https://user-images.githubusercontent.com/43855029/114235479-417ad580-994e-11eb-806b-2f73996f864d.png)

Figure. Bias & Variance Tradeoff

- Bias: the difference between the model prediction & observation. High bias: model did not train well.
- Variance: the variability of model prediction from one point to another. High variance: model performs really well in training but having high error rate in testing set


## 7.2 Train model using Ensemble Approach
Ensemble methods use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone.
Unlike a statistical ensemble in statistical mechanics, which is usually infinite, a machine learning ensemble consists of only a concrete finite set of alternative models, but typically allows for much more flexible structure to exist among those alternatives.
Here we will be learning several ensemble models:
- Random Forest
- Bagging
- Boosting 

![image](https://user-images.githubusercontent.com/43855029/115079289-f6713d00-9ece-11eb-90cb-7084e8d7a536.png)


## 7.3 Train model using Bagging (Bootstrap Aggregation)
- The bootstrap method is a resampling technique used to estimate statistics on a population by sampling a dataset with replacement.
- Bootstrap randomly create a small subsets of data from entire dataset
- The subset data has similar characteristic as the entire dataset.

### 7.3.1 Detail explaination of Bagging
There are 3 steps in Bagging

![image](https://user-images.githubusercontent.com/43855029/115079407-202a6400-9ecf-11eb-9c9c-7f3a0bbf1c28.png)

Step 1: Here you replace the original data with new sub-sample data using bootstrapping.

Step 2: Train each sub-sample data using ML algorithm

Step 3: Lastly, you use an average value to combine the predictions of all the classifiers, depending on the problem. Generally, these combined values are more robust than a single model.

### 7.3.2 Implementation of Bagging
Here we use iris data set:
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.6, random_state = 123)
```
First apply **Bagging** with **DecisionTree** model, Bagging's parameter can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html):
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
model_DT = DecisionTreeClassifier()

model_bag_DT = BaggingClassifier(base_estimator=model_DT, n_estimators=100,
                            bootstrap=True, n_jobs=-1,
                            random_state=123)
model_bag_DT.fit(X_train, y_train)

model_bag_DT.score(X_train,y_train),model_bag_DT.score(X_test,y_test)
```
The output accuracy from **Bagging** with **DecisionTree** for train/testing have : `(1.0, 0.9666666666666667)`

## 7.4 Train model using Boosting

http://uc-r.github.io/public/images/analytics/gbm/boosted_stumps.gif

- Boosting is an approach to convert weak predictors to get stronger predictors.
- Boosting follows a sequential order: output of base learner will be input to another
- If a base classifier is misclassifier (red box), its weight is increased and the next base learner will classify more correctly.
- Finally combine the classifier to predict result

![image](https://user-images.githubusercontent.com/43855029/115079476-39331500-9ecf-11eb-9af5-cb3cb2948cf0.png)

More information on Boosting can be found [here](https://www.analyticsvidhya.com/blog/2015/11/quick-introduction-boosting-algorithms-machine-learning/)

### 7.4.1 Adaptive Boosting: Adaboost
- Adaptive: weaker learners are tweaked by misclassify from previous classifier
- AdaBoost is best used to boost the performance of decision trees on binary classification problems.
- Better for classification rather than regression.
- Sensitive to noise

#### Implementation of Adaboost
```python
from sklearn.ensemble import AdaBoostClassifier
model_AD = AdaBoostClassifier(n_estimators=100, learning_rate=0.03).fit(X_train, y_train)

model_AD.score(X_train,y_train),model_AD.score(X_test,y_test)
```
The output accuracy from **AdaBoost**  for train/testing have : `(0.9333333333333333, 0.8333333333333334)`

### 7.4.2 Gradient Boosting Machines: 
- Extremely popular ML algorithm
- Widely used in Kaggle competition
- Ensemble of shallow and weak successive tree, with each tree learning and improving on the previous

```python
from sklearn.ensemble import GradientBoostingClassifier
model_GBM = GradientBoostingClassifier(n_estimators=100).fit(X_train,y_train)

model_GBM.score(X_train,y_train),model_GBM.score(X_test,y_test)
```
The output accuracy from **GradientBoosting**  for train/testing have : `(1.0, 0.9333333333333333)`

## 7.5 Compare Bagging and Boosting technique:
![image](https://user-images.githubusercontent.com/43855029/115079914-e443ce80-9ecf-11eb-8b19-622abbfe026c.png)

## 7.6 Conclusions
- Ensemble overcome the limitation of using only single model
- Between bagging and boosting, there is no better approach without trial & error.
