mats = [5, 3, 2]
park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

def getSize(mats, park, i, j):
    ans = -1
    for size in mats:
        sizeable = size
        for x in range(i, i+size):
            if sizeable == -1:
                break

            for y in range(j, j+size):
                if x >= len(park) or y >= len(park[0]):
                    sizeable = -1
                    break

                if park[x][y] != '-1':
                    sizeable = -1
                    break

        ans = max(ans, sizeable)
    return ans

def solution(mats, park):
    matsable = [[] for i in range(len(park))]
    answer = -1

    for i, i_value in enumerate(park):
        for j in [j for j, j_value in enumerate(i_value) if j_value == "-1"]:
            matsable[i].append(j)
    
    for i in range(len(matsable)):
        for j in matsable[i]:
            answer = max(answer, getSize(mats, park, i, j))

    return answer

print(solution(mats, park))