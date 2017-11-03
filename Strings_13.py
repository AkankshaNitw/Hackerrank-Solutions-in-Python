#Making Anagrams
#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    cnt = 0
    for c in s1:
        if c not in s2:
            cnt += 1
        else:
            temp = s2.index(c)
            s2 = s2[:temp] + "$" + s2[temp+1:]
    cnt_2 = len(s2) - s2.count("$")
    return cnt + cnt_2

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)