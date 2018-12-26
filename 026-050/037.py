from helper import primes, prime

def truncateable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not prime(int(s[:i])) or not prime(int(s[i:])):
            return False
    return True

result = 0
count = 0
for p in primes():
    if p > 10 and truncateable(p):
        print(p)
        result += p
        count += 1
    if count >= 11:
        break
		
print(result)
