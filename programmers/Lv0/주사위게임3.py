def solution(a, b, c, d):
    dice = [0 for _ in range(6)]
    dice[a-1] += 1
    dice[b-1] += 1
    dice[c-1] += 1
    dice[d-1] += 1
    if 4 in dice:
        answer = (dice.index(4)+1) * 1111
    elif 3 in dice:
        answer = ((dice.index(1)+1) + ((dice.index(3)+1) * 10))**2
    elif 2 in dice:
        if 1 in dice:
            p, q = [(i+1) for i, value in enumerate(dice) if value == 1]
            answer = p * q
        else:
            p, q = [(i+1) for i, value in enumerate(dice) if value == 2]
            answer = (p+q) * abs(p-q)
    else:
        answer = dice.index(1) + 1
    return answer