from math import log

max_val, result = 0, 0
i = 1
for line in open('099.txt'):
    base, exp = map(int, line.strip().split(','))
    val = exp * log(base)
    if val > max_val:
        max_val, result = val, i
    i += 1
print(max_val, result)
