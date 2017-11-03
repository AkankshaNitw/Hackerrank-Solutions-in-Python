#Gemstones
#!/bin/python3

import sys

def gemstones(arr):
    #print(arr)
    cnt = 0
    for element in list(set(arr[0])):
        #print(element)
        temp_cnt = 0
        for i in range(1, len(arr)):
            #print(i)
            if element in arr[i]:
                temp_cnt += 1
        if temp_cnt == len(arr)-1:
            #print(temp_cnt)
            cnt += 1
    return cnt
            

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)