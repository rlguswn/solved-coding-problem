def solution(a, b):
    ab = int(str(a) + str(b))
    calc = 2 * a * b
    answer = ab if ab > calc else calc
    return answer