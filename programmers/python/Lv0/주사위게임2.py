def solution(a, b, c):
    d = int(a==b) + int(b==c) + int(c==a)
    if d == 0:
        return a+b+c
    elif d == 1:
        return (a+b+c)*(a**2+b**2+c**2)
    elif d == 3:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)