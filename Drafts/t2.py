import binascii
i ='11111111'
i = int(i, 2)
print(i)
i = binascii.unhexlify('%x' % i)
print(i)
# i = str(i)
# i = i.encode('utf-8')
# i = str(i)
# print(i)