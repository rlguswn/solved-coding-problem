def solution(myString, pat):
    s = ""
    for i in myString:
        if i == "A":
            s += "B"
        elif i == "B":
            s += "A"
    answer = s.find(pat)
    if answer == -1:
        answer = 0
    else:
        answer = 1
    return answer