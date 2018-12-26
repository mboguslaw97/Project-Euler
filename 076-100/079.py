afters = {str(x):set() for x in range(10)}
befores = {str(x):set() for x in range(10)}
with open('079.txt') as text:
    for line in text:
        hint = line.strip()
        afters[hint[0]].update({hint[1], hint[2]})
        afters[hint[1]].add(hint[2])
        befores[hint[2]].update({hint[0], hint[1]})
        befores[hint[1]].add(hint[0])
for x in range(10):
    print(x, len(befores[str(x)]), len(afters[str(x)]))
