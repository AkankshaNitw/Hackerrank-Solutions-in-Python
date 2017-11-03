#Beautiful Binary String
#!/bin/python3

import sys

def minSteps(n, B):
    # Complete this function
    cnt = 0
    cons_cnt = 0
    for i in range(n-2):
        #print("i ",i)
        if B[i]=='0' and B[i+1]=='1' and B[i+2]=='0':
            cnt += 1
            #print("cnt ",cnt)
            if i<n-4 and B[i+3]=='1' and B[i+4]=='0':
                #cons_cnt += 1
                #print("cons_cnt ",cons_cnt)
                B = B[:i+2]+"1"+B[i+3:]
                #print("B ",B)
                
    #print(cnt)
    #print(cons_cnt)
    return(cnt)
   

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)