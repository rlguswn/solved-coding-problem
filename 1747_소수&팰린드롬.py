import sys

def checkPrime(x):
    for i in range(2, int(n/2)+1):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
result = 0

for i in range(n, 2000001):
    if i==1:
        continue
    if str(i) == str(i)[::-1]:
        if checkPrime(i) == True:
            result = i
            break

print(result)