def solution(arr, queries):
    answer = list()
    for s, e, k in queries:
        d = 1000001
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < d:
                d = arr[i]
        if d == 1000001:
            d = -1
        answer.append(d)
    return answer