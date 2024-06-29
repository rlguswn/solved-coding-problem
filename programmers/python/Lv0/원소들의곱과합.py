def solution(num_list):
    m = 1
    for i in num_list:
        m *= i
    s = (sum(num_list))**2
    if m > s:
        return 0
    return 1