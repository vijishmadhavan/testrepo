import streamlit as st
import urllib.request
import PIL.Image
from PIL import Image
import requests
import fastai
from fastai.vision import *
from fastai.utils.mem import *
from fastai.vision import open_image, load_learner, image, torch, Path
import numpy as np
from urllib.request import urlretrieve


def main():
  MODEL_URL = "https://www.dropbox.com/s/vreot1378ie7k67/testapp1.pkl?dl=1"
  urllib.request.urlretrieve(MODEL_URL, "testapp1.pkl")
  path = Path(".")
  learn=load_learner(path, 'testapp1.pkl')
  uploaded_file = st.file_uploader("Choose an image...")
  if uploaded_file is not None:
    a = PIL.Image.open(uploaded_file).convert('RGB')
    img_fast = open_image(uploaded_file)
    p,img_hr,b = learn.predict(img_fast)
    x = np.minimum(np.maximum(image2np(img_hr.data*255), 0), 255).astype(np.uint8)
    img = PIL.Image.fromarray(x).convert('RGB')
    size = a.size
    im1 = img.resize(size)
    blended = PIL.Image.blend(im1, a, alpha=0.5)
    st.image(blended, caption='Segmentation')

if __name__ == "__main__":
  main()