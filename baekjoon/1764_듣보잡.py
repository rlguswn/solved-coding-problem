import sys

n, m = map(int, sys.stdin.readline().split())
n_l = list()
m_l = list()

for i in range(n):
    n_l.append(sys.stdin.readline().strip())

for j in range(m):
    m_l.append(sys.stdin.readline().strip())

nm_l = sorted(list(set(n_l) & set(m_l)))

print(len(nm_l))
for k in nm_l:
    print(k)