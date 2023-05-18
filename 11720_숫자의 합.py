n = int(input())

number = input()
numbers = list()

for i in range(n):
    numbers.append(number[i:i+1])
    
print(sum(map(int, numbers)))