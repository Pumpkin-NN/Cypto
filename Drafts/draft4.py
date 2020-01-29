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
import pickle

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
    key = b'\xfa\xde8\t\xda\xc0\x9f\xf9E%\xee\xb5P\xe6\x9b\xc7'
    IV = b'\xbe\xad\x17\x19\t\x98`;\xd5\x1c\xc9H\xd3[\xc2g'
    
    #print(f"i am cipher:\n{key}\n{IV} ")
    
    ciphertext = []
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            
            cipher = AES.new(key, AES.MODE_OFB, IV)
            cipher_text = cipher.encrypt(pad(modify_pixel, 16)) 
            ciphertext.append(cipher_text)
    
    # Use pickle to write the list
    with open('Di1.pickle', 'wb') as f:
        pickle.dump(ciphertext, f)
    
    dt = np.dtype(np.uint8)
    
    # Read file using numpy "fromfile()"
    
    with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.pickle', mode='rb') as f:
        d = np.fromfile(f, dtype=dt, count=height*width).reshape(height,width)

    # Make into PIL Image and save
    img = Image.fromarray(d)
    
    img.save('Di4_pickle.png')
    
    return img, key, IV

def image_aes_decrypted(image_path, key, IV):
    #print(f"\n\ni am decipher:\n{key}\n{IV}\n\n ")
    decipher = AES.new(key, AES.MODE_OFB, IV)

    #with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.bin', 'rb') as f:
    with open('/Users/home/github/Cypto/Reversible_Data_Hiding/Di1.dat', 'rb') as f:
        f = f.read().split(b",")

    with open('Di1.pickle', 'rb') as fi:
        fi_list = pickle.load(fi)
    #print(fi_list)
    #print(f)
    #f_list = f[:-1]
    
    # b'\xa6\tY\x01$\xda\x84\xbf\x9fv\xf9\xf8\xb6A]\x1e'
    
    
    print(len(fi_list[0]))
    print(len(fi_list[1]))
    print(len(fi_list[-1]))
    
    plain_text = unpad(decipher.decrypt(fi_list[3]), 16)
    print(plain_text)
    '''
    plaintext = []
    for i in range(0, len(fi_list)):
        if len(fi_list[i]) == 16:
            print(fi_list[i])
            plain_text = unpad(decipher.decrypt(fi_list[i]), 16)
            continue
        else:
            print(len(fi_list[i]))
            print("wrong")
            break
    print(plaintext)
    '''
    '''
    plaintext = []
    for i in range(1, len(f_list)):
        plain_text = unpad(decipher.decrypt(f_list[i]), 16)
        plaintext.append(plain_text)
    print(plaintext)
    '''
    
    
    
    
    
    
    '''
    for item in f_list:
        print(item)
        # plain_text = unpad(decipher.decrypt(item), 16)
        #item: b'C\xe1$\xed@}\xef\x83J\x80\x18)\xab\x17\x9d\x80'
        #ciph: b'\xa6\x08X\x01$\xda\x84\xbf\x9fv\xf9\xf8\xb6A]\x1e'
        #file: b'\xa6\x08X\x00$\xdb\x84\xbe\x9fv\xf9\xf8\xb6A]\x1e'
        break
        
    # print(items)
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
    #img.save('draft4.png')
    
    
    # image_aes_decrypted('/Users/home/github/Cypto/Reversible_Data_Hiding/draft.png', key, IV)
    