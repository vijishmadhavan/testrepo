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







