from itertools import combinations as combos
from math import ceil, sqrt
from time import time

# square anagram word pairs
def sawps(s1, s2):
    for square1 in squares:
        cipher = {}
        chars, nums = set(), set()
        for i in range(L):
            c, n = s1[i], square1[i]
            if c in chars:
                if n != cipher[c]:
                    cipher = None
                    break
            elif n in nums:
                cipher = None
                break
            else:
                cipher[c] = n
                chars.add(c)
                nums.add(n)
        if cipher != None:
            square2 = ''
            for c in s2:
                if c in cipher:
                    square2 += cipher[c]
                else:
                    square2 = None
                    break
            if square2 != None and square2 in squares:
                yield int(square1), int(square2)

t0 = time()

L = 5

id_words_map = {}
for line in open('098.txt'):
    for word in line.strip().split(','):
        word = word[1:-1]
        if len(word) == L:
            id = ''.join(sorted(word))
            if id not in id_words_map:
                id_words_map[id] = []
            id_words_map[id].append(word)

squares = set()
M = 10 ** L
r = ceil(sqrt(M / 10))
while r ** 2 < M:
    squares.add(str(r ** 2))
    r += 1

result = 0
for words in id_words_map.values():
    for combo in combos(words, 2):
        for sawp in sawps(combo[0], combo[1]):
            result = max(max(sawp), result)
print(result)

print(time() - t0)
    

