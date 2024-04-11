# AmateursCTF 2024 - less-suspicious-rsa
- Write-Up Author: Dark

- Flag: amateursCTF{...}

## Challenge Description:
>I need help factoring this modulus, it looks less suspicious, but I can't factor using any conventional methods.
## Write up  

### Look at this code:
```python
if isqrt(N) < c < N:
            if c == encrypted_flag or c == (N - encrypted_flag):
                print("sorry, that looks like the flag")
                continue
            print(hex(pow(c, d, N))[2:])
```
This cryptosystem always give us the value $c^d \equiv m \pmod{N}$ when c is satisfied the condition above: \
It makes us remember the attack that if we have N, we can easy recover flag by mutiply encrypted by k number and send k to that cryptosystem:\
$k^d \equiv m_k \pmod{N}$\
$(k\times enc)^d = value \pmod{N}$\
We have: \
$value = (k\times enc)^d = (k\times flag^e)^d \equiv  k^d\times flag \equiv m_k\times flag \pmod{N}$ \
then:\
$flag = m_k^{-1} \times value \pmod{N}$

### Recover N:
With $c^d \equiv m \pmod{N}$, we can rewrite it in this form:\
$c^d = m + k\times N$ \
$=> c^d - m = k\times N$ \
Then the idea that we'll find N by get greatest common divisor by the relation of each $c^d - m$ we create.\
Choose some specific c like this we can solve it: \
$c_1=a,c2_=a\times 2, c_3 = \frac{a}{2}$ \
$c_4=b,c_5=b\times 2, c_6 = \frac{b}{2}$ \
which a,b satisfied conditon ```python isqrt(N) < c < N:```.
we have: \
$c_1 \equiv a^d \pmod{N} => c_1 = a^d + k_1\times N$\
$c_2 \equiv {a\times 2}^d \equiv 2^d \times a \pmod{N} => c_2 = 2^d \times a^d + k_2\times N$\
$c_3 \equiv (\frac{a}{2})^d \equiv (\frac{1}{2})^d \times a  \pmod{N}=> c_3 =  (\frac{1}{2})^d\times a^d + k_3\times N$\
Can easily to see that:  \
$c_1^2 - c_2*c_3 = k_x\times N$ 
As the same we have: \
$c_4^2 - c_5\times c_6 = k_y\times N  $
We got: $k\times N = gcd(k_x\times N, k_y\times N)
In our case, we can know that N is 2047 bits cause the getPrime(1024) function for p,q
then we can check bit of N and divide it by the prime number by bruteforce until we got 2047 bit, it will be the N value
### Get Flag:
The same idea, we can continue with: \
$enc\times \frac{1}{2} = p_1 \equiv msg\times (\frac{1}{2}^d) \pmod{N}$ \
$enc\times 2 = p_2 \equiv msg\times (2)^d \pmod{N}$ \
i choose this cause when i checked the encrypted flag, it get 2046 bits, when we multiply enc by k times which k >= 3, it can be larger than N, then i choose k = 2 and run script many times to get the case that encrypted_flag*2 < N.
Then we have:\
$msg^2 \equiv p_1\times p_2 \pmod{N}$ \
We can check if it's a square root, we can easily get msg by ```python msg = iroot(msg,2)[0]```, if not we can use tonelli shanks algorithm to recover msg.
In this case the first one ```python is True ```
