from PIL import Image
from ImageModification import image_modification
from AES_OFB import image_aes_ofb, image_recover 
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

if __name__ == "__main__":
    
    # Get the orignal image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.1.12.tiff')
    
    #Save the original image
    original_img = Image.open(im_path)
    original_img.save("original_img.png")
    
    # Save the pre-processed image
    pre_processing_img = pre_processing(im_path)
    pre_processing_img.save("pre_processed_img.png")
    
    # Get the pre-processed image path
    pre_processed_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/pre_processed_img.png')
    
    # Save the MSB/LSB encrypted image
    img = image_modification(pre_processed_img_path)
    img.save('encrypted_img.png')

    # Get the MSB/LSB encrypted image path
    encrypted_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/encrypted_img.png')
    
    # Save the MSB/LSB decrypted image
    img = image_modification(encrypted_img_path)
    img.save('decrypted_img.png')
    
    # Save the AES encrypted pre-processing image
    img, key, IV = image_aes_ofb(pre_processed_img_path)
    img.save('aes_encrypted_img.png')
    print(f'i am the aes key:{key}, IV:{IV}')
    
    # Get the AES encrypted image path
    aes_encrypted_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/aes_encrypted_img.png')
    
    # Save the AES decrypted image
    image_recover(aes_encrypted_img_path, key, IV)
    # img.save('aes_decrypted_img.png')