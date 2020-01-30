from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image, ImageOps
from bitstring import BitArray
from Crypto.Cipher import AES
import numpy as np
import pickle
import math
import os
def decimalToBinary(dec):  
    return bin(dec).replace("0b", "").zfill(8)

def binaryToDecimal(bi):
    return int(bi, 2)

def exchange_msb_lsb(bi):
    MSB = bi[:4]
    LSB = bi[4:]
    nb = LSB + MSB
    return nb
    
def aes_encrypted_bits(bits, key, IV):
    cipher = AES.new(key, AES.MODE_OFB, IV)
    bits = cipher.encrypt(pad(bits, 16))
    return bits

def aes_decrypted_bits(bits, key, IV):
    decipher = AES.new(key, AES.MODE_OFB, IV)
    bits = unpad(decipher.decrypt(bits), 16)
    bits = binaryToDecimal(bits)
    bits = decimalToBinary(bits)
    bits = exchange_msb_lsb(bits)
    bits = binaryToDecimal(bits)
    return bits

def bits_modify(bits):
    bits = BitArray(bits)
    bits = bits.bin[:8]
    bits = binaryToDecimal(bits)
    return bits
    
def aes_image_encrypt(image_path):
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()

    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # AES_CBC encryption
    key = get_random_bytes(16)
    IV = get_random_bytes(16)

    encrypted_bits = []
    image_bits = []
    for i in range(0,height):
        for j in range(0, width):
            (R, G, B) = px[i,j]
            R = exchange_msb_lsb(decimalToBinary(R))
            R = bytes(R, 'utf-8')
            R = aes_encrypted_bits(R, key, IV)
            
            G = exchange_msb_lsb(decimalToBinary(G))
            G = bytes(G, 'utf-8')
            G = aes_encrypted_bits(G, key, IV)
            
            B = exchange_msb_lsb(decimalToBinary(B))
            B = bytes(B, 'utf-8')
            B = aes_encrypted_bits(B, key, IV)
            
            # AES encrypt bits
            encrypted_bit = (R, G, B)
            encrypted_bits.append(encrypted_bit)
            
            # Image bits
            r = bits_modify(R)
            g = bits_modify(G)
            b = bits_modify(B)
            image_bit = (r, g, b)
            image_bits.append(image_bit)
            
    # Use pickle to store the cipher
    with open('aes_encrypted_image.pickle', 'wb') as f:
        pickle.dump(encrypted_bits, f)  
     
       
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(image_bits)
    
    return image, key, IV
    
def aes_image_decrypt(img, key, IV):
    with open('aes_encrypted_image.pickle', 'rb') as List:
        List = pickle.load(List)
    
    decrypted_bits = []
    for pixel in List:
        (R, G, B) = pixel
        R = aes_decrypted_bits(R, key, IV)
        G = aes_decrypted_bits(G, key, IV)
        B = aes_decrypted_bits(B, key, IV)
        
        decrypted_bit = (R, G, B)
        decrypted_bits.append(decrypted_bit)
        
    height = img.height
    width = img.width
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(decrypted_bits)
    image = image.rotate(-90)
    image = ImageOps.mirror(image)
    
    return image
   
   
   