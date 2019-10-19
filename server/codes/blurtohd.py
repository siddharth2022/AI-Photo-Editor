# example of loading a pix2pix model and using it for image to image translation
from keras.models import load_model
from numpy import load
from numpy import vstack
from matplotlib import pyplot
from numpy.random import randint

# load and prepare training images
def load_real_samples(filename):
	# load compressed arrays
	data = load(filename)
	# unpack arrays
	X1, X2 = data['arr_0'], data['arr_1']
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]

# plot source, generated and target images
def plot_images(src_img, gen_img, tar_img):
	images = vstack((src_img, gen_img, tar_img))
	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Source', 'Generated', 'Expected']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 3, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.show()

# load dataset
[X1, X2] = load_real_samples('maps_256.npz')
print('Loaded', X1.shape, X2.shape)
# load model
model = load_model('g_model.h5')
# select random example
ix = randint(0, len(X1), 1)
print(ix)
src_image, tar_image = X1[ix], X2[ix]
# generate image from source
gen_image = model.predict(src_image)
# plot all three images
plot_images(src_image, gen_image, tar_image)
print(type(src_image), gen_image.shape, tar_image.shape)


##########################################################

import os
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.models import load_model
from matplotlib import pyplot as plt
import numpy as np
from numpy import vstack
import time


model = load_model('g_model.h5')

##############################################################

filename="./Capture1.PNG"
size=(256,256)
pixels = load_img(filename, target_size=size)

# convert to numpy array
pixels = img_to_array(pixels)
# split into satellite and map
sat_img = pixels[:, :256]
sat_img = (sat_img - 127.5) / 127.5


input_image=[]
input_image.append(sat_img)
input_image=np.array(input_image)

t1=time.time()
gen_image=model.predict(input_image)
t2=time.time()

###########################################################

from matplotlib import pyplot
def show_images(src_img, gen_img):
	images = vstack((src_img, gen_img))
	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Source', 'Generated']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 2, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.show()

show_images(input_image,gen_image)