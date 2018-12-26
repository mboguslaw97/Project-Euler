from helper import gen_primes

def answer(n):
    total = 0
    for prime in gen_primes():
        if prime >= n:
            return total
        total += prime

print(answer(10))
print(answer(2000000))
