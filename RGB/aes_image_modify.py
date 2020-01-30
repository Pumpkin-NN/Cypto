from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import pickle
import math
import os
from bitstring import BitArray


def generate_key_IV():
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    return key, IV

def decimalToBinary(dec):  
    return bin(dec).replace("0b", "").zfill(8)

def binaryToDecimal(bi):
    return int(b, 2)

def modify

def aes_image_encrypt(image_path):
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()

    # Get the height and width from the original image
    height = im.height
    width = im.width

    modify_bits = []
    for i in range(0,height):
        for j in range(0, width):
            (R, G, B) = px[i,j]
            R = decimalToBinary(R)
            G = decimalToBinary(G)
            B = decimalToBinary(B)
            modify_bit = (R, G, B)
            modify_bits.append(modify_bit)
          
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(modify_bits)
    
    return image

def aes_image_decrypt(f, key, IV):
    
    
if __name__ == "__main__":
    key, IV = generate_key_IV()
    print(key, IV)