tri = []
with open('067.txt') as text:
    for line in text:
        tri.append([int(x) for x in line.split(' ')])
for i in range(len(tri)-2, -1, -1):    
    for j in range(len(tri[i])):
        tri[i][j] += tri[i+1][j] if tri[i+1][j] > tri[i+1][j+1] else tri[i+1][j+1]
print(tri[0][0])
