# m, n = 10, 10
# 당구대의 가로, 세로길이
# startX, startY = 3, 7
# 공이 놓인 위치
# balls=[[7, 7], [2, 7], [7, 3]]
# 목표로 해야하는 공들의 위치

def solution(m, n, startX, startY, balls):
    answer = []
    l = 2*(m**2 + n**2)
    
    for x, y in balls:
        arr = []
        # 왼쪽
        if not (startX>x and startY==y):
            arr.append((startX+x)**2 + (startY-y)**2)
        # 오른쪽
        if not (startX<x and startY==y):
            arr.append((2*m-startX-x)**2 + (startY-y)**2)
        # 위쪽
        if not (startX==x and startY>y):
            arr.append((startX-x)**2 + (startY+y)**2)
        # 아래쪽
        if not (startX==x and startY<y):
            arr.append((startX-x)**2 + (2*n-startY-y)**2)
        
        answer.append(min(arr))
    
    return answer