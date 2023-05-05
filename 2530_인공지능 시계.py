h, m, s = map(int, input().split())
add_time = int(input())

s1 = (s + add_time) % 60
m1 = (m + ((s + add_time) // 60)) % 60
h1 = (h + ((m + ((s + add_time) // 60)) // 60)) % 24

print(h1, m1, s1)