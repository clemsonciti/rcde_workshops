---
title: "Evaluation Metrics with caret"
teaching: 40
exercises: 0
questions:
- "How do we measure the accuracy of ML model"
objectives:
- "Learn different metrics with caret"
keypoints:
- "Caret"
---

# 4 Evaluation of prediction 

Here, we will discuss how we can evaluate our prediction. This process is somewhat different depending on whether we predict numerical outouts (regression) or categorical outputs (classification).

## 4.1 Classification model 

Let's do our first prediction. Let's predict the species of irises from the 4 variables (sepal / petal width and length). First, let's train the model:

```r
train_inputs=training[,1:4]
train_outputs=training[,5]
model <- train(train_inputs, train_outputs, method="lda")
```

Here, we have three classes (three species of irises), and we make the model which predicts the species from the four input variables. We use Fisher's linear discriminant analysis for this purpose. It's a simple classifier based on Ronald Fisher's seminal 1936 paper. Now, let's apply the model to the test set:

```r
predictions <- predict(model,testing)
```

Now, how good was our prediction? A quick way to evaluate the accuracy is to see how many times the predicted species were equal to observed species:

```r
mean(predictions==testing$Species)
```

This is termed *classification accuracy*, and is the most basic metric of our prediction. We can get more detailed metrics by computing confusion matrix (here, we not only see how many observations were correctly predicted, but also look at mistakes: which species are confused with other species).

```r
confusionMatrix (predictions,testing$Species)
```

Really good accuracy! We only made two mistakes: two examples of *versicolor* were mistaken for *virginica*.

We can visualize the confusion matrix:

```r
library(reshape2)
cm <- confusionMatrix (predictions,testing$Species)
cm_df <- melt(cm$table)
ggplot(cm_df, aes(x = Prediction, y = Reference, fill = value)) +
 geom_raster() + scale_fill_distiller(palette = "Spectral") 
``` 


- Evaluation Metric is an essential part in any Machine Learning project.
- It measures how good or bad is your Machine Learning model
- Different Evaluation Metrics are used for Regression model (Continuous output) or Classification model (Categorical output).

## 4.2 Regression model 

Now, let's do rergession -- that is, let's try to predict a numerical (continuous) outcome. We will use the `mtcars` dataset to predict miles-per-gallon from the car's weight, number of cylinders, and other variables. This time, we will do a leave-one-out: for each car, we will exclude it from the training set; use all remaining cars to train the model; and apply the model to predict the MPG of the excluded car. We will use Linear Model (LM) as the method of our prediction.

```r
predictions <- rep (0, dim(mtcars)[1])
for (i in 1:dim(mtcars)[1]) {
  training <- mtcars[-i,]
  testing  <- mtcars[i,] 
  train_inputs=training[,2:11]
  train_outputs=training[,1]
  test_inputs=testing[,2:11]
  model <- train(train_inputs, train_outputs, method="lm")
  predictions[i] <- predict(model,test_inputs)
}
```

Now, once we are done looping, we will get the `predictions` vector which contains the predicted value of MOG for each car. To visually see how it compares to actual MPG values, we can make a scatter plot with `qplot` function:

```r
qplot (predictions, mtcars$mpg)
```

To evaluate our prediction numerically, we can compute Pearson's correlation coefficient:

```r
cor (predictions, mtcars$mpg)
cor.test (predictions, mtcars$mpg)
```

Pretty good! However, when evaluating your prediction, never forget to visually inspect the scatter plot. It will tell you a lot more than you can get from looking at a single number of the correlation coefficient. Below is a [famous example](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) of four scatter plots, each representing correlation coefficient of 0.816: 

<img src="https://thumbnails-visually.netdna-ssl.com/anscombes-quartet_50290d2c47e85.png" width="600" />
