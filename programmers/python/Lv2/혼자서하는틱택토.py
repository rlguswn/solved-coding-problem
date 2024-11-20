# board = ["O.X", ".O.", "..X"]

def calc(arr):
    c = 0
    for i in range(3):
        for j in range(2):
            if len([0 for a in arr if a[j] == i]) == 3:
                c+=1
    
    if len([0 for a in arr if a[0] == a[1]]) == 3:
        c+=1
    
    if (0,2) in arr and (1,1) in arr and (2,0) in arr:
        c+=1
        
    return c
            
def solution(board):
    check = {"O":[], "X":[]}
    
    for i, i_value in enumerate(board):
        for j, j_value in enumerate(i_value):
            if j_value != ".":
                check[j_value].append((i,j))
    
    d = len(check["O"]) - len(check["X"])
    o, x = calc(check["O"]), calc(check["X"])
    
    # O와 X의 숫자는 O가 1개 더 많거나 같아야함
    if not d in [0, 1]:
        return 0
    
    # O가 줄을 완성했음에도 X도 완성
    if o > 0 and x > 0:
        return 0
    
    # O가 이긴다면 O의 개수가 1개 더 많아야함
    if o > 0 and d != 1:
        return 0
    
    # X가 이긴다면 O와 X의 개수가 같아야함
    if x > 0 and d != 0:
        return 0
    
    return 1