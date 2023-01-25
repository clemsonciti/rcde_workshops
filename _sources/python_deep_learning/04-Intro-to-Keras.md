# Introduction to Keras

## Import Keras

```python
import keras
```

## Layers in Deep Learning

![image](https://user-images.githubusercontent.com/43855029/129512909-a8eaa507-4869-4956-8bf9-ac6a5d6b4cd5.png)

- Input layer
- Dense (fully connected) layers
- Recurrent layer (use for model with time series data)
- Convolution layer (use for model with image data)
- Other layers

For regular Deep Learning model, we use fully connected or Dense layer:

```python
from tensorflow.keras.models import Sequential
from tensroflow.keras.layers import Dense
```

### Sequential

- A **Sequential** model is appropriate for a **plain stack of layers** where each layer has exactly one input tensor and one output tensor.
- More information can be found [here](https://keras.io/guides/sequential_model/)

### Dense:

![image](https://user-images.githubusercontent.com/43855029/129509811-8b951430-dc5f-47d4-a31b-a12b6edade12.png)

**Dense** implements the operation: output = activation(dot(input, kernel) + bias); where:
- activation is the element-wise activation function passed as the activation argument,
- kernel is a weights matrix created by the layer,
- bias is a bias vector created by the layer (only applicable if use_bias is True).
- More information on Dense can be found [here](https://keras.io/api/layers/core_layers/dense)

### Create a Sequential model with N=2 as in image above:

```python
# Create a Sequential model
model = Sequential()
# Create a first hidden layer, the input for the first hidden layer is input layer which has 3 variables:
model.add(Dense(5, activation='relu', input_shape=(3,)))
# Create a second hidden layer without specifying input_shape
model.add(Dense(4, activation='relu'))
# Create an output layer:
model.add(Dense(2,activation='sigmoid'))
```

### How about this model?

![image](https://user-images.githubusercontent.com/43855029/129513301-dfb25a8a-32d8-43a1-a6f4-713aa718c2e0.png)

### Optimal activation function?
#### For hidden layers:

![image](https://user-images.githubusercontent.com/43855029/129512679-34174dd4-8b79-4625-96d9-c85e5ea95c48.png)

#### For output layers:

![image](https://user-images.githubusercontent.com/43855029/129512553-17bf8d4e-5ed4-4180-aaa7-d180c2d093c0.png)

Source on optimal activation function can be found [here](https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/)


