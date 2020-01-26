from PIL import Image
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

    # Pre-processing image
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
    processed_pxs = processed_pxs.reshape(height, width)
    
    
    # Create a pre-processed image
    img = Image.fromarray(np.uint8(processed_pxs * 255) , 'L')
    img = img.resize((height, width))
    img = img.rotate(-90)
    # img.show()
    
    # Return the pre-processed image
    return img 