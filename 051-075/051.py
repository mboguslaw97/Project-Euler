from itertools import combinations
from helper import prime_sieve

def replace(n, x, indexes):
    s, c = str(n), str(x)
    result = ''
    for i in range(len(s)):
        result += c if i in indexes else s[i]
    return int(result)

result = float('inf')
prime_list = []
prime_set = set()
for prime in prime_sieve(1000000):
    if prime >= 100000:
        prime_list.append(prime)
        prime_set.add(prime)

combos = []
for r in range(1, 5):
    combos += list(combinations(range(5), r))

for prime in prime_list:
    for combo in combos:
        primes = []
        for x in range(0 in combo, 10):
            n = replace(prime, x, combo)
            if n in prime_set:
                primes.append(n)
        if len(primes) == 8:
            result = min(result, primes[0])

print(result)
