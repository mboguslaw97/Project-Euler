from re import sub
from string import ascii_uppercase

names = []
with open('022.txt') as text:
    for line in text:
        names += [name for name in sub('"', '', line).split(',')]
names.sort()

result = 0
for i in range(len(names)):
    result += (i + 1) * (sum(ascii_uppercase.index(c) for c in names[i]) + len(names[i]))
print(result)   #871198282
