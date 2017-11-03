#CamelCase
#!/bin/python3

import sys


s = input().strip()
upperCnt = 0
for c in s:
    if c.isupper():
        upperCnt += 1
print(upperCnt+1)
