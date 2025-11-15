from skimage import filters, morphology

def vessel_mask(img):
    thresh = filters.threshold_otsu(img)
    mask = img > thresh
    cleaned = morphology.remove_small_objects(mask, 50)
    return cleaned

def skeleton(mask):
    return morphology.skeletonize(mask)
