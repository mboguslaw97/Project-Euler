
def no_equal_sub_sums(l):
	sums = {0}
	for x in l:
		new_sums = set()
		for y in sums:
			if x + y in sums:
				return False
			new_sums.add(x + y)
		sums |= new_sums
	return True
	

def satisfies_req_two(l):
	l.sort()
	size = len(l)
	a = (size // 2) + (size % 2)
	b = a + 1 - (size % 2)
	s1 = sum(l[:a])
	s2 = sum(l[b:])
	return s1 > s2


f = open('105.txt', 'r')

result = 0
for line in f.readlines():
	l = list(map(int, line.split(',')))
	if satisfies_req_two(l) and no_equal_sub_sums(l):
		result += sum(l)
print(result)

f.close()	