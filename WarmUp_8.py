#Mini-Max Sum
#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

sum_list = []

for i in range(5):
    sumItr = 0
    for j in range(5):
        if j != i:
            sumItr += arr[j]
    sum_list.append(sumItr)
    
print(min(sum_list), max(sum_list))