def solution(my_string, target):
    answer = my_string.find(target)
    answer = 0 if answer == -1 else 1
    return answer