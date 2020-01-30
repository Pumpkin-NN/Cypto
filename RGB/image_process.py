from PIL import Image
from bitstring import BitArray
import numpy as np
import os

def generate_key():
    random_key = os.urandom(1)
    random_key = BitArray(random_key)
    random_key = random_key.bin
    print(f'random_key:{random_key}')
    return random_key

def decimalToBinary(dec):  
    return bin(dec).replace("0b", "").zfill(8)

def binaryToDecimal(bi):
    return int(b, 2)


def pixel_encode_process(pixel, key):
    pixel = pixel ^ int(key, 2)
    pixel = decimalToBinary(pixel)
    msb = pixel[:4]
    lsb = pixel[4:]
    nb = lsb + msb
    nb = binaryToDecimal(nb)
    return nb

def pixel_decode_process(pixel, key):
    pixel = decimalToBinary(pixel)
    msb = pixel[:4]
    lsb = pixel[4:]
    rb = lsb + msb
    rb = binaryToDecimal(rb)
    rb = rb ^ int(key, 2)
    return rb
    
    
def binaryToDecimal(b):
    d = int(b, 2)
    return d

def image_encrypt(image_path, key):
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
            R = pixel_encode_process(R, key)
            G = pixel_encode_process(G, key)
            B = pixel_encode_process(B, key)
            modify_bit = (R, G, B)
            modify_bits.append(modify_bit)              
                  
    OUTPUT_IMAGE_SIZE = (height, width)
    img = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    img.putdata(modify_bits)
    
    return img, key

def image_decrypt(image_path, key):
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
            R = pixel_decode_process(R, key)
            G = pixel_decode_process(G, key)
            B = pixel_decode_process(B, key)
            modify_bit = (R, G, B)
            modify_bits.append(modify_bit)              
                  
    OUTPUT_IMAGE_SIZE = (height, width)
    img = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    img.putdata(modify_bits)
    
    return img

