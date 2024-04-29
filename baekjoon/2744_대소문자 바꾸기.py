import sys

s = sys.stdin.readline()
result = ''

for i in range(len(s)-1):
    if s[i].isupper():
        result += s[i].lower()
    elif s[i].islower():
        result += s[i].upper()

print(result)