#Anagram
#!/bin/python3

import sys

def anagram(s):
    cnt = 0
    if (len(s)%2) != 0:
        return -1
    for i in range(round(len(s)/2)):
        if s[i] not in s[round(len(s)/2):]:
            cnt += 1
        else:
            temp = s[round(len(s)/2):].index(s[i])
            #print ("temp", temp)
            s = s[:(round(len(s)/2))+temp] + "$" + s[(round(len(s)/2))+temp+1:]
            #print(s)
    return cnt

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)