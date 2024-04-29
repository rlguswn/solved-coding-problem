import sys

vowel = ['a', 'e', 'i', 'o', 'u']

while(1):
    sum = 0
    s = sys.stdin.readline().rstrip().lower()
    if s == '#':
        break
    for i in vowel:
        sum += s.count(i)
    print(sum)