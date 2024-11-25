# book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# 예약시간이 문자열 형태로 담긴 배열

def strToTime(s):
    h, m = map(int, s.split(":"))
    return h*60+m

def solution(book_time):
    answer = [0]
    time = [[strToTime(i[0]), strToTime(i[1])+10] for i in book_time]
    time.sort(key=lambda x:x[0], reverse=True)
    
    while(time):
        start_t, end_t = time.pop()
        
        for i in range(len(answer)):
            if answer[i] <= start_t:
                answer[i] = end_t
                break
            elif i == len(answer)-1:
                answer.append(end_t)
    
    return len(answer)