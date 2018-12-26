from time import time

t0 = time()

L = 10 ** 6

divsums = {i : 0 for i in range(L + 1)}
for i in range(1, L + 1):
    for j in range(2 * i, L + 1, i):
        divsums[j] += i

max_length = 0
min_link = 0
todo = set(range(L + 1))
while len(todo) > 0:
    val = todo.pop()
    history = {val}
    chain = [val]
    while True:
        val = divsums[val]
        if val in history:
            i = chain.index(val)
            length = len(chain) - i
            if length > max_length:
                max_length = length
                min_link = min(chain[i:])
            break
        if val not in todo:
            break
        todo.remove(val)
        history.add(val)
        chain.append(val)
print(min_link)

print(time() - t0)
