#Diagonal Difference
#!/bin/python3

import sys


n = int(input().strip())

a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diagonal = 0
for i in range(n):
    diagonal += a[i][i]

back_diagonal = 0
for i in range(n):
    back_diagonal += a[i][n-i-1]

print(abs(diagonal - back_diagonal))