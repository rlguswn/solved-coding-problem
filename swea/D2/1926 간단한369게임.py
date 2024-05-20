n = int(input())
rule = {3, 6, 9}

def func(number, rule_number):
    d = 1
    cnt = 0
    for i in range(len(str(number))):
        if number % (d*10) // d in rule_number:
            cnt += 1
        d *= 10
    if cnt != 0:
        return '-' * cnt
    return number

for i in range(n):
    print(func(i+1, rule), end=' ')