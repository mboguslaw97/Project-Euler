def right(x1, y1, x2, y2):
    if x1 + y1 == 0 or x2 + y2 == 0 or (x1, y1) == (x2, y2):
        return False
    temp = x1 * x2 + y1 * y2
    return temp == 0 or temp == x1 * x1 + y1 * y1 or temp == x2 * x2 + y2 * y2

LIMIT = 51
result = 0
for x1 in range(LIMIT):
    for y1 in range(LIMIT):
        x2 = x1
        for y2 in range(y1 + 1, LIMIT):
            result += right(x1, y1, x2, y2)
        for x2 in range(x1 + 1, LIMIT):
            for y2 in range(LIMIT):
                result += right(x1, y1, x2, y2)
print(result)
