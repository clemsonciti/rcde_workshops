# Training Deep Learning Regression model with Keras


## Using Keras to solve a Regression Model

### Prepare the data
Here we use [Pima Indian Diabetes database](https://www.kaggle.com/uciml/pima-indians-diabetes-database) data:

- We need to omit the header line of the data. 

```python
import numpy as np
numpy.random.seed(42)
np_data = np.loadtxt("/zfs/citi/workshop_data/python_ml/diabetes.csv", delimiter=",", skiprows=1)
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
```


### Let's use Keras's Sequential model with Dense layers

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```

### Create a Sequential model with 3 layers:

```python
# Create a Sequential model
model = Sequential()
# Create a first hidden layer, the input for the first hidden layer is input layer which has 8 variables:
model.add(Dense(12, input_dim = 8, activation='relu'))
# Create a second hidden layer
model.add(Dense(8, activation='relu'))
# Create a third hidden layer
model.add(Dense(1, activation='sigmoid'))
```

### Compile model

```python
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

Here, **adam** optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments.

According to Kingma et al., 2014, the method is "computationally efficient, has little memory requirement, invariant to diagonal rescaling of gradients, and is well suited for problems that are large in terms of data/parameters".

More information on **adam** optimizer is [here](https://keras.io/api/optimizers/adam/)

In addition to **adam**, there are many other optimizer:
- [SGD](https://keras.io/api/optimizers/sgd)
- [RMSprop](https://keras.io/api/optimizers/rmsprop)
- [Adadelta](https://keras.io/api/optimizers/adadelta)
- [Adagrad](https://keras.io/api/optimizers/adagrad)
- [Adamax](https://keras.io/api/optimizers/adamax)
- [Nadam](https://keras.io/api/optimizers/nadam)
- [Ftrl](https://keras.io/api/optimizers/ftrl)

There are also many other **loss** function. 

The purpose of **loss** functions is to compute the quantity that a model should seek to minimize during training. Detail can be found [here](https://keras.io/api/losses/)

### Fit model

```python
model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10)
```

Here: 
- epochs: the number of iteration 
- verbose: 'auto', 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 
2 = one line per epoch. 'auto' defaults to 1 for most cases, but 2 when used with 
ParameterServerStrategy. Note that the progress bar is not particularly 
useful when logged to a file, so verbose=2 is recommended when not running 
interactively (eg, in a production environment).
- batch_size: Number of samples per batch of computation. If unspecified, batch_size will default to 32.

You can also create custom training/testing dataset: 

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=123)
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=150, batch_size=10)
```
 

### Save & load keras model
```python
from keras.models import load_model

model.save('my_model.keras')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.keras')
```

### Cross validation using K-Fold

```python
from sklearn.model_selection import StratifiedKFold

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=123)
cvscores = []
for train, test in kfold.split(X, Y):
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X[train], Y[train], epochs=150, batch_size=10, verbose=0)
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))

```