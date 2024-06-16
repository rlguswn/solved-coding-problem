def solution(num_list):
    d = list(filter(lambda x:x < 0, num_list))
    if not(d):
        return -1
    return num_list.index(d[0])