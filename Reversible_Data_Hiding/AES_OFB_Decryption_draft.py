from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from ImageModification import decimalToBinary, binaryToDecimal
from bitstring import BitArray
from PIL import Image
import numpy as np
import random

def image_aes_ofb_decryption(image_path, key, IV):
    cipher = AES.new(key, AES.MODE_OFB, IV)
    
    # Read the encrypted image
    byte = ''
    with open(image_path, "rb") as image:
        byte = image.read()
        byte = byte + byte
    
    byte = [byte[x:x+15] for x in range(0,len(byte),16)]
    print(byte)
    
    decrypt_bytes = []
    for i in byte:
        plaintext = unpad(cipher.decrypt(i), 16)
        decrypt_bytes.append(plaintext)
    print(decrypt_bytes)
    
    # plaintext = unpad(cipher.decrypt(byte), 16)
    # print(plaintext)
        