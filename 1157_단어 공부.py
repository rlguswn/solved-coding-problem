s = input().upper()
l = list(set(s))

count_list = list()

for i in l:
    cnt = s.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    count_max = l[count_list.index(max(count_list))]
    print(count_max)
