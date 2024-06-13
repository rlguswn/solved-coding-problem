def solution(num_list):
    e = ''
    o = ''
    for i in num_list:
        if i % 2 == 0:
            e += str(i)
        elif i % 2 == 1:
            o += str(i)
    answer = int(e) + int(o)
    return answer