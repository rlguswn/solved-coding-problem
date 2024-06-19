def solution(arr1, arr2):
    length1, length2 = len(arr1), len(arr2)
    sum1, sum2 = sum(arr1), sum(arr2)
    if length1 != length2:
        answer = 1 if length1 > length2 else -1
    elif sum1 != sum2:
        answer = 1 if sum1 > sum2 else -1
    else:
        answer = 0
    return answer