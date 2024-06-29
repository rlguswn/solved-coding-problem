def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        n = int(intStrs[i][s:s+l])
        if n > k:
            answer.append(n)
    return answer