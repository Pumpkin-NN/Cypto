from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import pickle
import math
import os

'''
Function: Use AES to encrypt image
'''
def image_aes_cbc(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # AES_OFB encryption
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    
    cipherbits = []
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            
            cipher = AES.new(key, AES.MODE_OFB, IV)
            cipherbit = cipher.encrypt(pad(modify_pixel, 16)) 
            cipherbits.append(cipherbit)
    
    # Use pickle to store the cipherbits
    with open('aes_image.pickle', 'wb') as f:
        pickle.dump(cipherbits, f)
        
    # Create image
    root_dir = os.path.dirname(os.getcwd())
    im_source = os.path.join(root_dir, 'Reversible_Data_Hiding/aes_image.pickle')
    dt = np.dtype(np.uint8)
    with open(im_source, mode='rb') as f:
        d = np.fromfile(f, dtype=dt, count=height*width).reshape(height,width)
    
    img = Image.fromarray(d)
    
    # Return the AES encrypted image and the AES key&IV
    return img, key, IV

'''
Function: Use AES to decrypt image
'''
def image_aes_decrypted(f, key, IV):
    
    with open(f, 'rb') as List:
        List = pickle.load(List)
    
    plainbits = []
    for item in List:
        decipher = AES.new(key, AES.MODE_OFB, IV)
        plainbit = unpad(decipher.decrypt(item), 16)
        plainbits.append(plainbit)
    
    # Create image
    # Find the total items
    count = 0
    for i in plainbits:
        count = count + 1
      
    # Convert binary to decimal  
    pixels = []
    for item in plainbits:
        bit = binaryToDecimal(item)
        pixels.append(bit)
    
    # Reshape to 2D array
    pixels = np.array(pixels)
    pixels = pixels.reshape(int(math.sqrt(count)), int(math.sqrt(count)))
    
    # Create the AES encypted image
    img = Image.fromarray(np.uint8(pixels * 255) , 'L')
    size = int(math.sqrt(count)), int(math.sqrt(count))
    img = img.resize(size)
    img = img.rotate(-90)
    
    return img