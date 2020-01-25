from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from ImageModification import decimalToBinary, binaryToDecimal
from bitstring import BitArray
from PIL import Image
import numpy as np
import random
import math
import io


def image_aes_ofb_encryption(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # AES_OFB encryption
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    
    encrypted_bits = ""
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            cipher = AES.new(key, AES.MODE_OFB, IV)
            cipher_text = cipher.encrypt(pad(modify_pixel, 16))
            
            cipher_text = BitArray(cipher_text)
            cipher_text = cipher_text.bin
            encrypted_bits = encrypted_bits + cipher_text
    encrypted_bits = [encrypted_bits[x:x+8] for x in range(0,len(encrypted_bits),8)]
    
    # Find the total items
    count = 0
    for i in encrypted_bits:
        count = count + 1
        
    # Reshape to 2D array
    encrypted_bits = np.array(encrypted_bits)
    
    encrypted_bits = encrypted_bits.reshape(int(math.sqrt(count)), int(math.sqrt(count)))
    
    # Create the encypted image
    img = Image.fromarray(encrypted_bits , 'L')
    size = int(math.sqrt(count)), int(math.sqrt(count))
    img = img.resize(size)
    
    # Return the modified image
    return img, key, IV