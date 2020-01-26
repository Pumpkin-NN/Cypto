# from bitstring import BitArray
# input_str = b'\xb9&\xa9\xfb\x08P\xa9&\xf2\xc03T\x16\xfe\x81\x02'
# c = BitArray(input_str)
# print(c.bin)


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import random




data = b'11111111'

key = b'\xb2\xa3\x00\xe1\x9f\x94\x159\xda\xbe\xb3\x0f\x1a\xe5U\xcb'
IV = b'\x10\x95S\xab\x12|\x1b\x96\xcb\x1bd\xbak\xe5\x9d\xd3'

# print(key, IV)
cipher = AES.new(key, AES.MODE_OFB, IV)
print(cipher)
ct = cipher.encrypt(pad(data, 16))
# print(ct)

# ct = b'\x03+@:\xac\xfd\xe2\x1e\x9f\xb6t\x87\xa0;\x15\xd6'



# print(key, IV)
ct = b'\x03+@:\xac\xfd\xe2\x1e\x9f\xb6t\x87\xa0;\x15\xd6'
cipher2 = AES.new(key, AES.MODE_OFB, IV)
print(cipher2)
pt = unpad(cipher2.decrypt(ct), 16)
print(pt)


