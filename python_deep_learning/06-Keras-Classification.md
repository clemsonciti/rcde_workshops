# Training Deep Learning Classification model with Keras

## Using Keras to solve a Classification Model

### Prepare the data
Here we use iris data from ANN and Classification episode in our previous Machine Learning class with sklearn:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data
y = iris.target
```

### Apply One Hot Encoding to categorize the output:
- One Hot Encoding allows to represent the categorical data in a probabilistic way that is understandable by the machine.
- For example **cat, dog, deer** can be converted to **0, 1, 2** or **[1 0 0,0 1 0,0 0 1]**

```python
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
Y = enc.fit_transform(y[:, np.newaxis]).toarray()
```

### Split data to training/testing:

```python
X_train, X_test, y_train, y_test = train_test_split(X,Y,train_size=0.6,random_state=123)
```

### Scale the input data:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Let's use Keras's Sequential model with Dense layers

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```

### Create a Sequential model with 3 layers:

```python
# Create a Sequential model
model = Sequential()
# Create a first hidden layer, the input for the first hidden layer is input layer which has 3 variables:
model.add(Dense(50, activation='relu', input_shape=(4,)))
# Create a second hidden layer
model.add(Dense(40, activation='relu'))
# Create an output layer with only 3 variables:
model.add(Dense(3,activation='softmax'))
```

### Compile model

```python
model.compile(optimizer='adam', loss='categorical_crossentropy',metrics='accuracy')
```

### Fit model

```python
model.fit(X_train_scaled, y_train, epochs=100, verbose=1,
               validation_data=(X_test_scaled,y_test))
```
 
### Evaluate model
Evaluate the testing set using given loss function
```python
results = model.evaluate(X_test_scaled, y_test, verbose=1)
print("test loss, test acc:", results)
```

### Predict output
```python
predictions = model.predict(X_test_scaled)
```

### Inverse transform the One Hot Encoding
```python
Y_pred = enc.inverse_transform(predictions)
Y_test = enc.inverse_transform(y_test)
```

### Evaluate using accuracy score:

```python
import sklearn
sklearn.metrics.accuracy_score(Y_pred,Y_test)
```

