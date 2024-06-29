def solution(num_list):
    d = num_list[-1] - num_list[-2]
    answer = num_list
    if d > 0:
        answer.append(d)
    else:
        answer.append(num_list[-1]*2)
    return answer