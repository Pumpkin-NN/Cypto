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

def exchange_msb_lsb(b, key):
    b = bin(b)[2:].zfill(8)
    msb = b[:4]
    lsb = b[4:]
    if lsb == '0000':
        lsb = int(lsb, 2) ^ int(key[:4], 2)
        lsb = bin(lsb)[2:].zfill(8)
    if lsb == msb:
        lsb = int(lsb, 2) ^ int(key[4:], 2)
        lsb = bin(lsb)[2:].zfill(8)
    eb = lsb + msb
    return eb

def binaryToDecimal(b):
    d = int(b, 2)
    return d

def pre_processing(image_path, key):
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
            R = binaryToDecimal(exchange_msb_lsb(R, key))
            G = binaryToDecimal(exchange_msb_lsb(G, key))
            B = binaryToDecimal(exchange_msb_lsb(B, key))
            modify_bit = (R, G, B)
            modify_bits.append(modify_bit)
          
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(modify_bits)
    
    return image

