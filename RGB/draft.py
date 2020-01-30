from bitstring import BitArray
import os

random_key = os.urandom(1)
print(random_key)

c = BitArray(random_key)
c = c.bin
print(type(c))