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
    
    
##################################################################################################################
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import random



def image_aes_ofb_encryption():
    pass


data = b'11111111'

key = get_random_bytes(16)

IV = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OFB, IV)
print(cipher)
ct = cipher.encrypt(pad(data, 16))
print(ct)



cipher2 = AES.new(key, AES.MODE_OFB, IV)
pt = unpad(cipher2.decrypt(ct), 16)
print(pt)
# ct = b64encode(ct_bytes).decode('utf-8')
# print(f'ct:{ct}')


# de_bytes = cipher.decrypt(ct_bytes)

# print(f'de_bytes:{de_bytes}')
# de = (de_bytes).decode('utf-8')
# print(f'de:{de}')