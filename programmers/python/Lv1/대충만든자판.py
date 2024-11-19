# keymap = ["ABACD", "BCEFD"]
# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열
# targets = ["ABCD","AABB"]
# 입력하려는 문자열들이 담긴 문자열배열

def solution(keymap, targets):
    answer = [0 for i in targets]
    num = dict()
    
    for i in keymap:
        for j, v in enumerate(i):
            if v in num.keys():
                num[v] = num[v] if num[v] < j+1 else j+1
                continue
            num[v] = j+1
    
    for i, v in enumerate(targets):
        for j in v:
            if j in num.keys():
                answer[i] += num[j]
                continue
            answer[i] = -1
            break
        
    return answer