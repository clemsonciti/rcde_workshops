---
title: "Training Machine Learning model using Ensemble approach"
teaching: 20
exercises: 0
questions:
- "How to overcome limitation of single ML model?"
objectives:
- "Learn to use different Ensemble ML algorithm for Machine Learning training"
keypoints:
- "Bagging, Boosting"
---

Ensemble learning is a way to combine multiple ML methods, and to base the final answer on the outputs of these classifiers. A good description of ensemble learning is [here](https://www.pluralsight.com/guides/ensemble-methods:-bagging-versus-boosting).

<img src="https://user-images.githubusercontent.com/43855029/115078334-7b5b5700-9ecd-11eb-93fb-c3f69e740a5c.png" width="400" />
[Source: Patheos.com](https://www.patheos.com/blogs/driventoabstraction/2018/07/blind-men-elephant-folklore-knowledge/)

<!---
Ensemble approaches can reduce variance & Avoid Overfitting by combining results of multiple classifiers on different sub-samples

![image](https://user-images.githubusercontent.com/43855029/114235479-417ad580-994e-11eb-806b-2f73996f864d.png) 

## 7.2 Train model using Ensemble Approach
Ensemble methods use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone.
Unlike a statistical ensemble in statistical mechanics, which is usually infinite, a machine learning ensemble consists of only a concrete finite set of alternative models, but typically allows for much more flexible structure to exist among those alternatives.
Here we will be learning several ensemble models:
- Random Forest
- Bagging
- Boosting with AdaBoost
- Boosting with Gradient Boosting Machine -->

Two examples of ensemble approach: *bagging* and *boosting*.

![image](https://user-images.githubusercontent.com/43855029/115079289-f6713d00-9ece-11eb-90cb-7084e8d7a536.png) 

Bagging creates a series of training sets from the originak training set with the procedure called bootstrapping. The bootstrapped sets are random samples (with replacement) of the observations in the original training set. These sets have the same number of observations as the original training set. Then, each set is processed with a machine learning model. The final outcome is the average output (for regression) or the majority vote (for classification). This combination is normally more robust than a single model.

Some implementations of Bagging in Caret:

- ctreebag: used for Decision Tree
- bagFDA: used for Flexible Discriminant Analysis
- ldaBag: Bagging for Linear Discriminant Analysis
- plsBag: Bagging for Principal Linear Regression

```r
ModFit_bag <- train(as.factor(Species) ~ .,data=training,
                   method="treebag",
                   importance=TRUE)
predict_bag <- predict(ModFit_bag,testing)
confusionMatrix(predict_bag, testing$Species)
plot(varImp(ModFit_bag))
```

In boosting, this process is sequential rather than parallel: output of one model is the input to another one. The inputs are weighted: if an observation is misclassified, it will be weighted more highly for the next classifier.
 
<!--- 

## 7.4 Train model using Boosting
- Boosting is an approach to convert weak predictors to get stronger predictors.
- Boosting follows a sequential order: output of base learner will be input to another
- If a base classifier is misclassifier (red box), its weight is increased and the next base learner will classify more correctly.
- Finally combine the classifier to predict result

![image](https://user-images.githubusercontent.com/43855029/115079476-39331500-9ecf-11eb-9af5-cb3cb2948cf0.png)


### 7.4.1 Adaptive Boosting: Adaboost
- Adaptive: weaker learners are tweaked by misclassify from previous classifier
- AdaBoost is best used to boost the performance of decision trees on binary classification problems.
- Better for classification rather than regression.
- Sensitive to noise

In the following example, we use the package `adabag`, not from `caret`

```r
library(adabag)

ModFit_adaboost <- boosting(Species~.,data=training,mfinal = 10, coeflearn = "Breiman")
importanceplot(ModFit_adaboost)
predict_Ada <- predict(ModFit_adaboost,newdata=testing)
confusionMatrix(testing$Species,as.factor(predict_Ada$class))
```
![image](https://user-images.githubusercontent.com/43855029/114237033-77b95480-9950-11eb-854d-fe4ae34dd2e1.png)

You can see the weight of different predictors from boosting model

### 7.4.2 Gradient Boosting Machines: 
- Extremely popular ML algorithm
- Widely used in Kaggle competition
- Ensemble of shallow and weak successive tree, with each tree learning and improving on the previous

```r
ModFit_GBM <- train(Species~.,data=training,method="gbm",verbose=FALSE)
ModFit_GBM$finalModel
predict_GBM <- predict(ModFit_GBM,newdata=testing)
confusionMatrix(testing$Species,predict_GBM)
```

## 7.5 Compare Bagging and Boosting technique:
![image](https://user-images.githubusercontent.com/43855029/115079914-e443ce80-9ecf-11eb-8b19-622abbfe026c.png)

## 7.6 Conclusions
- Ensemble overcome the limitation of using only single model
- Between bagging and boosting, there is no better approach without trial & error. -->
