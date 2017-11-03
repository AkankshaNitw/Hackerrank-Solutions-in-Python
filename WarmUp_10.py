#Time Conversion
#!/bin/python3

import sys

def timeConversion(s):
    res = ""
    if s[-2:] == "AM":
        if s[:2] == "12":
            res = ("00" + s[2:-2])
        else:
            res = (s[:-2])       
    elif s[-2:] == "PM":
        if s[:2] == "12":
            res = (s[:-2])
        else:
            res = (str(int(s[:2])+12)+s[2:-2])
    return (res)

s = input().strip()
result = timeConversion(s)
print(result)