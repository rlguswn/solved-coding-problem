t = int(input())

for j in range(t):
    arr = input().split()
    arr[0] = float(arr[0])
    for i in range(len(arr)):
        if arr[i] == "@":
            arr[0] *= 3
        elif arr[i] == "%":
            arr[0] += 5
        elif arr[i] == "#":
            arr[0] -= 7

    print(f'{arr[0]:.2f}')
