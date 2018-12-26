from itertools import combinations as combos


result = 0
s = set(range(12))
for i in range(2, len(s)//2 + 1):
	for combo in combos(s, 2 * i):
		for a in combos(combo, i):
			b = tuple(x for x in combo if x not in a)
			result += a < b and False in set(a[j] < b[j] for j in range(i))
print(result)