from PIL import Image

import os








def get_pixels(image_path):
    
    # Load pixels from image
    im = Image.open(image_path) 
    px = im.load()

    pixels = []
    for i in range(0,256):
        for j in range(0,256):
            pixels.append((px[i, j]))
    return pixels


def modify_pixels(pixels):
    pass



if __name__ == "__main__":
    # Get the image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.1.09.tiff')
     
    pxls = get_pixels(im_path)
    print(pxls)
    modify_pixels(pxls)
    