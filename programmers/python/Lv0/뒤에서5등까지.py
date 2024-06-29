def solution(num_list):
    answer = sorted(num_list)
    while(len(answer)!=5):
        answer.pop(-1)
    return answer