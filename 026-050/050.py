from helper import primes

LIMIT = 1000000

prime_list = list(primes(LIMIT))
prime_set = set(prime_list)

length, result = 0, 0
for i in range(len(prime_list)):
    total = 0
    for j in range(i, len(prime_list)):
        total += prime_list[j]
        if total > LIMIT:
            break
        if total in prime_set and j - i > length:
            length, result = j - i, total
print(length, result)
        
