matrix = []
with open('081.txt') as text:
    for line in text:
        matrix.append(tuple(map(int, line.strip().split(','))))

left = [matrix[-1][-1]]
top = [matrix[-1][-1]]
for i in range(1, len(matrix)):
    left[0] += matrix[-1][-1-i]
    top[0] += matrix[-1-i][-1]
    for j in range(1, i):
        left[j] = matrix[-1-j][-1-i] + min(left[j-1], left[j])
        top[j] = matrix[-1-i][-1-j] + min(top[j-1], top[j])
    corner = matrix[-1-i][-1-i] + min(left[-1], top[-1])
    left.append(corner)
    top.append(corner)
print(corner)
