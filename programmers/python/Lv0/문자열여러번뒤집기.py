def solution(my_string, queries):
    answer = list(my_string)
    for i, j in queries:
        s = reversed(answer[i:j+1])
        answer[i:j+1] = s
    answer = ''.join(answer)
    return answer