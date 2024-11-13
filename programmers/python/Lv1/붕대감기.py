bandage = [5, 1, 5] # 시전시간, 초당회복량, 시전 성공시 추가회복량
health = 30 # 최대 체력
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]] # 공격시간, 피해량

def solution(bandage, health, attacks):
    answer = health
    last = attacks[-1][0] + 1
    heal = 0
    attacks_time = []
    attacks_damage = []
    turn = 0

    for i, j in attacks:
        attacks_time.append(i)
        attacks_damage.append(j)
    
    for i in range(last):
        if i == attacks_time[turn]:
            answer -= attacks_damage[turn]
            heal = 0
            turn += 1

            if answer <= 0:
                return -1
        
        else:
            answer += bandage[1]
            heal += 1

            if bandage[0] == heal:
                answer += bandage[2]
                heal = 0

            if answer > health:
                answer = health
        
    return answer

print(solution(bandage, health, attacks))