def solution(my_string, s, e):
    answer = list(my_string)
    st = reversed(answer[s:e+1])
    answer[s:e+1] = st
    answer = ''.join(answer)
    return answer