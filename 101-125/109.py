
MAX_VALUE = 99
scores = list(range(21)) + [25]
result = 0

for i in range(1, len(scores)):
	# If not too large
	if 2 * scores[i] > MAX_VALUE:
		break
	for y in range(1, 4):
		for j in range(len(scores)):
			# If not too large
			if 2 * scores[i] + y * scores[j] > MAX_VALUE:
				break
			# if not (D0 or T0 T25)
			if not (y in {2, 3} and j == 0 or y == 3 and scores[j] == 25):
				for z in range(1, 4):
					for k in range(j, len(scores)):
						# If not too large
						if 2 * scores[i] + y * scores[j] + z * scores[k] > MAX_VALUE:
							break
						# If not (D0 or T0 or T25) and not counting duplicates
						if not (z in {2, 3} and k == 0 or z == 3 and scores[k] == 25):
							# If unique
							if (j != k or y <= z):
								result += 1

print(result)