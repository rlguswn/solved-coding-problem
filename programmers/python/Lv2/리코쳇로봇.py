# board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
# .:빈칸 D:장애물 R:시작 G:도착

from collections import deque

def solution(board):
    answer = 0
    queue = deque()
    visited = [[float("inf") for i in range(len(board[0]))] for j in range(len(board))]
    height, width = len(board), len(board[0])
    
    for i, i_value in enumerate(board):
        if "R" in i_value:
            visited[i][i_value.index("R")] = 0
            queue.append((i, i_value.index("R"), 0))
        if "G" in i_value:
            target = [i, i_value.index("G")]
    
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while(queue):
        x,y,c = queue.popleft()
        
        if [x,y] == target:
            return c
        
        for dx, dy in d:
            n_x = x
            n_y = y
            
            while(0<=n_x+dx<height and 0<=n_y+dy<width and board[n_x+dx][n_y+dy]!="D"):
                n_x += dx
                n_y += dy
                
            if visited[n_x][n_y] > c+1:
                visited[n_x][n_y] = c+1
                queue.append((n_x,n_y,c+1))

    return -1