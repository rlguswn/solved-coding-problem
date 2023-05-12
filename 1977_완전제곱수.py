m = int(input())
n = int(input())
result = list()

for i in range(m, n+1):
    if i**0.5 == int(i**0.5):
        result.append(i)

try:
    print(sum(result), min(result))
except:
    print(-1)