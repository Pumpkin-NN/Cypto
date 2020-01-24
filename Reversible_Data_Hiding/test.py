from PIL import Image

import os







# Get the pixels from the grey-scale image(256x256)
def get_pixels(image_path):
    
    # Load pixels from image
    im = Image.open(image_path) 
    px = im.load()

    pixels = []
    for i in range(0,256):
        for j in range(0,256):
            pixels.append((px[i, j]))
    return pixels

# Find the inverse of the pixels
def inverse_pixels(pixels):
    inv_pixels = []
    for k in pixels:
        m = (k + 128) % 256
        inv_pixels.append(m)
        
    return inv_pixels






if __name__ == "__main__":
    # Get the image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.1.09.tiff')
     
    pxls = get_pixels(im_path)
    inv_pixels = inverse_pixels(pxls)
    print(inv_pixels)
    