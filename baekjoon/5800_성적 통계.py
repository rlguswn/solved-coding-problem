import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    student = n.pop(0)
    n_max = max(n)
    n_min = min(n)
    n_gap = 0

    n.sort(reverse=True)
    for j in range(student-1):
        if n[j] - n[j+1] > n_gap:
            n_gap = n[j] - n[j+1]

    print(f'Class {i+1}')
    print(f'Max {n_max}, Min {n_min}, Largest gap {n_gap}')