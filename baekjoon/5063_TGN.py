n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    t = "advertise" if r < e - c else "does not matter" if r == e - c else "do not advertise"
    print(t)
