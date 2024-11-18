# n = 8
# n 미터의 벽
# m = 4
# 한번에 페인트를 칠하는 범위 m
# section = [2, 3, 6]
# 다시 페인트를 칠하는 구역

def solution(n, m, section):
    answer = 0
    prev = -m-1
    
    for i in section:
        if i >= prev+m:
            answer+=1
            prev = i
    
    return answer