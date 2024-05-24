t = int(input())
for i in range(t):
    length = int(input())
    number = list(map(int, input().split()))
    result, max_num = 0, 0
    for j in range(length-1, -1, -1):
        if number[j] > max_num:
            max_num = number[j]
        else:
            result = result + max_num - number[j]
    print(f'#{i+1} {result}')