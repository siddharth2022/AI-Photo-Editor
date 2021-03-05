# AI Photo Editor

An easy handy tool to enhance your images.

# Screenshot
**1. Home Page**
[![HomePage](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/cover.JPG "HomePage")](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/cover.JPG "HomePage")

**2. Blur To HD**
[![Blur To HD](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/blur_to_hd.jpg "Blur To HD")](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/blur_to_hd.jpg "Blur To HD")

**2.1. Blur To HD Output**
[![Blur To HD Output](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/blur_to_hd_output.jpg "Blur To HD Output")](https://raw.githubusercontent.com/arshit09/AI-Photo-Editor/master/frontend/image/blur_to_hd_output.jpg "Blur To HD Output")


# Getting Started

1. After cloning this repository, download trained model folder from [**this link**](https://mega.nz/#F!zfQCjADD!Iu94Q2tr_6LectFjPKQ7lw "this link").
2. Place it with the cloned folder - **location is already configured in the code. No need to modify the code**

# Run it
1. Install all the required dependencies.
```
pip3 install -r requirements.txt
```
2. Run flask server "server.py" located in "/server/".
```
python server.py
```

3. Open index.html from /frontend/


# How It Works
- Uses **Flask** as backend server.
- Different ML model is used to generate images, read more [**here**](https://github.com/arshit09/AI-Photo-Editor/blob/master/AIPhotoEditor.pdf "here").


# Recommended Environment
- Python 3.5-3.8
- TensorFlow 1.15
- Keras 2.2.5
- flask_cors
- OpenCV
- Numpy


# Features
- Remove fog from the image
- Remove specific object from the image
- Blur to HD image
- Satellite view image to Map view image


# Bugs and Improvements?
- For any bug reporting or improvements, please submit an issue [here](https://github.com/siddharth2022/AI-Photo-Editor/issues/new "here").
