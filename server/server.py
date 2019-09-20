from flask import Flask, request, send_file
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, save_img
from flask_cors import CORS
import os
import random
import numpy as np


global graph
graph = tf.get_default_graph()

image_to_map = load_model('models/image_to_map.h5')

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'

def predict(filename, process_type):
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)

    if process_type == 'object_removal':
        pass
    if process_type == 'fogg_removal':
        pass
    if process_type == 'image_to_map':
        # size=(256,256)
        # sat_img = load_img(input_path, target_size=size)
        # sat_img = img_to_array(sat_img)
        # # split into satellite and map
        # sat_img = (sat_img - 127.5) / 127.5

        # input_image=[]
        # input_image.append(sat_img)
        # input_image=np.array(input_image)
        # gen_image=image_to_map.predict(input_image)
        # gen_image=(gen_image+1)/2.0
        # save_img(output_path, gen_image)
        pass
    if process_type == 'blur_to_hd':
        pass
    if process_type == 'face_aging':
        pass


@app.route("/")
def index():
    return "helllo"

chars = "abcdefghijklmnopqrstuvwxyz"

@app.route("/process_image", methods = ['POST'])
def process_image():
    if 'image' in request.files:
        file = request.files['image']
        filename = ''.join(random.choice(chars) for x in range(10)) + '.' + file.filename.split('.')[-1]
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(path)
        file.save(path)
        predict(filename, request.form['type'])
        return filename
    return "Hello"

if __name__ == '__main__':
    app.run(debug = True)