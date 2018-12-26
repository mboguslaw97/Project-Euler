
def prime_sieve(n):
	all_ones = 2 ** n - 1
	bitmap_primes = all_ones
	for x in range(2, n):
		if (bitmap_primes >> x) & 1:
			yield x
			for i in range(2 * x, n, x):
				bitmap_primes &= all_ones ^ (1 << i)


def num_divisors(n, primes):
	result = 1
	i = 0
	while n > 1:
		power = 0
		while n % primes[i] == 0:
			n = int(round(n / primes[i]))
			power += 1
		result *= power + 1
		i += 1
	return result


def num_solutions(n, primes):
	n_divisors = num_divisors(n ** 2, primes)
	return (n_divisors + 1) // 2


cap = 200000
primes = list(prime_sieve(cap))
for n in range(100000, cap):
	if num_solutions(n, primes) > 1000:
		print(n)