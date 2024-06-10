tc = int(input())
for i in range(tc):
    n = int(input())
    result = 0
    for j in range(n):
        result += int((n**2 - j**2)**0.5)
    print(f'#{i+1} {result*4+1}')
    