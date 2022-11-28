# Neural Network

## 11. Neural Network

- Neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates. 

- Neuron is a basic unit in a nervous system and is the most important component of the brain.
- In each Neuron, there is a cell body (node), dendrite (input signal) and axon (output signal to other neuron).
- If a Neuron received enough signal, it is then activated to decide whether or not it should transmitt the signal to other neuron or not.

![image](https://user-images.githubusercontent.com/43855029/114472746-da188c00-9bc0-11eb-913c-9dcd14f872ac.png)
![image](https://user-images.githubusercontent.com/43855029/114472756-dd137c80-9bc0-11eb-863d-7c4d054efa89.png)

- Formulation of Neural Network

![image](https://user-images.githubusercontent.com/43855029/114472776-e997d500-9bc0-11eb-9f70-450389c912df.png)
```
Here, x1,x2....xn are input variables. w1,w2....wn are weights of respective inputs.
b is the bias, which is summed with the weighted inputs to form the net inputs. 
Bias and weights are both adjustable parameters of the neuron.
Parameters are adjusted using some learning rules. 
The output of a neuron can range from -inf to +inf.
The neuron doesn’t know the boundary. So we need a mapping mechanism between the input and output of the neuron. 
This mechanism of mapping inputs to output is known as Activation Function.
```
- Activation functions:
![image](https://user-images.githubusercontent.com/43855029/114575672-6752f380-9c48-11eb-8d53-c78d052cdf17.png)

```python
import matplotlib.pyplot as plt
import numpy as np

xrange = np.linspace(-2, 2, 200)

plt.figure(figsize=(7,6))

plt.plot(xrange, np.maximum(xrange, 0), label = 'ReLU')
plt.plot(xrange, np.tanh(xrange), label = 'Hyperbolic Tangent')
plt.plot(xrange, 1 / (1 + np.exp(-xrange)), label = 'Sigmoid/Logistic')
plt.plot(xrange, xrange, label = 'Linear')
plt.plot(xrange, np.heaviside(xrange, 0.5), label = 'Step')
plt.legend()
plt.title('Neural network activation functions')
plt.xlabel('Input value (x)')
plt.ylabel('Activation function output')

plt.show()
```
![image](https://user-images.githubusercontent.com/43855029/115588329-9e568400-a29c-11eb-92b3-abe0c2db16c5.png)

- Neural Network formulation: Multi-Layer Perceptron (MLP)
**Multi-layer Perceptron (MLP)** is a supervised learning algorithm.
Given a set of features `X = x1, x2, ... xm`, and target `y`, MLP can learn a non-linear function approximator for either classification or regression.

Between the input and the output layer, there can be one or more non-linear layers, called hidden layers. Figure below shows a one hidden layer MLP with scalar output.

![image](https://user-images.githubusercontent.com/43855029/114472972-51e6b680-9bc1-11eb-9e78-90ec739844ee.png)

![image](https://user-images.githubusercontent.com/43855029/114575549-48546180-9c48-11eb-8c9c-c5eac3180df1.png)

**The advantages of Multi-layer Perceptron:**
- Capability to learn non-linear models.
- Capability to learn models in real-time (on-line learning) using partial_fit.

**The disadvantages of Multi-layer Perceptron:**
- MLP with hidden layers have a non-convex loss function where there exists more than one local minimum. Therefore different random weight initializations can lead to different validation accuracy.
- MLP requires tuning a number of hyperparameters such as the number of hidden neurons, layers, and iterations.
- MLP is sensitive to feature scaling.

### 11.1. Type of Neural Network Multi-Layer Perceptron in sklearn
There are 2 main types of MLP in sklearn, depending on the model output:
- MLPClassifier: for Classification problem
- MLPRegressor: for Regression problem 

### 11.2. Implementation with Classification problem
Here we use **iris** data for Classification problem
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import pandas as pd
iris = load_iris()
X = iris.data
y = pd.DataFrame(iris.target)
y['Species']=pd.Categorical.from_codes(iris.target, iris.target_names)
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.6,random_state=123)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

The Class **MLPClassifier** implements a multi-layer perceptron (MLP) algorithm that trains using Backpropagation.
There are lots of parameters in MLPClassifier:
- **hidden_layer_sizes** which is the number of hidden layers and neurons for each layer. Default=`(100,)`
for example `hidden_layer_sizes=(100,)` means there is 1 hidden layers used, with 100 neurons.
for example `hidden_layer_sizes=(50,20)` means there are 2 hidden layers used, the first layer has 50 neuron and the second has 20 neurons.
- **solver** `lbfgs, sgd, adam`. Default=`adam`
- **activation** `identity, logistic, tanh, relu`. Default='relu`

More information can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)

```python
from sklearn.neural_network import MLPClassifier
model_NN = MLPClassifier(hidden_layer_sizes = (50,20),solver='lbfgs',activation='relu',random_state=123).fit(X_train_scaled, y_train['Species'])
model_NN.score(X_test_scaled,y_test['Species'])
```


### 11.3. Implementation with Regression problem
- Class **MLPRegressor** implements a multi-layer perceptron (MLP) that trains using backpropagation with no activation function in the output layer, which can also be seen as using the identity function as activation function. 
- Therefore, it uses the square error as the loss function, and the output is a set of continuous values.

Here we use **airquality** data from Regression espisode:
```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split

data_df = pd.DataFrame(pd.read_csv('/zfs/citi/workshop_data/python_ml/r_airquality.csv'))

imputer = KNNImputer(n_neighbors=2, weights="uniform")
data_knnimpute = pd.DataFrame(imputer.fit_transform(data_df))
data_knnimpute.columns = data_df.columns

X_train, X_test, y_train, y_test = train_test_split(data_knnimpute[['Temp','Wind','Solar.R']],
                                                    data_knnimpute['Ozone'],
                                                    train_size=0.6,random_state=123)
```                                                    
Fit **MLPRegressor** model
```python
from sklearn.neural_network import MLPRegressor
model_NN = MLPRegressor(hidden_layer_sizes = (50,20),solver='lbfgs',activation='relu',max_iter=1000).fit(X_train,y_train)
model_NN.score(X_test,y_test)
```

### 11.4. Tips on using MLP
- Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to scale your data. 
- There is built-in regularization parameter **alpha** (`Default 0.0001`). To find reasonable **alpha**, it's best to use **GridSearchCV**, usually in the range 10.0**-np.arange(1, 7)
- Empirically, we observed that **L-BFGS** converges faster and with better solutions on small datasets. For relatively large datasets, however, **Adam** is very robust. It usually converges quickly and gives pretty good performance. **SGD** with momentum or nesterov’s momentum, on the other hand, can perform better than those two algorithms if learning rate is correctly tuned.
- Since backpropagation has a high time complexity, it is advisable to start with smaller number of hidden neurons and few hidden layers for training.
- The loss function for Classifier is **Cross-Entropy** while for Regression is **Square-Error**

