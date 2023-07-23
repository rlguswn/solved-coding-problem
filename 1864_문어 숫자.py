import sys

def decoding(sentence):
    sentence = sentence.replace('-', '0')
    sentence = sentence.replace('\\', '1')
    sentence = sentence.replace('(', '2')
    sentence = sentence.replace('@', '3')
    sentence = sentence.replace('?', '4')
    sentence = sentence.replace('>', '5')
    sentence = sentence.replace('&', '6')
    sentence = sentence.replace('%', '7')
    sentence = sentence.replace('/', '-1')

    return int(sentence)

while(1):
    s = list(sys.stdin.readline().rstrip())
    if s == ['#']:
        break
    s.reverse()

    for i in range(len(s)):
        s[i] = decoding(s[i])
        s[i] = (8**(i)) * s[i]

    print(sum(s))