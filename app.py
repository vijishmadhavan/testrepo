import streamlit as st
from PIL import Image
import numpy as np
from fastai.vision import open_image, load_learner, image, torch


MODEL_URL = "https://www.dropbox.com/s/eyhud3qtk6pzztd/testapp.pkl?dl=0"
urllib.request.urlretrieve(MODEL_URL, "testapp.pkl")
path = Path(".")
learn=load_learner(path, 'testapp.pkl')

uploaded_file = st.file_uploader("Choose an image...")
p,img_hr,b = learn.predict(uploaded_file)
x = np.minimum(np.maximum(image2np(img_hr.data*255), 0), 255).astype(np.uint8)
img = PIL.Image.fromarray(x)
st.image(img, caption='Sunrise by the mountains')
