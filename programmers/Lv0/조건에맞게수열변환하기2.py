def solution(arr):
    answer = arr
    cnt = 0
    while(1):
        check = 0
        for i in range(len(answer)):
            if answer[i] >= 50 and answer[i] % 2 == 0:
                answer[i] = int(answer[i] / 2) + 1
            elif answer[i] < 50 and answer[i] % 2 == 1:
                answer[i] = answer[i] * 2 + 1
            else:
                check += 1
        if check == len(answer):
            return cnt
        cnt += 1