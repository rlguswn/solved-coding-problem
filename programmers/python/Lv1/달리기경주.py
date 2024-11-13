#7시15분

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    answer = players
    rank = {v: i for i, v in enumerate(players)}

    for i in callings:
        r = rank[i]
        previous = answer[r-1]
        current = answer[r]
        
        answer[r-1] = current
        answer[r] = previous

        rank[current] -= 1
        rank[previous] += 1

    return answer

print(solution(players, callings))