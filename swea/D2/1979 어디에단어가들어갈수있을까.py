t = int(input())

def check_w(arr1):
    word = list()
    cnt = 0
    for i in range(len(arr1)):
        if arr1[i] == 1:
            cnt += 1
        if cnt > 0 and (arr1[i] == 0 or i == len(arr1) - 1):
            word.append(cnt)
            cnt = 0
    return word

def check_h(arr2, x):
    word = list()
    cnt = 0
    for i in range(len(arr2)):
        if arr2[i][x] == 1:
            cnt += 1
        if cnt > 0 and (arr2[i][x] == 0 or i == len(arr2) - 1):
            if cnt > 1:
                word.append(cnt)
            cnt = 0
    return word

for i in range(t):
    n, k = map(int, input().split())
    result = 0
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    for j in range(n):
        result += check_w(puzzle[j]).count(k)
        result += check_h(puzzle, j).count(k)
        
    print(f'#{i+1} {result}')