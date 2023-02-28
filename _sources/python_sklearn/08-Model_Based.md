# Model-based Prediction

## 8.1 Naive Bayes
- Assuming data follow a probabilistic model
- Assuming all predictors are independent (Naïve assumption)
- Use Bayes’s theorem to identify optimal classifiers
- More information on Aplication of Bayes's Theorem in ML can be found [here](https://machinelearningmastery.com/bayes-theorem-for-machine-learning/)


![image](https://user-images.githubusercontent.com/43855029/114339414-20b7a900-9b23-11eb-9ae1-39640f50e06c.png)
![image](https://user-images.githubusercontent.com/43855029/114339497-62485400-9b23-11eb-8511-29e1c9077946.png)

![image](https://user-images.githubusercontent.com/43855029/114339516-6f654300-9b23-11eb-838c-aaf600ca922a.png)

### 8.1.1 Implementation Naive Bayes
Split data
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.6, random_state = 123)
```

Train data using Naive Bayes 
```python
from sklearn.naive_bayes import GaussianNB
model_NB = GaussianNB().fit(X_train,y_train)
model_NB.score(X_train,y_train)
model_NB.score(X_test,y_test)
```
In addition to **GaussianNB**, sklearn also includes: **MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB**.
More information on Naive Bayes using sklearn can be found [here](https://scikit-learn.org/stable/modules/naive_bayes.html)

## 8.2 Linear Discriminent Analysis
- LDA is a supervised learning model that is similar to logistic regression in that the outcome variable is categorical and can therefore be used for classification.
- LDA is useful with two or more class of objects

![image](https://user-images.githubusercontent.com/43855029/114339862-3bd6e880-9b24-11eb-9f4f-8f3af989c724.png)


### 8.2.1 Implementation LDA
Using the same iris data set, the LDA model is built:

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model_LDA = LinearDiscriminantAnalysis().fit(X_train,y_train)
model_LDA.score(X_train,y_train)
model_LDA.score(X_test,y_test)
```

### 8.2.2 Ensemble approach (Bagging) with LDA
```python
from sklearn.ensemble import BaggingClassifier
model_LDAbag = BaggingClassifier(base_estimator = model_LDA,n_estimators=100,
                                 bootstrap=True, n_jobs=-1,
                                 random_state=123)
model_LDAbag.fit(X_train,y_train)
model_LDAbag.score(X_train,y_train)
model_LDAbag.score(X_test,y_test)
```
