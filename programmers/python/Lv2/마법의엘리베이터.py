def solution(storey):
    answer = 0
    number = storey
    d = 1
    while (number!=0):
        p = number%(d*10)//d
        n = number%(d*100)//(d*10)
        if p<=5:
            answer+=p
            if p==5 and n>=5:
                number+=(d*10)
        else:
            answer+=(10-p)
            number+=(d*10)
        number-=(p*d)
        d*=10
            
    return answer