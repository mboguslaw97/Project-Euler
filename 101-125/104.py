

def trim_left(a, b):
	return int(str(a)[-9:]), int(str(b)[-9:])
	

def trim_right(a, b):
	sa, sb = str(a), str(b)
	sa = '0' * (len(sb) - len(sa)) + sa
	return int(sa[:n]), int(sb[:n])


def pandigital(n):
	s = set(str(n))
	return '0' not in s and len(s) == 9

n = 15
a, b = 1, 1
i = 2
while len(str(a)) < n + 9:
	a, b = b, a + b
	i += 1

al, bl = trim_right(a, b)
ar, br = trim_left(a, b)
while True:
	a, b = b, a + b
	al, bl = bl, al + bl
	ar, br = br, ar + br
	al, bl = trim_right(al, bl)
	ar, br = trim_left(ar, br)
	i += 1
	if pandigital(int(str(bl)[:9])) and pandigital(br):
		print(i)
		break