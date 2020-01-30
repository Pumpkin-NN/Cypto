from image_process import image_encrypt
from image_process import image_decrypt
from image_process import generate_key
from PIL import Image
import os

'''
Main Function
'''
if __name__ == "__main__":
    
    # Get the original image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/4.2.05.tiff')
    
    # Save the original image
    original_img = Image.open(im_path)
    original_img.save("original_img.png")
    
    # Encrypt image
    key = generate_key()
    encode_image, decipher_key = image_encrypt(im_path, key)
    encode_image.save("encode_image.png")
    
    # Recover image
    encode_image_path = os.path.join(root_dir, 'RGB/encode_image.png')
    recover_image = image_decrypt(encode_image_path, decipher_key)
    recover_image.save("recover_image.png")

    