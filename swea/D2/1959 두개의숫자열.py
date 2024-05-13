t = int(input())

def func(arr1, arr2):
    n = 0
    for i in range(len(arr1) - len(arr2) + 1):
        sum = 0
        for j in range(len(arr2)):
            sum = sum + (arr1[j+i] * arr2[j])
        if n < sum:
            n = sum
    return n

for i in range(t):
    la, lb = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    if la > lb:
        result = func(arr_a, arr_b)
    else:
        result = func(arr_b, arr_a)

    print(f'#{i+1} {result}')