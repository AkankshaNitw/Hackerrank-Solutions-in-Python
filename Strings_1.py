#Super Reduced String
#!/bin/python3

import sys
def remove_first_dups(s):
    flag = False
    temp_s = s
    for i,c in enumerate(s):
        if i+1<len(s) and s[i]==s[i+1]:
            flag = True
            if i+2<len(s):
                temp_s = s[:i]+s[i+2:]
            else:
                temp_s = s[:i]
            break
    return(temp_s, flag)
 
def super_reduced_string(s):
    flag = True
    while(flag):
        s, flag = remove_first_dups(s)
    if not s:
        return("Empty String")
    else:
        return(s)
      
s = input().strip()
result = super_reduced_string(s)
print(result)
