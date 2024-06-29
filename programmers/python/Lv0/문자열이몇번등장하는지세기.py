def solution(myString, pat):
    start = 0
    answer = 0
    while(1):
        i = myString.find(pat, start)
        if i == -1:
            break
        start = i + 1
        answer += 1
    return answer