def solution(edges):
    answer = [0, 0, 0, 0]
    node = dict()
    for a, b in edges:
        if not node.get(a):
            node[a] = [0, 0]
        if not node.get(b):
            node[b] = [0, 0]
        node[a][0] += 1
        node[b][1] += 1
    
    for key, cnt in node.items():
        if cnt[0] >= 2 and cnt[1] == 0:
            answer[0] = key
        elif cnt[0] == 0 and cnt[1] >= 1:
            answer[2] += 1
        elif cnt[0] >= 2 and cnt[1] >= 2:
            answer[3] += 1
    answer[1] = node[answer[0]][0] - answer[2] - answer[3]
    return answer