tc = int(input())
for i in range(tc):
    n = int(input())
    s = input()
    if n % 2 == 1:
        result = 'No'
    else:
        half = int(n/2)
        if s[:half] == s[half:]:
            result = 'Yes'
        else:
            result = 'No'
    print(f'#{i+1} {result}')
