#Plus Minus
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos_cnt = 0
neg_cnt = 0

for i in range(n):
    if arr[i] > 0:
        pos_cnt += 1
    elif arr[i] < 0:
        neg_cnt += 1

print(round((pos_cnt/n), 5))
print(round((neg_cnt/n), 5))
print(round(((n-pos_cnt-neg_cnt)/n), 5))