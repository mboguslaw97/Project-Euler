
f = open('102.txt', 'r')

result = 0
for line in f.readlines():
	v = [int(z) for z in line.split(',')]
	x = (v[0], v[2], v[4])
	y = (v[1], v[3], v[5])
	contains_origin = True
	for i in range(3):
		j = (i + 1) % 3
		k = (i + 2) % 3
		if x[j] - x[i]:
			m = (y[j] - y[i]) / (x[j] - x[i])
			b = y[i] - m * x[i]
			contains_origin &= (0 >= b and y[k] >= m*x[k] + b) or (0 <= b and y[k] <= m*x[k] + b)
		else:
			contains_origin &= (0 >= x[i] and x[k] >= x[i]) or (0 <= x[i] and x[k] <= x[i])
	result += contains_origin
print(result)

f.close()
	