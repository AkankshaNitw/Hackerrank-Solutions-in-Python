#Sherlock and Anagrams
#!/bin/python3

import sys

def countAnagrams(l):
    cnt = 0
    for i, e in enumerate(l):
        j= i + 1
        while (j<len(l)):
            if sorted(e) == sorted(l[j]):
                cnt += 1
            j += 1
    return (cnt)

def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)):
        myList = []
        for j in range(len(s)-i+1):
            myList.append(s[j:j+i])
        count += countAnagrams(myList)
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)