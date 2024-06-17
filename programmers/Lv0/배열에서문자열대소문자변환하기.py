def solution(strArr):
    length = len(strArr)
    answer = [0 for _ in range(length)]
    for i in range(length):
        if i % 2 == 0:
            answer[i] = strArr[i].lower()
        else:
            answer[i] = strArr[i].upper()
    return answer