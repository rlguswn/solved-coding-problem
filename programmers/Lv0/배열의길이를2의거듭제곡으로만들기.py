def solution(arr):
    answer = arr
    length = len(answer)
    d = 1
    while(length > d):
        d *= 2
    for i in range(d - length):
        answer.append(0)
    return answer