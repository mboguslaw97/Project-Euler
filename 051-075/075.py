##a = 2xy
##b = x^2 - y^2
##c = x^2 + y^2
##P = 2x^2 + 2xy

LIMIT = 1500000
length_combos = {}
y = 1
x = 2
while 2*x*x + 2*x*y <= LIMIT:
    while 2*x*x + 2*x*y <= LIMIT:
        a = 2*x*y
        b = x*x - y*y
        length = 2*x*x + 2*x*y
        k = 1
        while k * length <= LIMIT:
            if k * length not in length_combos:
                length_combos[k * length] = set()
            length_combos[k * length].add(frozenset({k * a, k * b}))
            k += 1
        x += 1   
    y += 1
    x = y + 1
print(sum(len(combos) == 1 for combos in length_combos.values()))
