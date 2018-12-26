g = []
with open('011.txt') as text:
    for line in text:
        g.append([int(x) for x in line.strip().split(' ')])
products = []
for r in range(len(g)):
    for c in range(len(g[0])):
        if r < len(g)-3:
            products.append(g[r][c] * g[r+1][c] * g[r+2][c] * g[r+3][c])
        if c < len(g[0])-3:
            products.append(g[r][c] * g[r][c+1] * g[r][c+2] * g[r][c+3])
        if r > 2 and c > 2:
            products.append(g[r][c] * g[r-1][c-1] * g[r-2][c-2] * g[r-3][c-3])
        if r > 2 and c < len(g[0])-3:
            products.append(g[r][c] * g[r-1][c+1] * g[r-2][c+2] * g[r-3][c+3])
print(max(products))
