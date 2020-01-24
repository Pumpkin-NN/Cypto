from PIL import Image
from ImageEncryption import image_encryption
import numpy as np
import os

'''
Function: Pre-Processing Algorithm
Goal: Correct all the prediction errors
'''
def pre_processing(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # Show the original image
    im.show()

    processed_pxs = []
    for i in range(0,height):
        for j in range(0,width):
            inv = (px[i, j] + 128) % 256
            if i == 0 or j == 0:
                # TODO Special processing
                if i == 0:
                    pred = px[i+1, j] // 2
                else:
                    pred = px[i, j+1] // 2
            else:
                pred = ( px[i-1, j] + px[i, j-1] ) // 2
            
            dif = abs(pred - px[i, j])
            dif_inv = abs(pred - inv)
            
            if dif >= dif_inv:
                if px[i, j] > 128:
                    processed_px = pred - 63
                    processed_pxs.append(processed_px)
                else:
                    processed_px = pred + 63
                    processed_pxs.append(processed_px)
            else:
                processed_px = px[i, j]
                processed_pxs.append(processed_px)
    # Reshape to 2D array
    processed_pxs = np.array(processed_pxs)
    processed_pxs = processed_pxs.reshape(256, 256)
    
    # Return the pre-processing pixels
    return processed_pxs, width, height 

if __name__ == "__main__":
    # Get the image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.1.12.tiff')
    
    '''
    updated_pixels, width, height = pre_processing(im_path)
    print(updated_pixels)
    
    # Create a new PIL image
    img = Image.fromarray(np.uint8(updated_pixels * 255) , 'L')
    
    # Define the pre-processing image window size
    size = width, height
    img = img.resize(size)
    
    # Show the pre-processing image
    img.rotate(-90).show()
    '''
    image_encryption(im_path)

    