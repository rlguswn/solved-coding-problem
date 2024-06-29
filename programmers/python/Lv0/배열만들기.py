def solution(l, r):
    d = 1
    answer = list()
    while(int(str(bin(d))[2:]) * 5 <= r):
        if int(str(bin(d))[2:]) * 5 >= l:
            answer.append(int(str(bin(d))[2:]) * 5)
        d += 1
        print(d)
    if len(answer) == 0:
        answer.append(-1)
    return answer