p, k = map(int, input().split())

result = p - k + 1
if result <= 0:
    result += 1000
print(result)