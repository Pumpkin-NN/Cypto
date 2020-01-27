from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from bitstring import BitArray
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import binascii
import random
import base64

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
    
    # print(f"i am cipher:\n{key}\n{IV} ")
    
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            
            cipher = AES.new(key, AES.MODE_OFB, IV)
            cipher_text = cipher.encrypt(pad(modify_pixel, 16))
            # print(type(cipher_text))
            
            img_bin = open("Di1.bin", "ab")
            #img_bin = open("Di1.dat", "ab")
            img_bin.write(cipher_text)
    
    print("write done")

    #dt = np.dtype(np.int32)
    dt = np.dtype(np.uint8)
    
    # Read file using numpy "fromfile()"
    with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.bin', mode='rb') as f:
    #with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.dat', mode='rb') as f:
        # d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)
        d = np.fromfile(f, dtype=dt, count=height*width).reshape(height,width)

    # Make into PIL Image and save
    img = Image.fromarray(d)
    img.save('Di1_bin.png')
    #img.save('Di1_dat.png')
    
    return img, key, IV

def image_aes_decrypted(image_path, key, IV):
    #print(f"\n\ni am decipher:\n{key}\n{IV}\n\n ")
    decipher = AES.new(key, AES.MODE_OFB, IV)

    with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.bin', 'rb') as f:
    #with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.dat', 'rb') as f:
        f = f.read()
    print(type(f))
    
    '''
    items = []
    for x in range(0,len(f),16):
        item = f[x:x+16]
        plain_text = unpad(decipher.decrypt(item), 16)
        items.append(plain_text)
        
    print(items)
    '''        
        
    '''
    # with open('try1.bin', 'ab') as fi:
        items = []
        for x in range(0,len(f),16):
            pixel = f[x:x+16]
            items.append(pixel)
        
        items = items[:-1]

        for i in items:
            
            # fi.write(plain_text)
            break
    '''
    '''       
    # Define width and height
    w, h = 512, 512

    # Read file using numpy "fromfile()"
    with open('/Users/home/github/Cypto/Reversible_Data_Hiding/try1.bin', mode='rb') as f:
        d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)

    # Make into PIL Image and save
    img = Image.fromarray(d)
    img.save('Di2.png')
    '''
if __name__ == '__main__':
    img, key, IV= image_aes_ofb('/Users/home/github/Cypto/Reversible_Data_Hiding/pre_processed_img.png')
    # img.save('draft.png')
    
    
    image_aes_decrypted('/Users/home/github/Cypto/Reversible_Data_Hiding/draft.png', key, IV)
    