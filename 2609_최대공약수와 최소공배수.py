import math

n1, n2 = map(int, input().split())

print(math.gcd(n1, n2))
print(math.lcm(n1, n2))

# n = list(map(int, input().split()))
# mi = 0
# ma = n[0] * n[1]

# for i in range(1, min(n)):
#     if n[0] % i == 0 and n[1] % i == 0 and mi < i:
#         mi = i

# for i in range(max(n), n[0] * n[1]):
#     if i % n[0] == 0 and i % n[1] == 0:
#         ma = i
#         break

# print(mi)
# print(ma)