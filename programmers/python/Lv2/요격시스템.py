def solution(targets):
    answer = 0
    sorted_targets = sorted(list(targets), key = lambda x:x[1])
    e = 0
    
    for ts, te in sorted_targets:
        if ts >= e:
            e = te
            answer+=1
    
    return answer