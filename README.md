# Xray Segmenation

# Quick Try - APP

APP - https://huggingface.co/spaces/Vijish/testapp

## Dataset:

- The dataset had few images which did not have segmentation mask.

Link: https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels


## Docker

### Build
```
docker build -t testapp1:latest .
```

### Run
```
docker run -p 8501:8501 testapp1:latest
```

Navigate to http://localhost:8501 for the app. (Streamlit runs on port 8501 by default)

## Technical details
- U-Net allows us to look at pixel-wise representations of our images through sizing it down and then blowing it back up into a high resolution image. The first part we call an "encoder" and the second a "decoder"
-  U-Net learner with a Residual Neural Network (ResNet) backbone and then trigger the fast.ai training process,We have used resnet 34.


## Installation Details

- **fastai==1.0.61** (and its dependencies).  Please dont install the higher versions
- **PyTorch 1.6.0** Please don't install the higher versions


