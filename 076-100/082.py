from time import time

def prioritize(r0, c0):
    w0 = weights[r0][c0]
    r1, c1, w1 = None, None, float('inf')
    for d in ((1, 0), (-1, 0), (0, 1)):
        r2, c2 = r0 + d[0], c0 + d[1]
        if 0 <= r2 < len(matrix) and c2 < len(matrix[r0]) and weights[r2][c2] is None:
            w2 = weights[r0][c0] + matrix[r2][c2]
            if w2 < w1:
                r1, c1, w1 = r2, c2, w2
                
    if r1 is not None and c1 is not None:
        for i in range(len(priorities)):
            if w1 > priorities[i][4]:
                priorities.insert(i, (r0, c0, r1, c1, w1))
                break
        else:
            priorities.append((r0, c0, r1, c1, w1))

t0 = time()
    
matrix = []
priorities = []
weights = []
with open('082.txt') as text:
    for line in text:
        matrix.append(tuple(map(int, line.strip().split(','))))
        weights.append([None] * len(matrix[-1]))
        weights[-1][0] = matrix[-1][0]
                
for r in range(len(matrix)):
    prioritize(r, 0)

while True:
    r0, c0, r1, c1, w1 = priorities.pop(-1)
    if c1 == len(weights[r1]) - 1:
        print(w1)
        break
    if weights[r1][c1] is None:
        weights[r1][c1] = w1
        prioritize(r1, c1)
    prioritize(r0, c0)

print(time() - t0)
