def solution(myString, pat):
    s = myString.lower()
    p = pat.lower()
    answer = 1 if p in s else 0
    return answer