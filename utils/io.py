import skimage.io as io
import matplotlib.pyplot as plt

def load(path):
    """Load an image from a file path."""
    return io.imread(path)

def show(img, title=None):
    """Display an image using matplotlib."""
    plt.figure()
    plt.imshow(img, cmap="gray")
    if title:
        plt.title(title)
    plt.axis("off")
    plt.show()
