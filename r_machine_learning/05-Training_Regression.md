---
title: "Training Machine Learning model using Regression Method"
teaching: 20
exercises: 0
questions:
- "How to train a Machine Learning model using Regression method"
objectives:
- "Learn to use different Regression algorithm for Machine Learning training"
keypoints:
- "Regression training"
---
# 5 More examples of prediction

CARET supports a huge number of prediction methods; see the list [here](https://rdrr.io/cran/caret/man/models.html). Let's do a few examples.

## 5.1 For Continuous output
### 5.1.1 Linear regression with one predictor
Pre-process the data and create a partition
```r
library(caret)
data(airquality)

set.seed(123)
#Impute missing value using Bagging approach
PreImputeBag <- preProcess(airquality,method="bagImpute")
airquality_imp <- predict(PreImputeBag,airquality)

indT <- createDataPartition(y=airquality_imp$Ozone,p=0.6,list=FALSE)
training <- airquality_imp[indT,]
testing  <- airquality_imp[-indT,]
```
Now, let's build a model using a single predictor. Let's predict `Ozone` from one variable, temperature (`Temp`), using a linear model (`method=lm`):
```r
ModFit <- train(Ozone~Temp,data=training,
                preProcess=c("center","scale"),
                method="lm")
summary(ModFit$finalModel)
```
Apply trained model to testing data set and evaluate output:
```r
prediction <- predict(ModFit,testing)
cor.test(prediction,testing$Ozone)
```

### 5.1.2 Linear regression with multiple predictors (Multi-Linear Regression)

Now, let's predict `Ozone` from three predictors: solar radiation, wind, and temperature. 
```r
modFit2 <- train(Ozone~Solar.R+Wind+Temp,data=training,
                 preProcess=c("center","scale"),
                 method="lm")
summary(modFit2$finalModel)

prediction2 <- predict(modFit2,testing)
cor.test(prediction2,testing$Ozone)
```
We see that our correlation has improved when we used more predictors. 


<!---
### 5.1.3 Train model using Stepwise Linear Regression
It’s a step by step Regression to determine which covariates set best match with the dependent variable. Using AIC as criteria:

```r
modFit_SLR <- train(Ozone~Solar.R+Wind+Temp,data=training,method="lmStepAIC")
summary(modFit_SLR$finalModel)
prediction_SLR <- predict(modFit_SLR,testing)
cor.test(prediction_SLR,testing$Ozone)
```

```r
> postResample(prediction_SLR,testing$Ozone)
      RMSE   Rsquared        MAE 
25.0004212  0.5239849 17.0977421 
```
-->

### 5.1.3 Train model using Polynomial Regression

![image](https://user-images.githubusercontent.com/43855029/122609104-6c1e9400-d04b-11eb-984c-ed20f0926451.png)

In this study, let's use polynomial regression with degrees of freedom=3:

```r
modFit_poly <- train(Ozone~poly(Solar.R,3)+poly(Wind,3)+poly(Temp,3),data=training,
                     preProcess=c("center","scale"),
                     method="lm")
summary(modFit_poly$finalModel)
prediction_poly <- predict(modFit_poly,testing)
cor.test(prediction_poly,testing$Ozone)
```

### 5.1.4 Train model using Principal Component Regression
Principal Component Regression is a combination of linear regression and principal component analysis; it is particularly useful when the predictors are highly correlated. 

```r
install.packages("pls")
library(pls)
modFit_PCR <- train(Ozone~Solar.R+Wind+Temp,data=training,method="pcr")
summary(modFit_PCR$finalModel)
prediction_PCR <- predict(modFit_PCR,testing)
cor.test(prediction_PCR,testing$Ozone)
```

## 5.2 For categorical output
### 5.2.1 Train model using Logistic Regression
- Logistic regression is a common method for binary classification problems (when outcomes fall into two categories).
- Typical binary classification: True/False, Yes/No, Pass/Fail
- Unlike linear regression, the prediction for the output is transformed using a non-linear function called the logistic function.
- The standard logistic function has formulation:
 
![image](https://user-images.githubusercontent.com/43855029/114233181-f7dcbb80-994a-11eb-9c89-58d7802d6b49.png)

<!--- ![image](https://user-images.githubusercontent.com/43855029/114233189-fb704280-994a-11eb-9019-8355f5337b37.png) -->
<img src="../fig/logreg.png" width=600 />

In this example, we use `spam` data set from package `kernlab`.
This is a data set collected at Hewlett-Packard Labs, that classifies **4601** e-mails as spam or non-spam. In addition to this class label there are **57** variables indicating the frequency of certain words and characters in the e-mail.
More information on this data set can be found [here](https://rdrr.io/cran/kernlab/man/spam.html)

Train the model:
```r
install.packages("kernlab")
library(kernlab)
data(spam)
names(spam)

indTrain <- createDataPartition(y=spam$type,p=0.6,list = FALSE)
training <- spam[indTrain,]
testing  <- spam[-indTrain,]

ModFit_glm <- train(type~.,data=training,method="glm")
summary(ModFit_glm$finalModel)
```
Predict based on testing data and evaluate model output:
```r
predictions <- predict(ModFit_glm,testing)
confusionMatrix(predictions, testing$type)
```

Plotting ROC and computing AUC:

```r
#Need to install package ROCR
install.packages("ROCR")
library(ROCR)
pred_prob <- predict(ModFit_glm,testing, type = "prob")
head(pred_prob)
data_roc <- data.frame(pred_prob = pred_prob[,'spam'],
                           actual_label = ifelse(testing$type == 'spam', 1, 0))

roc <- prediction(predictions = data_roc$pred_prob,
                      labels = data_roc$actual_label)

plot(performance(roc, "tpr", "fpr"))
abline(0, 1, lty = 2)
auc <- performance(roc, measure = "auc")
auc@y.values

```

![image](https://user-images.githubusercontent.com/43855029/122612391-07fece80-d051-11eb-9ab0-2f130ea10c59.png)
