
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


# Prints solution
# Return True if all future increments will not satisfy lhs > rhs
min_sum = float('inf')
def solve(l=7*[0], i=0, lhs=0, rhs=0):
	global result, min_sum
	nlhs, nrhs = lhs, rhs
	for x in range(l[i-1] + 1, 50):
		# Assign new value
		l[i] = x
		
		# Calculate new left-hand-sum and right-hand-sum
		if i <= 3:
			nlhs = lhs + l[i]
		elif i >= 4:
			nrhs = rhs + l[i]
		
		# Continue iteration
		if i + 1 < len(l):
			if solve(l, i + 1, nlhs, nrhs) and i > 3:
				pass
		else:
			
			# Check if all future increments will not satisfy lhs > rhs
			if nlhs <= nrhs:
				return True
			
			# Check if l is new smallest special set
			elif sum(l) < min_sum and no_equal_sub_sums(l):
				min_sum = sum(l)
				print(''.join(list(map(str, l))))


solve()