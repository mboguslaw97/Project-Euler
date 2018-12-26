from time import time
from itertools import combinations_with_replacement as cwr

t0 = time()

l = 7
facts = [1]
for i in range(1, l + 1):
    facts.append(i * facts[i - 1])
squares = [x ** 2 for x in range(10)]
tails = {1: 1, 89: 89}

result = 0
for combo in cwr(range(10), l):
    n = sum(squares[x] for x in combo)
    if n > 1:
        history = []
        while n not in tails:
            n = sum(squares[int(c)] for c in str(n))
            history.append(n)
        for m in history:
            tails[m] = tails[n]
            
        if tails[n] == 89:
            digits = {x:0 for x in range(10)}
            for x in combo:
                digits[x] += 1
            perms = facts[l]
            for x in range(0, 10):
                perms /= facts[digits[x]]
            result += perms
            
print(result)

print(time() - t0)
