def solution(my_string, m, c):
    answer = ''
    n = c-1
    while(n < len(my_string)):
        answer+=my_string[n]
        n+=m
    return answer