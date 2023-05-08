dice = input().split()

for i in range(1, 7):
    if dice.count(str(i)) == 3:
        reward = 10000 + 1000 * i
        break
    elif dice.count(str(i)) == 2:
        reward = 1000 + 100 * i
        break
    elif dice.count(str(i)) == 1:
        reward = 100 * i

print(reward)