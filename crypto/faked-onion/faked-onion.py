import hmac
from os import urandom

def strxor(a: bytes, b: bytes):
    return bytes([x ^ y for x, y in zip(a, b)])

class Cipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = 16
        self.rounds = 1

    def F(self, x: bytes):
        return hmac.new(self.key, x, 'md5').digest()[:15]

    def encrypt(self, plaintext: bytes):
        plaintext = plaintext.ljust(self.block_size, b'\x00')
        ciphertext = b''
        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i+self.block_size]
            for _ in range(self.rounds):
                L, R = block[:-1], block[-1:]
                L, R = R, strxor(L, self.F(R))
                block = L + R
            ciphertext += block

        return ciphertext
'''
Encrypt function:
message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
L = xxxxxxxxxxxxxxxxxxxxxx, R = x
L = x                       R = xxxxxxxxxxxxxxxxxxxxxx ^ F(x)
find F(x) in x is printable
F(x) = R ^ xxxxxxxxxxxxxxxxxxxxxx
'''

key = urandom(16)
key = b'\xa6>\x9a\xffr\xbc\xbcF\x92/\xd5n\x8f\xa1\xd8z'
cipher = Cipher(key)
from string import printable
flag = bytes.fromhex('6e5d1c8e1db0d4615e77f214a12483626947257e2f8082f2af9ffa7a316b3bbd34bb2fef634a8bcc413b8e34f48959d872c63655c3f94bf335e12f080cb4ce3b65de5928933e53ce438b12e724cd436e7de13dc385')
block_size = 16
for i in range(0,len(flag),block_size):
    print(i,chr(flag[i]),flag[i+1:i+block_size])
i = 0
a1 = b'n'*16
a1 = bytes.fromhex('6e521f8107bbcf7d435ac83cb4258553')
a1 = a1[1:16]
print(strxor(strxor(a1,b'n'*15),flag[i+1:i+block_size]).decode(),end="n")
i = 16
a2 = b'i'*16
a2 = bytes.fromhex('6941137a3fb684f5a3a9fc7507630dbf')
a2 = a2[1:16]
print(strxor(strxor(a2,b'i'*15),flag[i+1:i+block_size]).decode(),end='i')
i = 32
a3 = b'4'*16
a3 = bytes.fromhex('34e17ff6320ccda70660c872b991328a')
a3 = a3[1:16]
print(strxor(strxor(a3,b'4'*15),flag[i+1:i+block_size]).decode(),end='4')
i = 48
a4 = b'r'*16
a4 = bytes.fromhex('72df2143eee457b077fd021917b6d42c')
a4 = a4[1:16]
print(strxor(strxor(a4,b'r'*15),flag[i+1:i+block_size]).decode(),end='r')
i = 64
a5 = b'e'*16
a5 = bytes.fromhex('65e45b2282045dc217df12e61e9f153b')
a5 = a5[1:16]
print(strxor(strxor(a5,b'e'*15),flag[i+1:i+block_size]).decode(),end='e')
i = 80
a6 = b'}'*16
a6 = bytes.fromhex('7dfe71ddc8bd873f4901aa14c96d7c4c')
a6 = a6[1:16]
print(strxor(strxor(a6,b'}'*15),flag[i+1:i+block_size]).decode(),end='}')