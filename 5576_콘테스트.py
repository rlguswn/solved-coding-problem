import sys

w = list()
k = list()

for i in range(10):
    w.append(int(sys.stdin.readline()))

for j in range(10):
    k.append(int(sys.stdin.readline()))

w.sort(reverse=True)
k.sort(reverse=True)

print(w[0] + w[1] + w[2], k[0] + k[1] + k[2])