import sys

n = int(sys.stdin.readline())
f = 1
result = 0

if n != 0:
    for i in range(1, n+1):
        f *= i
    for j in ''.join(reversed(str(f))):
        if j == '0':
            result += 1
        else:
            print(result)
            break
else:
    print(0)