# x, y, n = 10, 40, 5
# x를 y로 변환
# 사용 가능한 연산 : x+=n, x*2, x*3

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque()
    queue.append((x,0))
    visited = [False] * y
    
    while(queue):
        dx, c = queue.popleft()
        
        for i in [dx+n, dx*2, dx*3]:
            if i < y and not(visited[i]):
                queue.append((i,c+1))
                visited[i] = True
            elif i == y:
                return c+1
    return -1