def solution(str1, str2):
    answer = str2.find(str1)
    answer = 0 if answer == -1 else 1
    return answer