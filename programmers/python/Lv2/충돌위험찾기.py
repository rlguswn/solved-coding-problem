# points = [[3, 2], [6, 4], [4, 7], [1, 4]]
# 운송 포인트의 좌표를 담은 정수배열
# routes = [[4, 2], [1, 3], [2, 4]]
# 로봇의 운송 경로를 담은 정수배열

def getPath(point, route):
    x, y = point[route[0]]
    path = [(x,y)]
    
    for i in range(1, len(route)):
        x2, y2 = point[route[i]]
        dx, dy = 0, 0
        
        if x!=x2:
            dx = 1 if x < x2 else -1
            while(x!=x2):
                x+=dx
                path.append((x,y))
        if y!=y2:
            dy = 1 if y < y2 else -1
            while(y!=y2):
                y+=dy
                path.append((x,y))
        
    return path

def solution(points, routes):
    answer = 0
    path = [0 for i in routes]
    point = {i+1: v for i, v in enumerate(points)}
    
    for i, r in enumerate(routes):
        path[i] = getPath(point, r)
    
    max_len = max(map(len, path))
    for i in range(max_len):
        row = []
        for j in range(len(path)):
            if i < len(path[j]):
                row.append(path[j][i])
        
        row2 = set(row)
        if len(row)!=len(row2):
            for j in row2:
                if row.count(j) >= 2:
                    answer+=1
    
    return answer