#Staircase
#!/bin/python3

import sys


n = int(input().strip())
for i in range(n):
    print(" "*(n-i-1), end="")
    print("#"*(i+1))