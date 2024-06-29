def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if not(arr[i] in answer):
            answer.append(arr[i])
        if len(answer) == k:
            break
    while(1):
        empty = k - len(answer)
        if empty == 0:
            break
        answer.append(-1)
    return answer