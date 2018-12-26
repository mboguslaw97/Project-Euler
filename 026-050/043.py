from itertools import permutations as perms

def special(s):
    for i in range(1, 8):
        if int(s[i:i+3]) % primes[i-1] != 0:
            return False
    return True

primes = [2, 3, 5, 7, 11, 13, 17]

result = 0
for perm in perms('0123456789', 10):
    s = ''.join(perm)
    if special(s):
        result += int(s)
print(result)
