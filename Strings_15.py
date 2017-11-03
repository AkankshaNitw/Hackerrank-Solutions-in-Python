#Two Strings
#!/bin/python3

import sys

def twoStrings(s1, s2):
    bool = False
    for c in s1:
        if c in s2:
            bool = True
            break
    if bool:
        return "YES"
    else:
        return "NO"

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)