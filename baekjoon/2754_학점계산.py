t = input()

def f(x):
    if t[1:] == '+':
        print(x + 0.3)
    elif t[1:] == '0':
        print(x)
    elif t[1:] == '-':
        print(x - 0.3)

if t[:1] == 'A':
    f(4.0)
elif t[:1] == 'B':
    f(3.0)
elif t[:1] == 'C':
    f(2.0)
elif t[:1] == 'D':
    f(1.0)
elif t[:1] == 'F':
    print(0.0)
