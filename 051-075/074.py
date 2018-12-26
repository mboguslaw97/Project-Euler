from time import time
from math import factorial as f

t0 = time()

fs = {n : f(n) for n in range(10)}
lengths = {}
for n in range(1000000):
    history_set = set()
    history_list = []
    while True:
        if n in lengths:
            for j, x in enumerate(history_list):
                lengths[x] = lengths[n] + len(history_list) - j
            break
        elif n in history_set:
            i = history_list.index(n)
            for j, x in enumerate(history_list):
                if j < i:
                    lengths[x] = len(history_list) - j
                else:
                    lengths[x] = len(history_list) - i
            break
        history_set.add(n)
        history_list.append(n)
        n = sum(fs[int(c)] for c in str(n))
print(sum(length == 60 for length in lengths.values()))
    
print(time() - t0)
