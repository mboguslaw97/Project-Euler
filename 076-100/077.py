from helper import prime_sieve

def count_sums(sum_counts, total, i):
    global LIMIT
    j = i
    while j < len(primes) and total + primes[j] < LIMIT:
        sum_counts[total + primes[j]] = sum_counts.get(total + primes[j], 0) + 1
        count_sums(sum_counts, total + primes[j], j)
        j += 1
    return sum_counts

LIMIT = 75
primes = tuple(prime_sieve(LIMIT))
for s, count in count_sums({}, 0, 0).items():
    if count > 5000:
        print(s, count)
