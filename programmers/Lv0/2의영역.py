def solution(arr):
    answer = []
    cnt = arr.count(2)
    if cnt >= 2:
        for i in range(arr.index(2), len(arr)):
            if cnt != 0:
                answer.append(arr[i])
            if arr[i] == 2:
                cnt -= 1
    elif cnt == 1:
        answer.append(2)
    else:
        answer.append(-1)
    return answer