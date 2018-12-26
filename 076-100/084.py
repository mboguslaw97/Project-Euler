from random import randint

CH_SPACES = {7, 22, 36}
CH_CARDS = (0, 10, 11, 24, 39, 5, 'R', 'R', 'U', '-3')
R_MAP = {7:15, 22:25, 36:5}
U_MAP = {7:12, 22:28, 36:12}
CC_SPACES = {2, 17, 33}
CC_CARDS = (0, 10)

counts = {space: 0 for space in range(40)}
space = 0
doubles = 0
for _ in range(999999):
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    double = doubles + 1 if die1 == die2 else 0
    space = (space + die1 + die2) % 40

    if doubles == 3 or space == 30:
        space = 10
        doubles = 0
    if space in CH_SPACES:
        r = randint(0, 15)
        if r < 10:
            card = CH_CARDS[r]
            if card == 'R': space = R_MAP[space]
            elif card == 'U': space = U_MAP[space]
            elif card == '-3': space -= 3
            else: space = card
    if space in CC_SPACES:
        r = randint(0, 15)
        if r < 2:
            space = CC_CARDS[r]
    counts[space] += 1

third_largest = sorted(counts.values())[-3]
for space, count in counts.items():
    if count >= third_largest:
        print(space, count)



