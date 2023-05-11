t = int(input())

for i in range(t):
    str = input()
    result = 0
    for j in range(len(str)):
        if str[j] == 'O':
            if str[j-1] == 'X' or j == 0:
                point = 1
                result += point
            else:
                point += 1
                result += point
    print(result)