import numpy as np
from skimage import exposure, restoration

def normalize(img):
    img = img.astype("float32")
    return (img - img.min()) / (img.max() - img.min() + 1e-8)

def denoise(img):
    img = normalize(img)
    return restoration.denoise_bilateral(
        img,
        sigma_color=0.05,
        sigma_spatial=3,
    )

def enhance(img):
    img = normalize(img)
    return exposure.equalize_adapthist(img, clip_limit=0.03)
