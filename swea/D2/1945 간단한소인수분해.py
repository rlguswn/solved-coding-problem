t = int(input())

def func(r, n):
    result = 0
    d = r
    while(1):
        if n % d != 0:
            break
        result += 1
        d *= r
    return result

for i in range(t):
    arr = list()
    n = int(input())
    print(f'#{i+1} {func(2, n)} {func(3, n)} {func(5, n)} {func(7, n)} {func(11, n)}')
