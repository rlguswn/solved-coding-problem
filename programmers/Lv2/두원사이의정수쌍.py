def solution(r1, r2):
    answer = 0
    for i in range(r2):
        cnt = int((r2**2 - i**2)**0.5) - int(max(0, (r1**2-i**2)-1)**0.5)
        answer+=cnt
    answer *= 4
    return answer