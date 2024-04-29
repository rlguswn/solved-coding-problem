import sys

t = int(sys.stdin.readline())

for i in range(t):
    s = sys.stdin.readline().strip()

    print(s[0]+s[-1])