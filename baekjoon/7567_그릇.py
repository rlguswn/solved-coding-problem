bowl = input()
h = 0

for i in range(len(bowl)):
    if bowl[i-1:i] != bowl[i:i+1]:
        h += 10
    else:
        h += 5

print(h)