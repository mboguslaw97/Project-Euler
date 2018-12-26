from time import time

def head(x):
    return str(x)[:2].zfill(2)

def tail(x):
    return str(x)[2:].zfill(2)

def solution(start, group, used):
    if len(group) == 6 and group[-1] == start:
        result = [int(group[i] + group[i + 1]) for i in range(-1, 5)]
        print(result)
        print(sum(result))
        
    h = group[-1]
    for s in range(3, 8):
        if s not in used and h in figurates[s]:
            for t in figurates[s][h]:
                solution(start, group + [t], used | {s})

t0 = time()

#figurate numbers grouped by first two digits (head)
figurates = {}
for s in range(3, 9):
    figurates[s] = {}
    P = 1
    delta = s - 1
    while P < 10000:
        if P >= 1000:
            h = head(P)
            figurates[s][h] = figurates.get(h, set()) | {tail(P)}
        P += delta
        delta += s - 2

for h, ts in figurates[8].items():
    for t in ts:
        solution(h, [t], set())

print(time() - t0)
