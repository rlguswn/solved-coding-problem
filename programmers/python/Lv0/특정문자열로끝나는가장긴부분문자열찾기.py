import re

def solution(myString, pat):
    p = re.compile(f'.*{pat}')
    answer = p.match(myString)
    return answer.group()