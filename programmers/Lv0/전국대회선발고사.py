def solution(rank, attendance):
    student = []
    cnt = 3
    for i in range(1, len(rank)+1):
        if attendance[rank.index(i)]:
            cnt -= 1
            student.append(rank.index(i))
        if cnt == 0:
            break
    answer = (student[0]*10000) + (student[1]*100) + student[2]
    return answer