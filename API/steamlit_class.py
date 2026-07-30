# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:48:18 2023

@author: Hosseini
"""

import streamlit as st
import cv2
from PIL import Image
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model as keras_load_model

nom_classe = [
    "Avulsion fracture",
    "Comminuted fracture",
    "Fracture Dislocation",
    "Greenstick fracture",
    "Hairline Fracture",
    "Impacted fracture",
    "Longitudinal fracture",
    "Oblique fracture",
    "Pathological fracture",
    "Spiral Fracture"
]

@st.cache_data
def load_model():
    model_architecture = 'arch_clas_os.json'
    model_weights = 'arch_clas_os.h5'
    model = 	model_from_json(open(model_architecture).read())
    model.load_weights(model_weights)  
    return model

with st.spinner('Model is being loaded..'):
  model=load_model()
 

st.write("""
#  Classification des fractures osseuses
""")

file = st.file_uploader("Upload the image to be classified", type=["jpg", "png", "jpeg"])


def upload_predict(image, model):  
    image = np.asarray(image)
    image = image.astype('float32')
    image = cv2.resize(image, (224, 224))
    image /= 255
    image = image.reshape([-1, 224, 224, 3])
    
    prediction = model.predict(image)
    pred_class = np.argmax(prediction, axis=1)       
    
    return pred_class, prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, width="stretch")
    
    pred_class, prediction = upload_predict(image, model)
    
    st.write(" Type de fracture :", nom_classe[pred_class[0]])
    st.write(" Probabilité :", float(prediction[0][pred_class[0]]))