#b = 'ob1000100'
'''
d = 79
b = bin(d).replace("0b", "").zfill(8)
print(b)
'''
'''
b = '0b1000100'
b = b[2:].zfill(8)
print(b)
'''

'''
b = bin(0b1000100 ^ 0b10001000)
print(b)

n = 0b11001100
m = bin(0b11001100 ^ 0b10001000)
print(m)
'''

b = '0b1000100'
b = int(b,2)
print(b)

m = '0b10001000'
m = int(m,2)
print(m)

n = m ^ b
print(n)

k = m ^ n
print(k)