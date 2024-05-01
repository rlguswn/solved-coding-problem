n = int((int(input()) - 1) / 2)
p = list(map(int, input().split()))
p.sort()
print(p[n])