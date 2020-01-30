from image_process import image_encrypt, image_decrypt, generate_key
from aes_image import aes_image_encrypt, aes_image_decrypt
from PIL import Image
import os

'''
Main Function
'''
if __name__ == "__main__":
    
    # Get the original image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/lena.tiff')
    
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
    
    # AES encrypt image
    encrypted_aes_image, key, IV = aes_image_encrypt('/Users/home/github/Cypto/RGB/misc/lena.tiff')
    encrypted_aes_image.save("encrypted_aes_image.png")
    
    # Get the pickle path
    root_dir = os.path.dirname(os.getcwd())
    encrypted_image_path = os.path.join(root_dir, 'RGB/aes_encrypted_image.pickle')
    
    # AES decrypt image
    decrypted_aes_image = aes_image_decrypt(encrypted_aes_image, key, IV)
    decrypted_aes_image.save("decrypted_aes_image.png")