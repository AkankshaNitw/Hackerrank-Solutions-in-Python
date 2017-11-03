#Mars Exploration
#!/bin/python3

import sys


S = input().strip()
cnt = 0
for i in range(0, len(S), 3):
    if S[i]!="S": 
        cnt += 1
    if S[i+1]!= "O":
        cnt += 1
    if S[i+2]!= "S":
        cnt += 1
print(cnt)