from PIL import Image
import numpy as np
import os

def pre_processing(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    print(px[4,6])
    
    # Get the height and width from the original image
    height = im.height
    width = im.width