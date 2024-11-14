# name = ["may", "kein", "kain", "radi"] 그리워하는 사람의 이름 배열
# yearning = [5, 10, 1, 3] 사람별 그리움 점수 배열
# photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# 사진들에 찍힌 인물의 이름 배열

def solution(name, yearning, photo):
    answer = []
    n = {v: i for i, v in enumerate(name)}
    
    for i in photo:
        s = 0
        for j in i:
            if j in name:
                s += yearning[n[j]]
        
        answer.append(s)
        
    return answer