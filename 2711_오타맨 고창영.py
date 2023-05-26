import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, w = sys.stdin.readline().split()
    n = int(n)
    print(w[0:n-1]+w[n:len(w)])
