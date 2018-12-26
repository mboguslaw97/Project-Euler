from time import time
from itertools import combinations as combos

def evals(nums):
    if len(nums) == 1:
        return nums
    if nums not in history:
        history[nums] = set()
        for r in range(1, 1 + len(nums) // 2):
            for nums1 in combos(nums, r):
                nums1 = frozenset(nums1)
                nums2 = frozenset(nums - nums1)
                for n1 in evals(nums1):
                    for n2 in evals(nums2):
                        vals = {n1 + n2, n1 - n2, n2 - n1, n1 * n2}
                        if n1 != 0: vals.add(n2 / n1)
                        if n2 != 0: vals.add(n1 / n2)
                        history[nums].update(vals)
    return history[nums]

t0 = time()

best = 0
history = {}
for combo in combos(range(10), 4):
    vals = evals(frozenset(combo))
    n = 1
    while n in vals:
        n += 1
    if n > best:
        best = n
        print(combo, best)

print(time() - t0)
