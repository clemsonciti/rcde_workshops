# Distributed machine learning with Spark

## 1. Application: Spam Filtering 
```{dropdown}

|    | viagra | learning | the | dating | nigeria | <b>spam?</b> |
| ---| ------ | -------- | --- | ------ | ------- | ------------ |
| X1 | 1      | 0        | 1   | 0      | 0       | y<sub>1</sub> = 1       |
| X2 | 0      | 1        | 1   | 0      | 0       | Y<sub>2</sub> = -1      |
| X3 | 0      | 0        | 0   | 0      | 1       | y<sub>3</sub> = 1       |

- Instance spaces X1, X2, X3 belong to set X (data points)
  - Binary or real-valued feature vector X of word occurrences
  - `d` features (words and other things, d is approximately 100,000)
- Class Y
  - Spam = 1
  - Ham = -1

```


## 2. Linear models for classification
```{dropdown}

:::{image} ../fig/csc467/10-svm/01.png
:class: bg-primary mb-1
:height: 50px
:align: center
:::

- Vector X<sub>j</sub> contains real values
  - The [Euclidean norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm) is `1`. 
  - Each vector has a label y<sub>j</sub>
- The goal is to find a vector W = (w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>d</sub>) with 
w<sub>j</sub> is a real number such that:
  - The labeled points are clearly separated by a line: 

:::{image} ../fig/csc467/10-svm/02.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

- Dot is spam, minus is ham!

:::{image} ../fig/csc467/10-svm/03.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

```

## 3. Linear classifiers
```{dropdown}
- Each feature `i` as a weight w<sub>i</sub>
- Prediction is based on the weighted sum:

:::{image} ../fig/csc467/10-svm/04.png
:class: bg-primary mb-1
:height: 50px
:align: center
:::

- If f(x) is:
  - Positive: predict +1
  - Negative: predict -1

:::{image} ../fig/csc467/10-svm/05.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

```

## 4. Support Vector Machine
```{dropdown}
- Originally developed by Vapnik and collaborators as a linear classifier. 
- Could be modified to support non-linear classification by mapping into high-dimensional spaces. 
- Problem statement:
  - We want to separate `+` from `-` using a line. 
  - Training examples: 

:::{image} ../fig/csc467/10-svm/06.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

  - Each example `i`:

:::{image} ../fig/csc467/10-svm/07.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

:::{image} ../fig/csc467/10-svm/08.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

  - Inner product:

:::{image} ../fig/csc467/10-svm/09.png
:class: bg-primary mb-1
:height: 100px
:align: center
:::

- Which is the best linear separate defined by w?

:::{image} ../fig/csc467/10-svm/10.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

```

## 5. Support Vector Machine: largest margin
```{dropdown}
- Distance from the separating line corresponds to the **confidence** of the prediction. 
- For example, we are more sure about the class of `A` and `B` than of `C`. 

:::{image} ../fig/csc467/10-svm/11.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- Margin definition:

:::{image} ../fig/csc467/10-svm/12.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

:::{image} ../fig/csc467/10-svm/13.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Maximizing the margin while identifying `w` is good according to intuition, theory, and practice. 

:::{image} ../fig/csc467/10-svm/14.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- A math question: how do you narrate this equation?

:::{image} ../fig/csc467/10-svm/15.png
:class: bg-primary mb-1
:height: 100px
:align: center
:::

```

## 6. Support Vector Machine: what is the margin?
```{dropdown}
- Slide from the book

:::{image} ../fig/csc467/10-svm/16.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- Notation:
  - `Gamma` is the distance from point A to the linear separator L: `d(A,L) = |AH|`
  - If we select a random point M on line L, then d(A,L) is the projection of AM onto vector `w`. 
  - [Project](https://mathworld.wolfram.com/Projection.html)
  - If we assume the normalized Euclidean value of `w`, `|w|`, is equal to one, that bring us to 
  the result in the slide. 
- In other words, maximizing the margin is directly related to how `w` is chosen.
- For the *i<sup>th</sup>* data point:

:::{image} ../fig/csc467/10-svm/17.png
:class: bg-primary mb-1
:height: 50px
:align: center
:::

```

## 7. Some more math ...
```{dropdown}

:::{image} ../fig/csc467/10-svm/18.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- After some more mathematical manipulations:

:::{image} ../fig/csc467/10-svm/19.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

- Everything comes back to an optimization problem on `w`:

:::{image} ../fig/csc467/10-svm/20.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

:::{image} ../fig/csc467/10-svm/21.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::


```

## 8. SVM: Non-linearly separable data
```{dropdown}

:::{image} ../fig/csc467/10-svm/22.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- For each data point:
  - If margin greater than 1, don't care. 
  - If margin is less than 1, pay linear penalty. 
- Introducing slack variables:

:::{image} ../fig/csc467/10-svm/23.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

:::{image} ../fig/csc467/10-svm/24.png
:class: bg-primary mb-1
:height: 30px
:align: center
:::

```

## 9. Hands-on: SVM
```{dropdown}
- Download the set of inaugural speeches from https://www.cs.wcupa.edu/lngo/data/bank.csv
- Activate the `pyspark` conda environment, install `pandas`, then launch Jupyter notebook

~~~
$ conda activate pyspark
$ conda install -y pandas
$ jupyter notebook
~~~ 


- Create a new notebook using the `pyspark` kernel, then change the notebook's 
name to `spark-7`. 
- Copy the code from `spark-6` to setup and launch a Spark application. 
- Documentation:
  - [SVM example](https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html?highlight=svm#pyspark.mllib.classification.SVMModel)
  - [Data format](https://spark.apache.org/docs/2.2.0/mllib-data-types.html#labeled-point)
  - [Split data frame for training and testing](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=randomsplit#pyspark.sql.DataFrame.randomSplit)

- Question: Can you predict whether a client will subscribe to a term deposit (feature `deposit`)?
- Problems:
  - What data should the bank data be converted to?
  - How to handle categorical data?

```
