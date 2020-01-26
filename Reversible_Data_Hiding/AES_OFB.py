from MSB_LSB import decimalToBinary, binaryToDecimal
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from bitstring import BitArray
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
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
    
    # AES_OFB encryption
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    
    encrypted_bits = ""
    decrypted_bits = []
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = bytes(modify_pixel, 'utf-8')
            cipher = AES.new(key, AES.MODE_OFB, IV)
            cipher_text = cipher.encrypt(pad(modify_pixel, 16))
            decipher = AES.new(key, AES.MODE_OFB, IV)
            plain_text = unpad(decipher.decrypt(cipher_text), 16)
            plain_text = plain_text.decode('utf-8')
            
            cipher_text = BitArray(cipher_text)
            cipher_text = cipher_text.bin
            encrypted_bits = encrypted_bits + cipher_text
            decrypted_bits.append(plain_text)
    
    encrypted_bits = [encrypted_bits[x:x+8] for x in range(0,len(encrypted_bits),8)]
    
    img = create_image(encrypted_bits)
    img = img.rotate(-90)
    
    # Return the AES encrypted image and the decrypted bits
    return img, decrypted_bits

def image_aes_decrypted(decrypted_bits):
    
    img = create_image(decrypted_bits)
    img = img.rotate(-90)
    
    # Return the AES decypted image
    return img