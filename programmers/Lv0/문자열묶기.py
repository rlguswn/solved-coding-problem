def solution(strArr):
    answer = []
    arr = list(map(len, strArr))
    n_list = list(set(arr))
    for i in n_list:
        answer.append(arr.count(i))
    return max(answer)