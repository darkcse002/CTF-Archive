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
This cryptosystem always give us the value of m when c is satisfied the condition above: \
$c^d \equiv m \pmod{N}$, 
It makes us remember the attack that if we have N, we can easy find the message: \
$enc = msg^e \pmod{N}$ \
if we have: 
$2*enc = (2*msg)^e = 2^e.msg^e \pmod{N} $



*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

#this is list
* Item 1
* Item 2
  * Item 2a
  * Item 2b

#this is ordered list
1. Item 1
2. Item 2
3. Item 3
   1. Item 3a
   2. Item 3b

```c
thi is c code
```

this is table
column1|column2
-------|-------
a|b
c|d
d|d

to place new line with **double space** in the end of line

to placing image in readme.md  
![this is alt text](https://avatars.githubusercontent.com/u/68818539?v=4)
