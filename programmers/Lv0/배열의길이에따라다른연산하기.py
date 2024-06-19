def solution(arr, n):
    answer = arr
    length = len(answer)
    for i in range(int(not(length%2)), length, 2):
        answer[i] += n
    return answer