# wallpaper = [".#...", "..#..", "...#."]
# 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열

def solution(wallpaper):
    answer = []
    file_x = []
    file_y = []
    height = len(wallpaper)
    width = len(wallpaper[0])
    
    for i in range(height):
        for j in range(width):
            if wallpaper[i][j] == "#":
                file_x.append(i)
                file_y.append(j)
                
    answer.append(min(file_x))
    answer.append(min(file_y))
    answer.append(max(file_x)+1)
    answer.append(max(file_y)+1)
    
    return answer