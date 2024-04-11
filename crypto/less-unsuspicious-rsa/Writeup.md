
# AmateursCTF 2024 - less-suspicious-rsa
- Write-Up Author: Dark

- Flag: amateursCTF{...}

## Challenge Description:
>I need help factoring this modulus, it looks less suspicious, but I can't factor using any conventional methods.
## Write up  

### Look at this code:
```python
from Crypto.Util.number import *

def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        p += n
    return p

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


flag = bytes_to_long(open('flag.txt', 'rb').read().strip())
p = getPrime(512)
q = nextPrime(p, factorial(90))
p = getPrime(512)
N = p * q
e = 65537
c = pow(flag, e, N)
print(N, e, c)
```
