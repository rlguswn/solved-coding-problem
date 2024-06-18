def solution(myStr):
    answer = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split(" ")
    answer = list(filter(lambda x:x!="", answer))
    if not(answer):
        answer.append("EMPTY")
    return answer