#Pangrams
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import string
s = input().strip()
s = (''.join(s.split())).lower()

alphas = list(string.ascii_lowercase)
counter = 0

for a in alphas:
    if a in s:
        counter += 1
if (counter==26):
    print("pangram")
else:
    print("not pangram")