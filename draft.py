from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import random




data = b'10000000'

key = get_random_bytes(16)

IV = get_random_bytes(16)
# print(key, IV)
cipher = AES.new(key, AES.MODE_OFB, IV)
print(cipher)
ct = cipher.encrypt(pad(data, 16))
# ct = unpad(ct, 16)
print(len(ct))





# print(key, IV)
cipher2 = AES.new(key, AES.MODE_OFB, IV)
pt = unpad(cipher2.decrypt(ct), 16)
print(pt)


