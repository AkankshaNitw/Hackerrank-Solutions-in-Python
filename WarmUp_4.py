#A Very Big Sum
#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)