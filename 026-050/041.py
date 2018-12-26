from helper import prime
from itertools import permutations as perms

for perm in perms('7654321', 7):
    if prime(int(''.join(perm)), 2):
        print(''.join(perm))
        break
