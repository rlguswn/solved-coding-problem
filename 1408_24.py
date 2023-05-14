h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

if s1 > s2:
    m2 -= 1
    s2 += 60

if m1 > m2:
    h2 -= 1
    m2 += 60

if h1 > h2:
    h2 += 24

h = str(h2 - h1)
m = str(m2 - m1)
s = str(s2 - s1)

def f(x):
    if len(x) == 1:
        x = '0' + x
    return x

print(f'{f(h)}:{f(m)}:{f(s)}')