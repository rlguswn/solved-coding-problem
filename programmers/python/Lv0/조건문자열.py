def solution(ineq, eq, n, m):
    if ineq == ">":
        answer1 = n > m
    elif ineq == "<":
        answer1 = n < m
    if eq == "=":
        answer2 = n == m
    elif eq == "!":
        answer2 = 0
    answer = int(answer1 or answer2)
    return answer