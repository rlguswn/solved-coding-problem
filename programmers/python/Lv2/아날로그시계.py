def solution(h1, m1, s1, h2, m2, s2):
    time = (h1 * 60 * 60) + (m1 * 60) + s1
    end = (h2 * 60 * 60) + (m2 * 60) + s2
    answer = 1 if time == 0 or time == 3600 * 12 else 0
    
    for i in range(time, end):
        h = i / 120 % 360
        m = i / 10 % 360
        s = i * 6 % 360
        
        next_h = 360 if (i+1) / 120 % 360 == 0 else (i+1) / 120 % 360
        next_m = 360 if (i+1) / 10 % 360 == 0 else (i+1) / 10 % 360
        next_s = 360 if (i+1) * 6 % 360 == 0 else (i+1) * 6 % 360
        
        if s < h and next_s >= next_h:
            answer+=1
        if s < m and next_s >= next_m:
            answer+=1
        if next_s == next_m == next_h:
            answer-=1
            
    return answer