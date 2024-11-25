# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# S:시작지점, E:출구, L:레버, O:통로, X:벽

from collections import deque

def solution(maps):
    answer = 0
    visited = [[float("inf") for i in maps[0]] for j in maps]
    queue = deque()
    height, width = len(maps), len(maps[0])
    
    for i, i_value in enumerate(maps):
        for j, j_value in enumerate(i_value):
            if j_value == "S":
                visited[i][j] = 0
                queue.append((i,j,0))
            elif j_value == "L":
                lever = (i,j)
                door = False
            elif j_value == "E":
                target = (i,j)
    
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while(queue):
        x,y,c = queue.popleft()
        
        if (x,y) == lever and not(door):
            queue = deque()
            visited = [[float("inf") for i in maps[0]] for j in maps]
            visited[x][y] = c
            door = True
        
        if (x,y) == target and door:
            return c
        
        for dx, dy in d:
            nx = x
            ny = y
            
            if 0<=nx+dx<height and 0<=ny+dy<width and maps[nx+dx][ny+dy]!="X":
                nx+=dx
                ny+=dy

                if visited[nx][ny] > c+1:
                    visited[nx][ny] = c+1
                    queue.append((nx,ny,c+1))
    
    return -1