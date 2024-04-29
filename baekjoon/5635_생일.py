n = int(input())
l_name = list()
l_birth = list()

def f(x):
    if len(x) == 1:
        return '0' + x
    else:
        return x

for i in range(n):
    name, day, month, year = input().split()
    l_name.append(name)
    l_birth.append(year + f(month) + f(day))
    li = list(zip(l_name, l_birth))

print(sorted(li, key=lambda x:x[1])[len(li)-1][0])
print(sorted(li, key=lambda x:x[1])[0][0])
    