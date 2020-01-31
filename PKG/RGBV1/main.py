from AES import aes_image
from ENCODE import image_process
from PIL import Image
import os

'''
Main Function
'''
if __name__ == "__main__":
    
    # Get the original image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'RGBV1/misc/lena.tiff')
    
    # Save the original image
    original_img = Image.open(im_path)
    original_img.save("Outputs/original_img.png")
    
    
    # Encrypt image
    key = image_process.generate_key()
    encode_image, decipher_key = image_process.image_encrypt(im_path, key)
    encode_image.save("Outputs/encode_image.png")
    
    # Recover image
    encode_image_path = os.path.join(root_dir, 'RGBV1/Outputs/encode_image.png')
    decode_image = image_process.image_decrypt(encode_image_path, decipher_key)
    decode_image.save("Outputs/decode_image.png")
    
    # AES encrypt image
    encrypted_aes_image, key, IV = aes_image.aes_image_encrypt(im_path)
    encrypted_aes_image.save("Outputs/encrypted_aes_image.png")
    
    # Get the pickle path
    root_dir = os.path.dirname(os.getcwd())
    encrypted_image_path = os.path.join(root_dir, 'RGBV1/Outputs/aes_encrypted_image.pickle')
    
    # AES decrypt image
    decrypted_aes_image = aes_image.aes_image_decrypt(encrypted_aes_image, key, IV)
    decrypted_aes_image.save("Outputs/decrypted_aes_image.png")