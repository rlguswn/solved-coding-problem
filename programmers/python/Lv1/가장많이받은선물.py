friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

def solution(friends, gifts):
    f = {value: i for i, value in enumerate(friends)}
    l = len(friends)
    p = [0 for i in range(l)]
    answer = [0 for i in range(l)]
    count = [[0 for i in range(l)] for j in range(l)]

    for i in gifts:
        send, receive = i.split()
        count[f[send]][f[receive]] += 1
        count[f[receive]][f[send]] -= 1
    
    for i in range(l):
        p[i] = sum(count[i])

    for i in range(l):
        for j in range(l):
            if i == j:
                continue

            if count[i][j] > 0:
                answer[i] += 1
            elif count[i][j] == 0:
                if p[i] > p[j]:
                    answer[i] += 1

    return max(answer)

print(solution(friends, gifts))