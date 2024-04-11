
import sys
from random import randint
from Crypto.Util.number import bytes_to_long
from tqdm import tqdm


m = 150094635296999121
# flag = bytes_to_long(open('flag.txt', 'rb').read())
flag = bytes_to_long(b'1'*45) # flag has 45 bytes
upper = 1 << (flag.bit_length() + 1) # upper = nhieu vailon
bl = upper.bit_length()//4

def printf(a):
    sys.stdout.write(hex(a)[2:].zfill(bl))
    sys.stdout.write('\n')

def lcg():
    a = randint(0, m)
    c = randint(0, m)
    seed = randint(0, m)
    # print('time: ',a,c,seed)
    while True:
        seed = (a * seed + c) % m
        # print('seed now = ', seed)
        yield seed

def randbelow(n):
    a = next(x)
    # print('a = ', a)
    while a < n:
        a *= m
        a += next(x)
    # print('res = ', hex((a%n)^flag)[2:])
    return a % n

def trial():
    global x
    x = iter(lcg())
    printf(flag ^ randbelow(upper))
    printf(flag ^ randbelow(upper))

trial()
sys.stdout.flush()