#Funny String
#!/bin/python3

import sys

def funnyString(s):
    reverse_s = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(reverse_s[i])-ord(reverse_s[i-1])):
            return ("Not Funny")
    return("Funny")

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)