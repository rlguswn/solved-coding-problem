t = int(input())

for h in range(t):
    r, s = input().split()
    result = ""
    for i in range(len(s) + 1):
        st = s[i-1:i]
        for j in range(int(r)):
            result = result + st
    print(result)
