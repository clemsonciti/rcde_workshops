# Convolution Neural Network for image classification

# Convolutional Neural Network - CNN


- CNNs are one type of ANN which utilize the neuron, kernel, activation function.
- Inputs must be in images (or assumed to be images)
- Using Forward & Backpropagation technique with certain property to process it faster
- CNNs best for object detection, image classification, computer vision

## Architecture of CNNs


![image](https://user-images.githubusercontent.com/43855029/129789560-452539b8-06c7-4a3b-8543-c2f6e5a6f9c6.png)
[Source](http://henrysprojects.net/projects/conv-net.html)

- A basic CNNs consists of Convolution Layers, Max Pooling Layers and fully connected Layer (Dense) before output layer
- A simple image can be simply flatten into 1D vector and driven through the regular fully connected NN. However, this requires lot of computational power if the image is large and has more color.
- Therefore, Convolution Layers and  Max Pooling

### Convolutional Layer (CNN or ConvNet)

- Take a look at the simple gray scale image below which contains 10 pixels on width & height. The color scale has only 2 values (black & white) or (binary -1 and 1), there fore the size of the following image is 10x10x1:

![image](https://user-images.githubusercontent.com/43855029/129790068-408bbad8-8752-4153-9ce3-9099cae1995a.png)

- However, regular image contains colors [RGB](https://www.rapidtables.com/web/color/RGB_Color.html) with each color scale ranges from 0-255, making the size of each image is: n x n x 3 (n = number of pixel).

![image](https://user-images.githubusercontent.com/43855029/129623983-173558ba-45f5-4a42-972d-a6252f7695e0.png)

- CNN uses the Convolved Feature to reduce the image size by dot product with given kernel.
- The image reduction without losing features and easier to process for good prediction

![image](https://user-images.githubusercontent.com/43855029/129624312-db0f2ce1-4767-4a18-9a02-f5cee4c6cfe5.png)

- So for 3 channel RGB colors, the image size have been reduced:

![image](https://user-images.githubusercontent.com/43855029/129624564-96d6d7e4-6409-4775-ad9d-2bf133fa0396.png)

- In other word, the convoluted image from RGB image would look like:

![image](https://user-images.githubusercontent.com/43855029/129791297-fae899e5-1745-4fa0-b348-1785dea769ea.png)


### Pooling Layer
- Similar to the Convolutional Layer, the Pooling layer is responsible for reducing the spatial size of the Convolved Feature.
- This is to decrease the computational power required to process the data through dimensionality reduction
- Two types of Pooling: Max Pooling & Average Pooling.

![image](https://user-images.githubusercontent.com/43855029/129624678-75532145-0e90-48d5-9703-c8ee626aa7f4.png)

In which Max Pooling performs a lot better than Average Pooling.

- The image after Max Pooling layer would look like:

![image](https://user-images.githubusercontent.com/43855029/129791581-5d9fa47d-1390-44c2-b86a-f66273a9f7ca.png)


### Flatten Layer
- Once the images have passed through Convolution Layer and Pooling Layer, its size has been reduced greatly and ready for MLP training (or to another Convolution steps).
- The image is then flatten to a column vector and passed through feed-forward NN and BackPropagation applied to every iteration.
- Softmax activation function is applied to classified the multi-output

More information can be found [here](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)


## Application of CNN in image classification

### The CIFAR10 database
- The [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) database consisting 60,000 color images with 10 different classes
- Each image has 32 x 32 pixels with color range from 0-255
- It is good database for pattern recognition and image classification task (the entire data is clean and ready for use).
- The dataset was divided into 50,000 images for training and 10,000 images for testing
- The 10 [classes](https://keras.io/api/datasets/cifar10/) are **airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck**
- Sample CIFAR10 data:

![image](https://user-images.githubusercontent.com/43855029/134049153-99879363-c761-4b1d-b378-78186024bb95.png)[Source](https://www.cs.toronto.edu/~kriz/cifar.html)

### Importing libraries
```python
import keras
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
```

### Import convolution, max pooling and flatten as mentioned above:
```python
from tensorflow.keras.layers import Conv2D # convolutional layers to reduce image size
from tensorflow.keras.layers import MaxPooling2D # Max pooling layers to further reduce image size
from tensorflow.keras.layers import Flatten # flatten data from 2D to column for Dense layer
```

### Load CIFAR10 data
```python
from tensorflow.keras.datasets import cifar10

# load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Normalized data to range (0, 1):
X_train, X_test = X_train/255, X_test/255
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
```

Sample ploting:
```python
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
for i in range(49):
    plt.subplot(7,7,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_train[i])
    # The CIFAR labels happen to be arrays, which is why you need the extra index    
    plt.xlabel(class_names[y_train[i][0]])
plt.show()
```

![image](https://user-images.githubusercontent.com/43855029/134049444-f95cd292-9b5f-40f9-852c-6bbe0a724d78.png)


Using One Hot Encoding from Keras to convert the label:

```python
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(y_train.shape)
print(y_test.shape)
```

### Construct Convolutional Neural Network
- For Convolution front end, starting with kernel size (3,3) with a number of filter 10 followed by Max Pooling Layer with pool_size = (2,2).
- The 2D data after two Max Pooling layer is flatten directly.

```python
model = Sequential()
model.add(Conv2D(8, (3, 3), strides=(1, 1), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Flatten())
model.add(Dense(100, activation='relu'))
#Output layer contains 10 different number from 0-9
model.add(Dense(10, activation='relu'))
model.summary()
```

```python
# compile model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  metrics=['accuracy'])                                                       
```

### Train model

Fit the model

```python
# fit the model
model_CNN = model.fit(X_train, y_train, epochs=10, 
                    validation_data=(X_test, y_test))
```

### Evaluate the output

Visualize the training/testing accuracy:

```python
fig = plt.figure(figsize=(8, 10), dpi=80)
plt.subplot(2,1,1)
plt.plot(model_CNN.history['accuracy'],"b-o")
plt.plot(model_CNN.history['val_accuracy'],"r-d")
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.legend(['train', 'test'])

plt.subplot(2,1,2)
plt.plot(model_CNN.history['loss'],"b-o")
plt.plot(model_CNN.history['val_loss'],"r-d")
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'])
plt.tight_layout()
fig
```

![image](https://user-images.githubusercontent.com/43855029/135329289-3e48cf23-ab0c-4a35-8074-b0a344e8dbbe.png)


### Save & reload CNN model
Save model:

```python
model.save('CNN_CIFAR10.keras')
```

Reload model:
```python
model_new = tf.keras.models.load_model('CNN_CIFAR10.keras')
```

### Evaluate model with testing data
```python
test_loss, test_accuracy = model_new.evaluate(X_test, y_test, batch_size=64)
print('Test loss: %.4f accuracy: %.4f' % (test_loss, test_accuracy))
```

```
157/157 [==============================] - 0s 2ms/step - loss: 1.1538 - accuracy: 0.6080
Test loss: 1.1538 accuracy: 0.6080
```

The accuracy rate is 0.6080 for testing data means there are 6080 right classification based on 10,000 sample of testing data

### Visualize the output with the first 25 testing images

```python
predictions = model_new.predict(X_test)
ypreds = np.argmax(predictions, axis=1)

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_test[i])
    plt.xlabel(class_names[ypreds[i]])
plt.show()
```

![image](https://user-images.githubusercontent.com/43855029/135329702-29eeb261-e7bb-4d93-bd6c-894e8360df16.png)

### Improving the performance?
Use more convolution and max pooling payer:

```python
model = Sequential()
model.add(Conv2D(8, (3, 3), strides=(1, 1), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(Flatten())
model.add(Dense(100, activation='relu'))
#Output layer contains 10 different number from 0-9
model.add(Dense(10, activation='relu'))

# compile model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  metrics=['accuracy'])     
model.fit(X_train, y_train, epochs=10, 
                    validation_data=(X_test, y_test))                   
```

```python
predictions = model.predict(X_test)
ypreds = np.argmax(predictions, axis=1)

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_test[i])
    plt.xlabel(class_names[ypreds[i]])
plt.show()
```
