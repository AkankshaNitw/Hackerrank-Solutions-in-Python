#Caesar Cipher
#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
out_s = ""
for c in s:
    if c.isalpha():
        if c.isupper():
            out_s += chr(ord("A") + ((ord(c)-ord("A")+k)%26))
        else:
            out_s += chr(ord("a") + ((ord(c)-ord("a")+k)%26))
    else:
        out_s += c
print(out_s)