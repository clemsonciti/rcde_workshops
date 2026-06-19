# Recap on ANN

## Recap of Artificial Neural Networks (ANN)
Previous ANN in Machine Learning lecture can be found here: https://vuminhtue.github.io/Machine-Learning-Python/10-Neural-Network/index.html

- A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.

- A neuron is the basic unit in a nervous system and is the most important component of the brain.

- In each neuron, there is a cell body (node), dendrite (input signal) and axon (output signal to other neuron).

- If a neuron received enough signal, it is then activated to decide whether or not it should transmit the signal to other neurons or not.

![image](https://user-images.githubusercontent.com/43855029/114472746-da188c00-9bc0-11eb-913c-9dcd14f872ac.png)

Biological Neural Networks

![image](https://user-images.githubusercontent.com/43855029/114472756-dd137c80-9bc0-11eb-863d-7c4d054efa89.png)

Machine Learning Neural Networks (normally consists of 1 hidden layer: Shallow Network)

![image](https://user-images.githubusercontent.com/43855029/119180080-cf61da00-ba3d-11eb-9ad4-26c159a470be.png)

Deep Neural Networks (multiple hidden layers)

### Forward Propagation (Feed-forward)
- The process in which data passes through multiple layers of neurons from input layer to output layers.
- The image below demonstrates the data from an input layer passing through 1 neuron by connection through the dendrite with specific weights for each connection.
- The bias is also added to adjust the output from the neuron
- Output of the neuron is converted using activation function in order to map with the output layer.
- Since there is only direction for the data to go, this method is called forward propagation.
![image](https://user-images.githubusercontent.com/43855029/114472776-e997d500-9bc0-11eb-9f70-450389c912df.png)

### Backpropagation
- Forward Propagation is fast but it has limitations: Weights and biases cannot be changed.
- In order to overcome this limitation, Backpropagation calculates the error between output and observed data, propagates the error back into the network, and updates the weights and biases
- The Backpropagation process is repeated until number of iteration/epochs is reached or the error between output and observed is within the acceptable threshold.

![image](https://user-images.githubusercontent.com/43855029/119187908-f1605a00-ba47-11eb-8c78-9e459eaadea1.png)


### Activation Functions
Typical activation functions in Neural Networks:
- Step Function (Binary Function)
- Linear Function
- Sigmoid Function* & Softmax*
- Hyperbolic Tangent Function (Tanh)*
- Rectified Linear Unit Function (ReLU)*

"*" Most popular functions

(1) Sigmoid Function

![image](https://user-images.githubusercontent.com/43855029/119183889-af80e500-ba42-11eb-923f-8314b3f88734.png)

- One of the widely used activation function in the hidden layer of NN
- However, it is flat with abs(z)>3, therefore it might lead to "vanishing gradient" in Backpropagation approach, that slowdown the optimization of NN in Deep Neural Network.
- Sigmoid function converts the output to range (0, 1) so it is not symmetric around the origin. All values are positive.
- Application in binary classification problems.

(2) Softmax
- The softmax is a more generalized form of the sigmoid.
- It is used in multi-class classification problems.
- Similar to sigmoid, it produces values in the range of 0–1. It is used as the final layer in classification models.
- Application in classification with more categories

(3) Hyperbolic Tangent Function (Tanh)

![image](https://user-images.githubusercontent.com/43855029/119186714-777ba100-ba46-11eb-8e8f-f82ce0954a91.png)

- Tanh is quite similar to Sigmoid but it is symmetric around the origin
- However, it also flat with abs(z)>3 and also lead to "vanishing gradient" problems in Deep Neural Networks

(3) ReLU Function

![image](https://user-images.githubusercontent.com/43855029/119186990-b1e53e00-ba46-11eb-8f1c-637b546e62e8.png)

- The most widely used Activation Function in Deep Neural Networks
- It is nonlinear
- It does not activate all neurons at the same time: If the input is negative, the neuron is not activated
- Therefore, it overcomes the "vanishing gradient" problem

### Gradient problem
[Gradient problem](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11)
When training a deep neural network with gradient based learning and backpropagation, we find the partial derivatives by traversing the network from the the final layer to the initial layer. Using the chain rule, layers that are deeper into the network go through continuous matrix multiplications in order to compute their derivatives.

#### Vanishing gradient
- In a network of **n** hidden layers, **n** derivatives will be multiplied together. If the derivatives are small then the gradient will decrease exponentially as we propagate through the model until it eventually vanishes
- The accumulation of small gradients results in a model that is incapable of learning meaningful insights since the weights and biases of the initial layers, which tend to learn the core features from the input data (X), will not be updated effectively. In the worst case scenario the gradient will be 0 which in turn will stop the network and stop further training.

#### Exploding gradient
- If the derivatives are large, then the gradient will increase exponentially as we propagate down the model until they eventually explode, and this is what we call the problem of exploding gradients.
- The accumulation of large derivatives results in the model being very unstable and incapable of effective learning. The large changes in the model weights creates a very unstable network. At extreme values the weights become so large that it causes overflow, resulting in NaN weight values which can no longer be updated.

#### Solution:
[Solution](https://www.analyticsvidhya.com/blog/2021/06/the-challenge-of-vanishing-exploding-gradients-in-deep-neural-networks/)

- Reduce the amount of layer
- Proper weights for initilization

```python
keras.layer.Dense(25, activation = "relu", kernel_initializer="he_normal")
```

- Using Non-saturating Activation Functions like ReLU
- Batch Normalization

```python
keras.layers.BatchNormalization(),
```
- Gradient Clipping

```python
optimizer = keras.optimizers.SGD(clipvalue = 1.0)
```

