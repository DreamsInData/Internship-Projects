import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import sys
import os

# Load the model
model = tf.keras.models.load_model("animal_classifier_model_v2.h5")

# Class names 
class_names = ['Bear', 'Bird', 'Cat', 'Cow', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Giraffe', 'Horse', 'Kangaroo', 'Lion', 'Panda','Tiger','Zebra']

# Load and preprocess image
img_path = "C:\\Users\\ak656\\Desktop\\internship projects\\Animal Classification\\dataset\\Bear\\bear_1_1.jpg"  
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
predictions = model.predict(img_array)
predicted_class = class_names[np.argmax(predictions)]

print(f"Predicted Class: {predicted_class}")