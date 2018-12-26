from itertools import permutations as perms

for perm in perms(range(1, 10)):
    perm = (10,) + perm
    total = perm[8] + perm[9] + perm[1]
    for i in range(0, 8, 2):
        if perm[i] + perm[i + 1] + perm[i + 3] != total:
            break
    else:
        min_i, min_val = 0, 10
        for i in range(2, 10, 2):
            if perm[i] < min_val:
                min_i, min_val = i, perm[i]
        perm = perm[min_i:] + perm[:min_i]

        s = ''
        for i in range(-10, 0, 2):
            s += str(perm[i]) + str(perm[i + 1]) + str(perm[i + 3])
        print(s)
