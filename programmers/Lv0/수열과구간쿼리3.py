def solution(arr, queries):
    for i, j in queries:
        d = arr[i]
        arr[i] = arr[j]
        arr[j] = d
    return arr