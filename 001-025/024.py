from itertools import permutations

perms = permutations(range(10))
for i in range(1000000):
    result = next(perms)
print(result)


    
