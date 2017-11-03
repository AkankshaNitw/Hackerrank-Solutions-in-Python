#HackerRank in a String!
#!/bin/python3

import sys


q = int(input().strip())
test = "hackerrank"

for a0 in range(q):
    s = input().strip()
    j=0
    for i, c in enumerate(s):
        if s[i] == test[j]:
            j += 1
            if(j == len(test)):
                print ("YES")
                break
    if j!= len(test):
        print ("NO")