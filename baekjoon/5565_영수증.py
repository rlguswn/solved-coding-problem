total_money = int(input())
price = list()

for i in range(9):
    price.append(int(input()))

print(total_money - sum(price))