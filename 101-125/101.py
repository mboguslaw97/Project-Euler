import numpy.polynomial.polynomial as P


#p = [0, 0, 0, 1] 
p = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
x = list(range(1, len(p)))
y = [P.polyval(i, p) for i in range(1, len(p))]

result = 0
for i in range(len(p) - 1):
	u = P.polyfit(x[:i+1], y[:i+1], i)
	u = [round(a) for a in u]
	result += P.polyval(i + 2, u)
	
print(result)