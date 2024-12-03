# weights = [100,180,360,100,270]

def solution(weights):
    count = dict()
    answer = [0,0]
    ratios = [2/3, 3/2, 2/4, 4/2, 3/4, 4/3]
    
    # 각 무게별 수 집계
    for i in weights:
        if not(i in count.keys()):
            count[i] = 1
        else:
            count[i] += 1
    
    # 동일한 무게로 시소 짝꿍
    for k in [i for i in count.keys() if count[i] > 1]:
        answer[0]+=count[k] * (count[k]-1)
        
    # 다른 무게로 시소 짝꿍
    for i in weights:
        for ratio in ratios:
            target = i*ratio
            if target.is_integer() and target in count.keys():
                answer[1] += count[target]
    
    return (answer[0]+answer[1])//2