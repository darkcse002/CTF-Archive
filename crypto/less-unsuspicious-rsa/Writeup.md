
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
We can see that the nextPrime function return this value: $q = p + (-p \mod n) + k\times n + 1$ \
Let $p = k\times n + p\mod n$\, so:\
$q = k\times n + 1$\
with n is factorial(90), we can check it's bit and got 459 bits, then k.bit_length() <= 512 - 459 = 53 (bits).\
This take me to the topic [Coppersmith theorem](https://crypto.stackexchange.com/questions/5644/attacks-on-the-rsa-cryptosystem) that if we have the the atleast half of p bits $\frac{n}{4}$ bits (in this case is 256 bits), we can efficiently factorize N.
And yes, sage math have function to solve the function $F(x) = x + a [N]$. \
We simplify convert $q = k\times n + 1$ by this way:
We have: \
$F(x) = k\times n + 1 \pmod{N} => F(x)\times inverse(n) = G(x) = k + inverse(n) \pmod{N}$\
We can easily recover k by coppersmith method, with function small_root:\
``` k = f.small_roots(X=2^54,beta=0.2,epsilon=1/200) ``` \
choose beta such that $x > N^{beta}$, and epsilon small enough to make searching solution efficently
then we got k => q => p => easy to get phi and d to recover flag
#### References for Coppersmith's attack: https://hackmd.io/@nomorecaffeine/By_SVppIh


