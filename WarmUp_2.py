#Simple Array Sum
#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    return (sum(ar))

n = int(input().strip())
#print(n)
ar = list(map(int, input().strip().split(' ')))
#print(ar)
result = simpleArraySum(n, ar)
print(result)