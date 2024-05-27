t = int(input())

def hit(col, row, size):
    sum = 0
    for i in range(size):
        for j in range(size):
            sum += arr[col+i][row+j]
    return sum

for i in range(t):
    n, m = map(int, input().split())
    arr = [0 for _ in range(n)]
    result = 0
    for j in range(n):
        arr[j] = list(map(int, input().split()))
    for k in range(n-m+1):
        for l in range(n-m+1):
            bug = hit(k, l, m)
            if bug > result:
                result = bug
    print(f'#{i+1} {result}')
