from itertools import combinations as combos

squares = [(0, 1), (0, 4), (2, 5), (8, 1), (0,), (1,), (3,), (4,)]
dice = [set(combo) for combo in combos(range(10), 6)]

count = 0
for i in range(len(dice)):
    for j in range(i + 1, len(dice)):
        for square in squares:
            if len(square) == 2:
                if square[0] not in dice[i] or square[1] not in dice[j]:
                    if square[1] not in dice[i] or square[0] not in dice[j]:
                        break
            elif square[0] not in dice[i] or 6 not in dice[j] and 9 not in dice[j]:
                if 6 not in dice[i] and 9 not in dice[i] or square[0] not in dice[j]:
                    break
        else:
            count += 1
print(count)
