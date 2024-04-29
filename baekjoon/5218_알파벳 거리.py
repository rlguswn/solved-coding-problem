import sys

t = int(sys.stdin.readline())

for i in range(t):
    d = 'Distances:'
    s1, s2 = sys.stdin.readline().split()

    for j in range(len(s1)):
        distance = ord(s2[j]) - ord(s1[j])
        if distance < 0:
            distance += 26
        d += f' {distance}'
    print(d)