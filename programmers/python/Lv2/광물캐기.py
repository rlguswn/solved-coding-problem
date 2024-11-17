# picks 곡괭이의 개수를 나타내는 정수 배열 (dia, iron, stone)
# minerals 광물들의 순서를 나타내는 문자열 배열

def sortGuide(minerals):
    s = 0
    for i in minerals:
        if i=="diamond":
            s+=25
        elif i=="iron":
            s+=5
        else:
            s+=1
    return -s

def solution(picks, minerals):
    answer = 0
    mineral = []
    l = len(minerals)
    
    for i in range(l//5):
        mineral.append(minerals[i*5:i*5+5])
    if l%5!=0:
        mineral.append(minerals[l//5*5:])
    
    if sum(picks) < len(mineral):
        mineral = mineral[:sum(picks)]
    mineral.sort(key=lambda x:(sortGuide(x), len(x)))
    
    pick_grade = -1
    pick_count = 0
    for i in mineral:
        while(pick_count==0 and pick_grade!=2):
            pick_grade += 1
            pick_count = picks[pick_grade]
            
        if pick_count==0 and pick_grade==2:
            break
        
        for j in i:
            if pick_grade==0:
                answer+=1
            elif pick_grade==1:
                if j=="diamond":
                    answer+=5
                    continue
                answer+=1
            else:
                if j=="diamond":
                    answer+=25
                    continue
                elif j=="iron":
                    answer+=5
                    continue
                answer+=1
        
        pick_count-=1
        
    return answer