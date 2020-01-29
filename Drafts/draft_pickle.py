from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from bitstring import BitArray
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import random
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
    with open('Di1.pickle', 'wb') as pickle_out:
        pickle.dump(ciphertext, pickle_out)
    
    print("Written done!")
    
    return key, IV

def image_aes_decrypted(image_path, key, IV):

    # Load the data from the pickle file
    with open('Di1.pickle', 'rb') as List:
        List = pickle.load(List)
    
    PlainText = []
    for item in List:
        decipher = AES.new(key, AES.MODE_OFB, IV)
        pt = unpad(decipher.decrypt(item), 16)
        PlainText.append(pt)
    print(PlainText)
    
    img = create_image(PlainText)
    img = img.rotate(-90)
    img.save("yeah.png")
    
    
    
if __name__ == '__main__':
    key, IV= image_aes_ofb('/Users/home/github/Cypto/Reversible_Data_Hiding/pre_processed_img.png')
    # img.save('draft.png')
    
    
    image_aes_decrypted('/Users/home/github/Cypto/Reversible_Data_Hiding/draft.png', key, IV)
    