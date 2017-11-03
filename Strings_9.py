#Alternating Characters
#!/bin/python3

import sys

def alternatingCharacters(s):
    cnt = 0
    for i in range(len(s)-1):
        #print(i)
        if s[i]==s[i+1]:
            #print(s[i+1])
            cnt += 1
    return cnt
            
        

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)