def solution(my_string):
    answer = list(filter(lambda x:x!="", my_string.split(" ")))
    return answer