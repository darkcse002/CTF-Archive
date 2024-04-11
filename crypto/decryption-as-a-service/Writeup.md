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
$c^d = m + k\times N$
