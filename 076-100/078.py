from math import sqrt

seq = [1, 2]
for d in range(2, 500):
    seq.append(seq[-1] + 2 * d - 1)
    seq.append(seq[-1] + d)
print(seq[-1])

pvals = [1] + [0] * seq[-1]
i = 0
for n in range(1, seq[-1]):
    if n >= seq[i + 1]:
        i += 1
    for j in range(i + 1):
        if j % 4 < 2:
            pvals[n] += pvals[n - seq[j]]
        else:
            pvals[n] -= pvals[n - seq[j]]
    if pvals[n] % 1000000 == 0:
        print(n, pvals[n])
        break
print(pvals)
