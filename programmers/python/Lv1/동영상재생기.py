def getTime(time_str):
    m = int(time_str[0:2])
    s = int(time_str[3:5])
    return m*60 + s

def opPass(start, end, now):
    if start <= now and end >= now:
        return end
    return now

def toText(time_int):
    m = str(time_int//60) if time_int//60 >= 10 else "0" + str(time_int//60)
    s = str(time_int%60) if time_int%60 >= 10 else "0" + str(time_int%60)
    return f"{m}:{s}"

def solution(video_len, pos, op_start, op_end, commands):
    total_s = getTime(video_len)
    op_start_s = getTime(op_start)
    op_end_s = getTime(op_end)
    time = getTime(pos)
    
    time = opPass(op_start_s, op_end_s, time)
    for s in commands:
        if s == "prev":
            time -= 10
            if time < 0:
                time = 0
        
        elif s == "next":
            time += 10
            if time > total_s:
                time = total_s
        
        time = opPass(op_start_s, op_end_s, time)
    answer = toText(time)
    return answer