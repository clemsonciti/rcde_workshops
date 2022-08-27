# Regularization and Variable Selection

![image](https://user-images.githubusercontent.com/43855029/114340188-ff57bc80-9b24-11eb-826a-69cb444687d4.png)
- One of the major aspects of training your machine learning model is to avoid overfitting (Using more parameter to best fit the training but on the other hand, failed to evaluate the testing).
- The concept of balancing bias and variance, is helpful in understanding the phenomenon of overfitting

## 9 Regularization
- In order to reduce the Model Complexity or to avoid Multi-Collinearity, one needs to reduce the number of covariates 
(or set the coefficient to be zero).
  - Multi-colinearity: Some independent variables are
  correlated. 
- If the coefficients are too large, let’s penalize them to enforce them to be smaller
- Regularization is a form of multilinear regression, that constrains/regularizes or shrinks the coefficient estimates towards zero.
- In other words, this technique discourages learning a more complex or flexible model, so as to avoid the risk of overfitting
- A simple Multi-Linear Regression look like this:
![image](https://user-images.githubusercontent.com/43855029/114416230-766d6f00-9b7e-11eb-800b-2b7a65782859.png)

=> in which: **β** represents the coefficient estimates for different variables or predictors(x)

The residual sum of squares **RSS** is the loss function of the fitting procedure.
And we need to determine the optimal coefficients **𝛽** to minimize the loss function

![image](https://user-images.githubusercontent.com/43855029/114417635-c39e1080-9b7f-11eb-8465-cbb9e0dff39e.png)

This procedure will adjust the **β** based on the training data. 
If there is any noise in training data, the model will not perform well for testing data. Thus, Regularization comes in and regularizes/shrinkage these 𝛽 towards zero.

There are 3 main types of Regularization. 
- Ridge Regression
- LASSO
- Elastics Nets

### 9.1 Ridge Regression
![image](https://user-images.githubusercontent.com/43855029/121278968-b496be80-c8a1-11eb-9117-250db80ca4d8.png)

**𝜆**: Regularization Penalty, to be selected that the model minimized the error

The Ridge Regression loss function contains 2 elements: (1) RSS is actually the Ordinary Least Square (OLS) function for MLR and (2) The regularization term with **𝜆**:

![image](https://user-images.githubusercontent.com/43855029/121278778-4fdb6400-c8a1-11eb-9141-46d995d07061.png)

- Selecting good **𝜆** is essential. In this case, Cross Validation method should be used
- Ridge Regression enforces **β** to be lower but not 0. By doing so, it will not get rid of irrelevant features but rather minimize their impact on the trained model.
- In statistics the coefficient esimated produced by this method is know as **L2 norm**
- It is good practice to normalize predictors to the same scale before performing Ridge Regression (Because in OLS, the coefficients are scale equivalent)

#### 9.1.1 Implementation
Setting up training/testing model using the Stanford's [prostate cancer data](https://web.stanford.edu/~hastie/ElemStatLearn/datasets/prostate.data)
```python
import pandas as pd
import numpy as np
data=pd.read_csv("/zfs/citi/workshop_data/python_ml/prostate_data.csv")
ind_train = data["train"]=="T"
data = data.drop(["train"],axis=1)
X_train = data.drop(["lpsa"],axis=1)[ind_train]
X_test = data.drop(["lpsa"],axis=1)[~ind_train]
y_train = data["lpsa"][ind_train]
y_test = data["lpsa"][~ind_train]
```

Predict using Ridge Regression method and Cross Validation approach:
```python
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_squared_error as mse

n_lambda = 100
lambdas = np.logspace(-2,6, n_lambda)

MSE_train = []
MSE_test = []
coefs = []

for ld in lambdas:
    ridgecv = RidgeCV(alphas = [ld], normalize = True)
    model_RR = ridgecv.fit(X_train, y_train)
    y_predRR_cv_train = model_RR.predict(X_train)
    y_predRR_cv_test  = model_RR.predict(X_test)    
    MSE_train.append(mse(y_train,y_predRR_cv_train))
    MSE_test.append(mse(y_test,y_predRR_cv_test))    
    coefs.append(model_RR.coef_)

coef_df = pd.DataFrame(coefs)
coef_df.columns = X_train.columns
```

Plotting the Mean Square Error for Training and Testing dataset based on **𝜆** variation
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=False)

ax1 = plt.subplot(221)
ax1.scatter(np.log10(lambdas), MSE_train,color="red")
ax1.set_title("Training Set")
ax2 = plt.subplot(222)
ax2.scatter(np.log10(lambdas), MSE_test,color="red")
ax2.set_title("Testing Set")

ax1.set_xlabel("log($\\lambda$)")
ax2.set_xlabel("log($\\lambda$)")
ax1.set_ylabel('MSE')
ax2.set_ylabel('MSE')

plt.show()
```
![image](https://user-images.githubusercontent.com/43855029/115435103-7bae6780-a1d7-11eb-995b-31a69408469e.png)

Plotting the coefficient of different predictors based on **𝜆**
```python

ax = plt.gca()
for i in range(0,coef_df.columns.size):
    ax.plot(np.log10(lambdas), coef_df.iloc[:,i])
    
ax.legend(coef_df.columns)
#ax.set_xscale('log')
plt.xlabel("log($\\lambda$)")
plt.ylabel('Coefficients')
plt.title('Ridge Regression Coefficients')
plt.axis('tight')
plt.show()
```

![image](https://user-images.githubusercontent.com/43855029/121300671-259b9d80-c8c5-11eb-8d65-8abf3ba5632f.png)

The plot shows different coefficients for all predictors with **𝜆** variation.



- Ridge Regression's pros: the pros of RR method over OLS is rooted in the bias variance trade-off. As when **𝜆** increases, the flexibility of RR fit decreases, hence decrease the variance but increase the bias
- Ridge Regression's cons: **β** never be 0, so all predictors are included in the final model. Therefore, it is not good for best feature selection.

### 9.2 LASSO: Least Absolute Shrinkage & Selection Operator
![image](https://user-images.githubusercontent.com/43855029/121297875-f5ea9680-c8c0-11eb-96c7-b52291a7adbc.png)

- In order to overcome the cons issue in Ridge Regression, the LASSO is introduced with the similar shrinkage parameter, but the different is not in square term of the coefficient but only absolute value
- Similar to Ridge Regression, LASSO also shrink the coefficient, but **force** coefficients to be equal to 0. Making it able to to perform **feature selection**
- In statistics the coefficient esimated produced by this method is know as **L1 norm**

#### 9.2.1 Implementation 
Predict using Lasso method:

```python
from sklearn.linear_model import Lasso

n_lambda = 100
lambdas1 = np.logspace(-6,0, n_lambda)

MSE_train = []
MSE_test = []
coefs = []
for ld in lambdas1:
    lassocv = Lasso(alpha=ld)
    model_LS = lassocv.fit(X_train, y_train)
    y_predLS_cv_train = model_LS.predict(X_train)
    y_predLS_cv_test = model_LS.predict(X_test)
    MSE_train.append(mse(y_train,y_predLS_cv_train))
    MSE_test.append(mse(y_test,y_predLS_cv_test))
    coefs.append(model_LS.coef_)    
```
Plotting the Mean Square Error for Training and Testing dataset based on **𝜆** variation

```python
fig, ax = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=False)


ax1 = plt.subplot(221)
ax1.scatter(np.log10(lambdas1), MSE_train,color="red")
ax1.set_title("Training Set")
ax2 = plt.subplot(222)
ax2.scatter(np.log10(lambdas1), MSE_test,color="red")
ax2.set_title("Testing Set")

ax1.set_xlabel("log($\\lambda$)")
ax2.set_xlabel("log($\\lambda$)")
ax1.set_ylabel('MSE')
ax2.set_ylabel('MSE')

plt.show()
```
![image](https://user-images.githubusercontent.com/43855029/115447429-80c6e300-a1e6-11eb-8808-d44145b77e5f.png)

Plotting the coefficient of different predictors based on **𝜆**

```python
coef_df = pd.DataFrame(coefs)
coef_df.columns = X_train.columns

ax = plt.gca()
for i in range(0,coef_df.columns.size):
    ax.plot(np.log10(lambdas1), coef_df.iloc[:,i])
    
ax.legend(coef_df.columns,bbox_to_anchor = (1.05, 0.6))
#ax.set_xscale('log')
plt.xlabel("log($\\lambda$)")
plt.ylabel('Coefficients')
plt.title('LASSO Coefficients')
plt.axis('tight')
plt.show()
```

![image](https://user-images.githubusercontent.com/43855029/121300854-5da2e080-c8c5-11eb-9eec-00c42b39dcbf.png)

The plot shows different coefficients for all predictors with **𝜆** variation. Depending on **𝜆** values that the **β** varying and it can be 0 at certain point.


### 9.3 Elastic Nets
Elastic Nets Regularization is a method that includes both LASSO and Ridge Regression. Its formulation for the loss function is as following:
![image](https://user-images.githubusercontent.com/43855029/114456877-615b0500-9bab-11eb-9298-028fcffc03ab.png)

- 𝛼=0: pure Ridge Regression
- 𝛼=1: pure LASSO
- 0<𝛼<1: Elastic Nets

#### 9.3.1 Implementation 
```python
from sklearn.linear_model import ElasticNet

MSE_train = []
MSE_test = []
coefs = []
for ld in lambdas1:
    Elastic_cv = ElasticNet(alpha=ld,l1_ratio=0.5)
    model_EN = Elastic_cv.fit(X_train, y_train)
    y_predEN_cv_train = model_EN.predict(X_train)
    y_predEN_cv_test = model_EN.predict(X_test)
    MSE_train.append(mse(y_train,y_predEN_cv_train))
    MSE_test.append(mse(y_test,y_predEN_cv_test))
    coefs.append(model_EN.coef_)
```

- The ElasticNet mixing parameter, with **0 <= l1_ratio <= 1.** 
- For **l1_ratio = 0** the penalty is an L2 penalty (**Ridge Regression**). 
- For **l1_ratio = 1** it is an L1 penalty (**LASSO**).
- For **0 < l1_ratio < 1**, the penalty is a combination of L1 and L2.

