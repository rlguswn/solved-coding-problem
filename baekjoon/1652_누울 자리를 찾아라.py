import sys

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]
count = [0, 0]

for i in range(n):
    length = [0, 0]
    for j in range(n):
        if l[i][j] == ".":
            length[0] += 1
        else:
            length[0] = 0
        if length[0] == 2:
            count[0] += 1

        if l[j][i] == ".":
            length[1] += 1
        else:
            length[1] = 0
        if length[1] == 2:
            count[1] += 1

print(count[0], count[1])