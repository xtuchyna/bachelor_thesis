"""
TODO#: describe program in short - what is the purpose and use case
TODO: module commenting - can use this multiline commenting
TODO: add copyright mark
TODO: check out licensing guidlines from fedoraproject.org page
    e.g.: GPL BSD MIT licenses
TODO: make code more structured
    checkout https://www.python.org/dev/peps/pep-0257/
"""


import tensorflow as tf
from tensorflow import keras

import numpy as np

import matplotlib.pyplot as plt
plt.show(block=True)

from PIL import Image, ImageOps

print( tf.__version__ + "\n" )

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print( "train_images:", train_images.shape )
print( "train_labels:", len(train_labels), "\n" )

print( "test_images:", test_images.shape )
print( "test_labels:", len(test_labels), "\n" )

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 250.0
test_images = test_images / 250.0

#This block prints the pic and pic2 images (example images from the training dataset)
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(True)
plt.savefig( "pic.png" )

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.savefig( "pic2.png" )
#end of the print block

model = keras.Sequential([
    # Flatten layer transforms the input image (which is 28x28) to just one dimensional array
    # no parameters to learn, only formats the input data
    keras.layers.Flatten( input_shape = ( 28, 28 ) ),
    
    #Dense layers - fully or densely-connected neural layers
    #units = nodes = neurons
    #128 units
    keras.layers.Dense( 128, activation = tf.nn.relu ),
    #10 units - one for each of the 10 labels
    keras.layers.Dense( 10, activation = tf.nn.softmax )
])

#model compiling
model.compile(
    #defines how the model is updated based on the data it sees and its loss function
    optimizer = tf.train.AdamOptimizer(),

    #loss function measures how accurate is the model during trainig
    #the less number the better.
    loss = "sparse_categorical_crossentropy",

    #monitors the training and testing
    #accuracy = fraction of the correctly classified images
    metrics = [ "accuracy" ]
)

print( "model results without any training" )
train_loss, train_acc = model.evaluate( train_images, train_labels )
print( "train accuracy: ", train_acc )
print( "train loss: ", train_loss, "\n")

#the training step, the model is "fit" to the trainig data
model.fit( train_images, train_labels, epochs = 5 )

print( "model results after training" )
train_loss, train_acc = model.evaluate( train_images, train_labels )
print( "train accuracy: ", train_acc )
print( "train loss: ", train_loss, "\n" )

print( "model results after training on test dataset which was never seen by the model before: " )
test_loss, test_acc = model.evaluate( test_images, test_labels )
print( "test accuracy: ", test_acc )
print( "test loss: ", test_loss )

# now, if we want to use the trained model on our custom image
# first, we need to open, convert to grayscale and invert the image (later explained)
raw_pic = Image.open( "custom_sweater.jpeg" ).convert( "L" )
raw_pic = ImageOps.invert( raw_pic )

# now resize the image
max_size = ( 28, 28 )
raw_pic = ImageOps.fit( raw_pic, max_size, Image.ANTIALIAS )

# because of the np.array we inverted the image before - np.array() somehow inverted the image
# TODO find out why
pic_array = np.array( raw_pic )

# same preprocessing as in beginning
pic_array = pic_array / 250.0
print( "resolution of our image: ", pic_array.shape )

plt.figure()                                                                                                                       
plt.grid(True)
plt.imshow( pic_array )
plt.savefig( "converted_custom_image.png" )

# our keras model works only with batches - collections of images (coz it is optimized to work on multiples examples at once)
# thus we add pic_array to a list
test_batch = ( np.expand_dims( pic_array, 0 ) )
print( "our test collection: ", test_batch.shape )
print( "model's predictions for the test image: ", model.predict( test_batch ) )

plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow( test_batch[ 0 ], cmap=plt.cm.binary)
plt.xlabel( class_names[ np.argmax( model.predict( test_batch ) ) ] )
plt.savefig( "custom_pic.png" )
print( "see custom_pic.png for result" )
