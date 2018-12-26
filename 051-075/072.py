def PHI(n):
    numer = n
    denom = 1
    for pf in prime_factors[n]:
        numer *= pf - 1
        denom *= pf
    return numer // denom

LIMIT = 1000001
prime_factors = {n : set() for n in range(2, LIMIT)}
for i in range(2, LIMIT):
    if len(prime_factors[i]) == 0:
        for j in range(i, LIMIT, i):
            prime_factors[j].add(i)

result = 0
for d in range(2, LIMIT):
    result += PHI(d)
print(result)

