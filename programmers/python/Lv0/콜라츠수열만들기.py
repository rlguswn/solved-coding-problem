def solution(n):
    answer = list()
    while(1):
        answer.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n*3+1
    return answer