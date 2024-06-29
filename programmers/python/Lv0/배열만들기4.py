def solution(arr):
    stk = [arr[-1]]
    l = len(arr)
    for i in range(l-1, -1, -1):
        if stk[0] > arr[i]:
            stk.insert(0, arr[i])
    return stk