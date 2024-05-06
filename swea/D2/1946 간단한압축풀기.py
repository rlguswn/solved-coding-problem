t = int(input())
for i in range(t):
    n = int(input())
    result = ""
    for _ in range(n):
        s, m = input().split()
        result += s*int(m)
    print(f'#{i+1} ')
    for j in range(int(len(result) / 10) + 1):
        print(result[j*10:j*10+10])
