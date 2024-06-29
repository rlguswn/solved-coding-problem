def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if strArr[i].find("ad") == -1:
            answer.append(strArr[i])
    return answer