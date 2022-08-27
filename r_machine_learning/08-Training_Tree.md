---
title: "Training Machine Learning model using Tree-based model"
teaching: 20
exercises: 0
questions:
- "How to train a Machine Learning model using Tree-based model"
objectives:
- "Learn to use different Tree-based algorithm for Machine Learning training"
keypoints:
- "Decision Tree, Random Forest"
---

## Training the model using Decision Trees
-   Decision trees can take inputs where some variables are numerical and some are categorical
-   Very handy when dealing with demographic data (gender, age, education level)
-   Works for continuous or categorical outputs
-   Very flexible, can capture complex relationships between inputs and outputs
-   Easy to interpret
-   Training could be slow
-   Prone to overfitting
![image](https://user-images.githubusercontent.com/43855029/114233972-198a7280-994c-11eb-9f4f-da4ed958961e.png)

### Spliting algorithm
- Gini Impurity: (Categorical)
- Chi-Square index (Categorical)
- Cross-Entropy & Information gain (Categorical)
- Reduction Variance (Continuous)

<!---
### Pros & Cons
![image](https://user-images.githubusercontent.com/43855029/114234120-548ca600-994c-11eb-889e-e8ec6d313e52.png) -->

### Implementation
Here we will use `iris` data
```r
library(caret)
data(iris)
set.seed(123)
indT <- createDataPartition(y=iris$Species,p=0.6,list=FALSE)
training <- iris[indT,]
testing  <- iris[-indT,]
```
Next we will train using `method="rpart"` with `gini` splitting algorithm:
```r
ModFit_rpart <- train(Species~.,data=training,method="rpart",
                      parms = list(split = "gini"))
# gini can be replaced by chisquare, entropy, information

#fancier plot
install.packages("rattle")
library(rattle)
fancyRpartPlot(ModFit_rpart$finalModel)
```
![image](https://user-images.githubusercontent.com/43855029/114234603-ff04c900-994c-11eb-9999-0c5d5f85b76e.png)
Apply decision tree model to predict output of testing data
```r
predict_rpart <- predict(ModFit_rpart,testing)
confusionMatrix(predict_rpart, testing$Species)

testing$PredRight <- predict_rpart==testing$Species
ggplot(testing,aes(x=Petal.Width,y=Petal.Length))+
  geom_point(aes(col=PredRight))
```
![image](https://user-images.githubusercontent.com/43855029/114234661-117f0280-994d-11eb-950f-d07ed91cda09.png)

## Train model using Random Forest
![image](https://user-images.githubusercontent.com/43855029/115076000-f3278280-9ec9-11eb-89b4-b07f3713b105.png)

- A single decision tree is prone to overfitting. A solution is to grow a number of decision trees, i.e. a forest.
- We use portions of the data to grow a tree for each portion (bootstrapping)
- All trees are used to predict the output, and the final prediction is the majority vote (in classification) or the average (in regression)
- Very versatile, good generalization (especially for classification), handles missing data well
- Quite slow and hard to interpret (prone to be used as a "black box")

<!---
### Detail explaination
- If there are M input variables, a number m<M is specified such that at each node, m variables are selected at random out of the M. The best split on these m is used to split the node. The value of m is held constant while we grow the forest.
- Each tree is grown to the largest extent possible and  there is no pruning.
- Predict new data by aggregating the predictions of the ntree trees (i.e., majority votes for classification, average for regression).
![image](https://user-images.githubusercontent.com/43855029/114235192-d16c4f80-994d-11eb-9732-571463c2f3f5.png)

### Pros & Cons of Random Forest
![image](https://user-images.githubusercontent.com/43855029/114235213-daf5b780-994d-11eb-83f8-ac7520749dbe.png)
-->
### Implementation of Random Forest

```r
ModFit_rf <- train(Species~.,data=training,method="rf",prox=TRUE)

predict_rf <- predict(ModFit_rf,testing)
confusionMatrix(predict_rf, testing$Species)

testing$PredRight <- predict_rf==testing$Species
ggplot(testing,aes(x=Petal.Width,y=Petal.Length))+
  geom_point(aes(col=PredRight))
```
![image](https://user-images.githubusercontent.com/43855029/114235296-fb257680-994d-11eb-93ff-54702cbf87b8.png)

We can see that Random Forest result has better prediction than the Decision Tree.
