# today = "2022.05.19"
# 오늘 날짜는 의미하는 문자열
# terms = ["A 6", "B 12", "C 3"]
# 약관 타입과 약관의 유효기간
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# 파기해야 할 개인정보
# 모든 달은 28일까지 있다고 가정

def strToDate(s):
    year, month, date = map(int, s.split("."))
    return (year*12 + month)*28 + date

def solution(today, terms, privacies):
    answer = []
    today_date = strToDate(today)
    dday = dict()
    
    for i in terms:
        t, m = i.split()
        dday[t] = today_date - (int(m)*28)
        
    for i, v in enumerate(privacies):
        p_day, p_type = v.split()
        if strToDate(p_day) <= dday[p_type]:
            answer.append(i+1)
    
    return answer