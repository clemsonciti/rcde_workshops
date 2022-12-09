---
title: "Introduction to Machine Learning"
teaching: 10
exercises: 0
questions:
- "What is Machine Learning"
objectives:
- "Learn the basics of Machine Learning"
keypoints:
- "Basic Machine Learning"
---

Very broadly speaking, machine learning is a discpline where an algorithm learns how to make predictions from data; ideally, the more data are available, the better the predictions get.

Two types of machine learning:
- Supervised machine learning: the algirithm learns the assiciations between "input" and "output" data (for example, between demographcs and political preferences). It has two stages: 
1. *Training* the algorithm: we provide the algorithm with a set of inputs and outputs, and let it figure out the associations between them;
2. *Testing* the algotrithm: we obtain a set of inputs that were not used in the training, and use the algorithm to estimate the outputs. 
- Unsupervised machine learning: here, we don't look at the outputs, and try to discover patterns in the inputs (for example, clusters of data).

The output variables can be numerical or categorical. An example of a numerical output is predicting how long it takes a person to recover from a trauma, based on the severity of the trauma, person's age, gender, etc. If we try to predict whether the person will recover or not, the output is categorical (with two categories: recoverers and non-recoverers). A model that predicts a numerical outcome is a *regression* model; a model which predicts a categorical outcome is a *classification* model.  

Getting a good sample of data for training is critical. If the data are not representative of the general population, the algorithm will perform badly in the testing phase. However, in real world, any finite sample of data cannot include all the information about the general population, and therefore any machine learning algorithm is *biased* by the training sample.

Generally speaking, a complex algorithm can learn more complex associations, but sometimes too much complexity is a bad thing. If our algorithm allows for too much complexity, it will try to model the random associations between inputs and outputs that are specific to the training set. Because these associations don't generalize to the test set, the algorithm will make errors in the testing phase. This is called *overfitting*. 

It is common to mix supervised and unsupervised methods within the same prediction process. For example, unsupervised methods can provide a simpler representation of the data and help against overfitting.


{% include links.md %}

