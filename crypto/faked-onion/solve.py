from pwn import *
conn = remote('chal.amt.rs',1414)
print(conn.recvuntil(b'> '))

from string import printable
ls = []
for i in printable:
    conn.sendline(b'1')
    print(conn.recvline())
    break