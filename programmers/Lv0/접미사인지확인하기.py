def solution(my_string, is_suffix):
    l = len(is_suffix)
    if my_string[-l:] == is_suffix:
        return 1
    return 0