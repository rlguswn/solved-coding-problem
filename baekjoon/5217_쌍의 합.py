import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = list()
    for i in range(1, n//2+n%2):
        if n > i and i*2 < n:
            result.append(f'{i} {n-i}')
    print(f'Pairs for {n}: ', end='')
    print(', '.join(result))