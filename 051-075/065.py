seq = []
for k in range(66, 0, -2):
    seq += [1, k, 1]
N, D = 0, 1
for a in seq:
    N, D = D, a * D + N
print(sum(map(int, str(2 * D + N))))
