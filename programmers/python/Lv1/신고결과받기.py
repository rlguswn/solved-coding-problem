id_list = ["muzi", "frodo", "apeach", "neo"]
# 이용자의 ID가 담긴 문자열 배열
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열(동일 신고는 1회로 처리)
k = 2 # 정지기준(k번 이상 신고당하면 정지)

def solution(id_list, report, k):
    answer = [0 for i in id_list]
    r = list(set(report))
    ban = [0 for i in id_list]
    name = {v: i for i, v in enumerate(id_list)}
    
    for i in r:
        send, receive = i.split()
        ban[name[receive]] += 1
    
    ban = [i for i, v in enumerate(ban) if v >= k]
    
    for i in r:
        send, receive = i.split()
        if name[receive] in ban:
            answer[name[send]] += 1
    
    return answer

print(solution(id_list, report, k))