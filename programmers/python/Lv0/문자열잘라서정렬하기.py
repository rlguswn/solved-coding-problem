def solution(myString):
    answer = sorted(list(filter(lambda x:x!="", myString.split("x"))))
    return answer