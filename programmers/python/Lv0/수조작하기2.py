def solution(numLog):
    answer = ""
    for i in range(len(numLog)-1):
        d = numLog[i+1] - numLog[i]
        if d == 1:
            answer += "w"
        elif d == -1:
            answer += "s"
        elif d == 10:
            answer += "d"
        elif d == -10:
            answer += "a"
    return answer