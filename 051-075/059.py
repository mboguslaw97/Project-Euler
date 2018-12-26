from string import ascii_lowercase
from itertools import product

cipher = []
with open('059.txt') as text:
    for line in text:
        cipher += map(int, line.split(','))

popular = {ord(' '), ord('E'), ord('e'), ord('T'), ord('t'), ord('A'), ord('a'), ord('O'), ord('o')}
for key in product((ord(c) for c in ascii_lowercase), repeat=3):
    msg = ''
    value = 0
    score = 0
    for i in range(len(cipher)):
        code = key[i % 3] ^ cipher[i]
        msg += chr(code)
        value += code
        score += code in popular
    if score > 500:
        print('Key: {}  Score: {}  Value: {}'.format(key, score, value))
        print(msg)
        print()
    
