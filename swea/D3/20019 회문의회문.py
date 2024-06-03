t = int(input())

def func(str):
    n = len(str)
    m = int((n-1)/2)
    for j in range(n):
        if str[j] != str[j-n]:
            return "NO"
    if str[:m] != str[m+1:]:
        return "NO"
    return "YES"

for i in range(t):
    s = input()
    print(f'#{i+1} {func(s)}')
