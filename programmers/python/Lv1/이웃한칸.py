board = [["blue", "red", "orange", "red"], 
         ["red", "red", "blue", "orange"], 
         ["blue", "orange", "red", "red"], 
         ["orange", "orange", "red", "blue"]]
h = 1
w = 1

def check(board, h, w, color):
    if board[h][w] == color:
        return 1
    return 0

def solution(board, h, w):
    answer = 0
    color = board[h][w]
    height = len(board)
    width = len(board[0])

    if h+1 < height:
        answer += check(board, h+1, w, color)

    if h-1 >= 0:
        answer += check(board, h-1, w, color)

    if w+1 < width:
        answer += check(board, h, w+1, color)

    if w-1 >= 0:
        answer += check(board, h, w-1, color)

    return answer

print(solution(board, h, w))