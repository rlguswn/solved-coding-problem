t = int(input())

def func(str, pattern):
    cnt = 0
    for i in range(int(len(str) / len(pattern))):
        if pattern != str[i*len(pattern):(i+1)*len(pattern)]:
            return 0
        cnt += 1
    return cnt

for i in range(t):
    s = input()
    p = s[0]
    for j in range(10):
        result = func(s, p)
        if result == 0:
            p += s[j+1]
            continue
    print(f'#{i+1} {len(p)}')