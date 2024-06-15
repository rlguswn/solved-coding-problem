def solution(str_list):
    l = str_list.index("l") if str_list.count("l") >= 1 else 21
    r = str_list.index("r") if str_list.count("r") >= 1 else 21
    answer = str_list[:l] if l < r else str_list[r+1:]
    return answer