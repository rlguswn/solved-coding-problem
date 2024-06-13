def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            num = d*i + a
            answer += num
    return answer