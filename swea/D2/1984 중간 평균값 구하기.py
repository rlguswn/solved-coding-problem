t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    arr.sort()
    avg = round(sum(arr) / len(arr))
    print(f'#{i+1} {avg}')