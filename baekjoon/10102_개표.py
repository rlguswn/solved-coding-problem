v = int(input())
str = input()

print('A') if str.count('A') > str.count('B') else print('Tie') if str.count('A') == str.count('B') else print('B')

# if str.count('A') > str.count('B'):
#     print('A')
# elif str.count('A') == str.count('B'):
#     print('Tie')
# else:
#     print('B')