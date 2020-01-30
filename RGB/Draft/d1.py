from bitstring import BitArray
import os


#27 8 190

def decimalToBinary(dec):  
    return bin(dec).replace("0b", "").zfill(8)

def binaryToDecimal(bi):
    return int(bi, 2)

def generate_key():
    random_key = os.urandom(1)
    random_key = BitArray(random_key)
    random_key = random_key.bin
    print(f'random_key:{random_key}')
    return random_key

key = generate_key()
def pixel_process(pixel, key):
    print(f'ori:{pixel}')
    pixel = pixel ^ int(key, 2)
    print(f'pixel:{pixel}')
    pixel = decimalToBinary(pixel)
    print(f'bin_pixel:{pixel}')
    msb = pixel[:4]
    print(f'msb:{msb}')
    lsb = pixel[4:]
    print(f'lsb:{lsb}')
    nb = lsb + msb
    print(f'bin_nb:{nb}')
    nb = binaryToDecimal(nb)
    print(f'nb:{nb}')
    return nb, key

if __name__ == '__main__':
    R = 32
    G = 17
    B = 122
    
    r, key1 = pixel_process(R, key)
    print(key1)
    print(f'r:{bin(r)}')
    g, key1 = pixel_process(G, key)
    print(key1)
    print(f'g:{bin(g)}')
    b, key1 = pixel_process(B, key)
    print(key1)
    print(f'b:{bin(b)}')

    print("############################")


    R, key2 = pixel_process(r, key1)
    print(key1)
    print(f'R:{bin(R)}')
    G, key2 = pixel_process(g, key1)
    print(key1)
    print(f'G:{bin(G)}')
    B, key2 = pixel_process(b, key1)
    print(key1)
    print(f'B:{bin(B)}')



