#The Love-Letter Mystery
#!/bin/python3

import sys

def theLoveLetterMystery(s):
    cnt = 0
    for i in range(round(len(s)/2)):
        j = len(s)-i-1
        if s[i] < s[j]:
            while(s[i] != s[j]):
                if(s[j]!= "a" or s[j]!= "A"):
                    if(j+1 < len(s)):
                        s = s[:j]+ chr(ord(s[j])-1) +s[j+1:]
                    else:
                        s = s[:j]+ chr(ord(s[j])-1) 
                    cnt += 1
        elif s[i] > s[j]:
            while(s[i] != s[j]):
                if(s[i]!= "a" or s[i]!= "A"):
                    s= s[:i]+ chr(ord(s[i])-1) +s[i+1:]
                    cnt += 1
    return cnt          
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)