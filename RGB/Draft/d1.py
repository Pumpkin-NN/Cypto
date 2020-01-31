from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from bitstring import BitArray
from Crypto.Cipher import AES
from PIL import Image
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
    
def chunks(lst, n):
    for i in range(0, len(lst), n):
        return lst[i:i + n]

def aes(bits, key, IV):
    cipher = AES.new(key, AES.MODE_OFB, IV)
    bits = cipher.encrypt(pad(bits, 16))
    return bits

def recover(bits, key, IV):
    decipher = AES.new(key, AES.MODE_OFB, IV)
    bits = unpad(decipher.decrypt(bits), 16)
    bits = binaryToDecimal(bits)
    bits = decimalToBinary(bits)
    bits = exchange_msb_lsb(bits)
    bits = binaryToDecimal(bits)
    return bits

def bits_modify(bits):
    bits = BitArray(bits)
    bits = bits.hex
    
    bits = chunks(bits, 16)
    bits = bits[:1]
    bits = int(bits, 16)
    
    print(bits)
    print("\n")
    # bits = bits.bin[:8]
    # bits = binaryToDecimal(bits)
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
            R = aes(R, key, IV)
            
            G = exchange_msb_lsb(decimalToBinary(G))
            G = bytes(G, 'utf-8')
            G = aes(G, key, IV)
            
            B = exchange_msb_lsb(decimalToBinary(B))
            B = bytes(B, 'utf-8')
            B = aes(B, key, IV)
            
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
    with open('aes_image.pickle', 'wb') as f:
        pickle.dump(encrypted_bits, f)  
     
       
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(image_bits)
    image.save("ei.png")
    
    return image, key, IV
    
def aes_image_decrypt(img, key, IV):
    with open('aes_image.pickle', 'rb') as List:
        List = pickle.load(List)
    
    decrypted_bits = []
    for pixel in List:
        (R, G, B) = pixel
        R = recover(R, key, IV)
        G = recover(G, key, IV)
        B = recover(B, key, IV)
        
        decrypted_bit = (R, G, B)
        decrypted_bits.append(decrypted_bit)
        
    height = img.height
    width = img.width
    OUTPUT_IMAGE_SIZE = (height, width)
    image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    image.putdata(decrypted_bits)
    # image = image.rotate(-90)
    image.save("di.png")
    
    
if __name__ == "__main__":
   image, key, IV = aes_image_encrypt('/Users/home/github/Cypto/RGB/misc/lena.tiff')
   
   
   aes_image_decrypt(image, key, IV)