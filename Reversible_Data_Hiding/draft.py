from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from bitstring import BitArray
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import binascii
import random

import math
import io

def create_image(bits):
    # Find the total items
    count = 0
    for i in bits:
        count = count + 1
      
    # Convert binary to decimal  
    pixels = []
    for item in bits:
        bit = binaryToDecimal(item)
        pixels.append(bit)
    
    # Reshape to 2D array
    pixels = np.array(pixels)
    pixels = pixels.reshape(int(math.sqrt(count)), int(math.sqrt(count)))
    
    # Create the AES encypted image
    img = Image.fromarray(np.uint8(pixels * 255) , 'L')
    size = int(math.sqrt(count)), int(math.sqrt(count))
    img = img.resize(size)
    
    return img

def image_aes_ofb(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # AES_CBC encryption
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    
    print(f"i am cipher:\n{key}\n{IV} ")
    encrypted_bits = ""
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            
            cipher = AES.new(key, AES.MODE_CBC, IV)
            cipher_text = cipher.encrypt(pad(modify_pixel, 16))
            #decipher = AES.new(key, AES.MODE_CBC, IV)
            #plain_text = unpad(decipher.decrypt(cipher_text), 16)
            #plain_text = plain_text.decode('utf-8')
            # print(cipher_text)
            cipher_text = BitArray(cipher_text)
            # print(f'bit_array:{cipher_text}')
            cipher_text = cipher_text.bin
            encrypted_bits = encrypted_bits + cipher_text
            #decrypted_bits.append(plain_text)
    
    encrypted_bits = [encrypted_bits[x:x+8] for x in range(0,len(encrypted_bits),8)]
    
    img = create_image(encrypted_bits)
    img = img.rotate(-90)
    
    
    # Return the AES encrypted image and the decrypted bits
    return img, key, IV

def image_aes_decrypted(image_path, key, IV):
    print(f"\n\ni am decipher:\n{key}\n{IV} ")
    decipher = AES.new(key, AES.MODE_CBC, IV)
    
    im = Image.open("draft.png")
    px = im.load()
    
    height = im.height
    width = im.width
    
    pixels = ''
    for i in range(0, height):
        for j in range(0, width):
                bit = decimalToBinary(px[i, j])
                pixels = pixels + bit


    pixels = int(pixels, 2)
    pixels = binascii.unhexlify('%x' % pixels)
    
    pixels = [pixels[x:x+16] for x in range(0,len(pixels),16)]
    
    for item in pixels:
        print(item)
        plain_text = unpad(decipher.decrypt(item), 16)
        
        print(plain_text)
        break

    # Item format: b'\x92\x98\xad\xa7\x8a\xf3k\x8c\n\x91\x9c\xdb6u\x86\xad'
    #              b'\xdf\x95\xc7\x8f\xferg\xb2\x85\xb9\x8d\xb3\x11\xe5\xfa\xd4'
    #              b'T\xba\xec\xe1\xcd\xaf\x9d$~~\xab\xc7t0(\xb1'
    
    
    # Ciph format: b'\x19S\x12l\x06L\xe1\x0fn\xb0\x94\x8c\x85\xcd\x03\x1a'
    
    # plain_text = unpad(decipher.decrypt(i), 16)
    # print(plain_text)
        
    # byte = binascii.hexlify(bytearray(pixels))
    # print(byte)
    
    # return pixels


if __name__ == '__main__':
    img, key, IV= image_aes_ofb('/Users/home/github/Cypto/Reversible_Data_Hiding/pre_processed_img.png')
    img.save('draft.png')
    
    image_aes_decrypted('/Users/home/github/Cypto/Reversible_Data_Hiding/draft.png', key, IV)
    