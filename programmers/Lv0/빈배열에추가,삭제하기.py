def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            d = arr[i]
            answer.extend([arr[i] for _ in range(arr[i]*2)])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer