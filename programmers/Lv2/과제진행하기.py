def solution(plans):
    answer = []
    stack = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x:x[1])
    
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        time = plans[i+1][1] - plans[i][1]
        
        while time and stack:
            playTime = stack[-1][1]
            if time >= playTime:
                time -= playTime
                answer.append(stack.pop()[0])
            else:
                stack[-1][1] -= time
                time = 0
    answer.append(plans[-1][0])
    while(stack):
        answer.append(stack.pop()[0])
    return answer