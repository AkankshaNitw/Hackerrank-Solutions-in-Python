#Birthday Cake Candles
#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    cnt = 0
    largest = max(ar)
    for i in range(n):
        if ar[i] == largest:
            cnt += 1
    return cnt
       

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)