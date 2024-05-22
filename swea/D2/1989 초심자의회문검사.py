t = int(input())
for i in range(t):
    s = list(input())

    s1 = ''.join(s)
    s.reverse()
    s2 = ''.join(s)
    print(f'#{i+1} {int(s1==s2)}')
