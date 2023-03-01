# Evaluation Metrics with Scikit-Learn

- Evaluation Metric is an essential part in any Machine Learning project.
- It measures how good or bad is your Machine Learning model
- Different Evaluation Metrics are used for Regression model (Continuous output) or Classification model (Categorical output).

## 4.1 Regression model Evaluation Metrics

### 4.1.1 Correlation Coefficient (R) or Coefficient of Determination (R2):

![image](https://user-images.githubusercontent.com/43855029/120700259-72274900-c47f-11eb-8959-a4bbe4eafccc.png)

```python
from sklearn import metrics
metrics.r2_score(y_test,y_pred)
```

### 4.1.2 Root Mean Square Error (RMSE) or Mean Square Error (MSE)

![image](https://user-images.githubusercontent.com/43855029/120700533-c5010080-c47f-11eb-8050-b1cd8c63746e.png)

```python
from sklearn import metrics
print(metrics.mean_squared_error(y_test,y_pred,squared=False)) # RMSE
print(metrics.mean_squared_error(y_test,y_pred,squared=True)) # MSE
```

## 4.2. Classification model Evaluation Metrics

### 4.2.1 Confusion Matrix
- A confusion matrix is a technique for summarizing the performance of a classification algorithm.
- You can learn more about Confusion Matrix [here](https://www.analyticsvidhya.com/blog/2020/04/confusion-matrix-machine-learning/)

For binary output (classification problem with only 2 output type, also most popular):

![image](https://user-images.githubusercontent.com/43855029/120687356-efe35880-c46f-11eb-950f-5feef237a4c1.png)

### 4.2.2 Accuracy

The most common metric for classification is accuracy, which is the fraction of samples predicted correctly as shown below:

![image](https://user-images.githubusercontent.com/43855029/120700619-dea24800-c47f-11eb-81c4-df090cad93da.png)

```python
from sklearn import metrics
metrics.accuracy_score(y_test,y_pred)
```

### 4.2.3 Precision 

Precision is the fraction of predicted positives events that are actually positive as shown below:

![image](https://user-images.githubusercontent.com/43855029/120700808-1c9f6c00-c480-11eb-9ec8-597d02a76a94.png)

### 4.2.4 Recall

Recall (also known as sensitivity) is the fraction of positives events that you predicted correctly as shown below:

![image](https://user-images.githubusercontent.com/43855029/120700754-07c2d880-c480-11eb-81e1-7c7926452346.png)


### 4.2.5 F1 score

The f1 score is the harmonic mean of recall and precision, with a higher score as a better model. The f1 score is calculated using the following formula:

![image](https://user-images.githubusercontent.com/43855029/120701061-6ee08d00-c480-11eb-9ab1-71d905e6a491.png)

More information on Precision, Recall and F1 score can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)

```python
metrics.precision_recall_fscore_support(y_test,y_pred,average='binary')
```

### 4.2.6 AUC-ROC curve
- ROC: Receiver Operating Characteristics:  probability curve
- AUC: Area Under The Curve: represents the degree or measure of separability.
 
![image](https://user-images.githubusercontent.com/43855029/120698991-ccbfa580-c47d-11eb-9f11-6e2acb00d46d.png)

  - AUC = 1:   perfect prediction
  - AUC = 0.8: model has 80% chance to predict the right class
  - AUC = 0.5: worst case, model has **NO** accuracy in prediction (random)
  - AUC = 0:   the model is actually reciprocating the classes
  
![image](https://user-images.githubusercontent.com/43855029/120699552-84ed4e00-c47e-11eb-8089-54158439ad6f.png)

ROC Interpretation

![image](https://user-images.githubusercontent.com/43855029/133898061-2c7f5da6-c41b-41af-8a81-b65fef3c3184.png)

Code to calculate FPR, TPR:

```python
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test,y_pred)
```

Code to calculate AUC score:

```python
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(y_test,y_pred)
```

We will go into detail how to plot AUC-ROC curve in the next chapter with a classification problem
