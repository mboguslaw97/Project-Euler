def answer(n):
    max_val, max_length = 1, 1
    lengths = {1: 1}
    for i in range(2, n):
        val, length = i, 0
        while True:
            val = val/2 if val%2==0 else 3*val+1
            length += 1
            if val in lengths:
                length += lengths[val]
                break
        lengths[i] = length
        if length > max_length:
            max_val, max_length = i, length
    return max_val

print(answer(1000000))
