#Game of Thrones - I
#!/bin/python3

import sys

def gameOfThrones(s):
    l = "".join(set(s))
    cnt = 0
    for e in l:
        #print(e)
        if (s.count(e)) % 2 != 0:
            #print("odd")
            cnt += 1
    if cnt < 2:
        return("YES")
    else:
        return("NO")
    

s = input().strip()
result = gameOfThrones(s)
print(result)