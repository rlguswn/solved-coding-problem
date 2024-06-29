def solution(binomial):
    calc = binomial.split()
    if calc[1] == "+":
        answer = int(calc[0]) + int(calc[2])
    elif calc[1] == "-":
        answer = int(calc[0]) - int(calc[2])
    elif calc[1] == "*":
        answer = int(calc[0]) * int(calc[2])
    return answer