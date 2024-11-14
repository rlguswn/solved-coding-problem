park = 	["OSO", "OOO", "OXO", "OOO"] # 공원을 나타내는 문자열 배열
routes = ["E 2", "S 3", "W 1"] # 로봇 강아지가 수행할 명령이 담긴 문자열 배열
# N:위쪽 S:아래쪽 W:왼쪽 E오른쪽

def move(direction, distance, x, y, park_x, park_y, stop):
    dx = x
    dy = y

    if direction == "N":
        for i in range(distance):
            if [dx-1, dy] in stop or dx-1 < 0:
                return x, y
            dx -= 1
    
    elif direction == "S":
        for i in range(distance):
            if [dx+1, dy] in stop or dx+1 >= park_x:
                return x, y
            dx += 1
    
    elif direction == "W":
        for i in range(distance):
            if [dx, dy-1] in stop or dy-1 < 0:
                return x, y
            dy -= 1
    
    elif direction == "E":
        for i in range(distance):
            if [dx, dy+1] in stop or dy+1 >= park_y:
                return x, y
            dy += 1

    return dx, dy

def solution(park, routes):
    park_x = len(park)
    park_y = len(park[0])
    stop = []

    for i in range(park_x):
        for j in range(park_y):
            if park[i][j] == "S":
                answer = [i, j]
            if park[i][j] == "X":
                stop.append([i, j])

    for i in routes:
        direction, distance = i.split()
        distance = int(distance)

        answer = move(direction, distance, answer[0], answer[1], park_x, park_y, stop)
    
    return answer

print(solution(park, routes))