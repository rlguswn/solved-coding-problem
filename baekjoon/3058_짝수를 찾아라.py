import sys

t = int(sys.stdin.readline())

for i in range(t):
    sum = 0
    min = 101
    n = list(map(int, sys.stdin.readline().split()))
    for j in n:
        if j % 2 == 0:
            sum += j
            if j < min:
                min = j
    print(sum, min)