tc = int(input())
for i in range(tc):
    n = int(input())
    r = 0
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            r = j
    if r == 0:
        r = n - 1
    result = r + n//r - 2
    print(f'#{i+1} {result}')