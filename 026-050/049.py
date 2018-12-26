from itertools import permutations as perms

LIMIT = 10000
prime_set = set()
primes = [True] * LIMIT
for x in range(2, LIMIT):
    if primes[x]:
        if x > 999:
            prime_set.add(x)
        for y in range(x, LIMIT, x):
            primes[y] = False

while len(prime_set) > 0:
    prime = prime_set.pop()
    nums = {prime}
    for perm in perms(str(prime)):
        num = int(''.join(perm))
        if num in prime_set:
            nums.add(num)
            prime_set.remove(num)
    for num1 in nums:
        for num2 in nums:
            if num1 != num2:
                num3 = 2 * num2 - num1
                if num3 in nums:
                    print(num1, num2, num3)
