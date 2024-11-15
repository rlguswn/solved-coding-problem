# diffs = [1, 5, 3]
# 퍼즐의 난이도 정수배열
# times = [2, 4, 7]
# 퍼즐의 소요 시간 정수배열
# limit = 30
# 전체 제한시간
# diff <= level 이면 time만큼 소요
# diff > level 이면 퍼즐을 총 diff - level만큼 틀림 time + time_prev만큼 소요

def calc(dif, time, level):
    total = 0
    time_prev = 0
    for i in range(len(dif)):
        if level >= dif[i]:
            total += time[i]
        else:
            r = dif[i] - level
            total = total + (time[i]*(r+1)) + (time_prev*r)
        time_prev = time[i]
    return total

def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    answer_prev = 0
    
    while(1):
        answer = (start+end)//2
        if answer_prev == answer:
            break
        time = calc(diffs, times, answer)
        print(f"{answer}:{time}")
        if time <= limit:
            end = answer
        elif time > limit:
            start = answer + 1
        answer_prev = answer

    return answer