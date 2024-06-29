def solution(str_list, ex):
    answer = ''.join(filter(lambda x:x.find(ex)==-1, str_list))
    return answer