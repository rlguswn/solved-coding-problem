# maps = ["X591X","X1X5X","X231X", "1XXX1"]
# X 또는 1~9 의 자연수로 이루어진 문자열 배열

def bfs(maps,visited,location):
    queue = [location]
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    s = 0
    
    while(queue):
        x,y,c = queue.pop()
        
        if visited[x][y]:
            continue
            
        visited[x][y] = True
        s+=c
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]!="X" and not(visited[nx][ny]):
                queue.append((nx,ny,int(maps[nx][ny])))

    return s

def solution(maps):
    answer = []
    visited = [[False for i in maps[0]] for j in maps]
    queue = []
    
    for i, i_value in enumerate(maps):
        for j, j_value in enumerate(i_value):
            if j_value!="X":
                queue.append((i,j,int(maps[i][j])))
    
    while(queue):
        s = bfs(maps,visited,queue.pop())
        
        if s!=0:
            answer.append(s)
    
    if answer:
        answer.sort()
        return answer
    
    return [-1]