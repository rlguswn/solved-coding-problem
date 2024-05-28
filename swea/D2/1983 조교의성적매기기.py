t = int(input())

def point_calc(point_str):
    p1, p2, p3 = map(int, point_str.split())
    total = (p1*0.35) + (p2*0.45) + (p3*0.20)
    return total

def total_calc(rank, n):
    r = rank / n
    if r > 0.9:
        return 'A+'
    elif r > 0.8:
        return 'A0'
    elif r > 0.7:
        return 'A-'
    elif r > 0.6:
        return 'B+'
    elif r > 0.5:
        return 'B0'
    elif r > 0.4:
        return 'B-'
    elif r > 0.3:
        return 'C+'
    elif r > 0.2:
        return 'C0'
    elif r > 0.1:
        return 'C-'
    else:
        return 'D0'

for i in range(t):
    n, k = map(int, input().split())
    student = [0 for _ in range(n)]
    for j in range(n):
        student[j] = point_calc(input())
    sorted_st = sorted(student)
    print(f'#{i+1} {total_calc(sorted_st.index(student[k-1]) + 1, n)}')