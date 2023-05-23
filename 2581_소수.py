import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

result_sum = 0
result_min = 10000

for i in range(m, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            result_sum += i
            if result_min > i:
                result_min = i

if result_sum == 0:
    print(-1)
else:
    print(result_sum)
    print(result_min)