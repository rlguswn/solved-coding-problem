import sys

s = sys.stdin.read().lower().replace('\n', '').replace(' ', '')
result = [0] * 26

for i in s:
    result[ord(i)-ord('a')] += 1

for j in range(26):
    if result[j] == max(result):
        print(chr(j+97), end='')