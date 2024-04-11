# AmateursCTF 2024 - less-suspicious-rsa
- Write-Up Author: whoami \[[whoami](the link to me)\]

- Flag: place your flag here

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
$c1=a,c2=a\times 2, c3 = \frac{a}{2}$ \
$c4=b,c5=b\times 2, c6 = \frac{b}{2}$ \
which a,b satisfied conditon ```python isqrt(N) < c < N:```.
we have: \
$c_1 \equiv a^d \pmod{N} => c_1 = a^d + k_1\times N$\
$c_2 \equiv {a\times 2}^d \equiv 2^d \times a \pmod{N} => c_2 = 2^d \times a^d + k_2\times N$\
$c_3 \equiv (\frac{a}{2})^d \equiv (\frac{1}{2})^d \times a  \pmod{N}=> (\frac{1}{2})^d + k_3\times N$\
Can **easily** to see that: 
### $\frac{(c_2-k_2\times N)^2}{(a^d)^2} =\frac{(c_3-k_2\times N)}{a^d}$
