n = int(input())
s = int(n/1000) + int(n%1000/100) + int(n%100/10) + int(n%10)
print(s)