from time import time

def fill(puzzle, guesses, r, c, val):
    puzzle[r][c] = val
    del guesses[(r, c)]
    for i in range(9):
        if (r, i) in guesses:
            guesses[(r, i)].discard(val)
        if (i, c) in guesses:
            guesses[(i, c)].discard(val)
    tlr, tlc = r // 3 * 3, c // 3 * 3
    for dr in range(3):
        ri = tlr + dr
        for dc in range(3):
            ci = tlc + dc
            if (ri, ci) in guesses:
                guesses[(ri, ci)].discard(val)

def solve(puzzle):
    puzzle = [list(row) for row in puzzle]
    guesses = {(r, c) : set(range(1, 10)) for r in range(9) for c in range(9)}
    for r, c in guesses.copy():
        if puzzle[r][c] != 0:
            fill(puzzle, guesses, r, c, puzzle[r][c])
    while len(guesses) > 0:
        progress = False
        for r, c in guesses.copy():
            guess = guesses[(r, c)]
            row_guess = set()
            for i in range(9):
                if (r, i) in guesses and (r, i) != (r, c):
                    row_guess |= guesses[(r, i)]
            dif = guess - row_guess
            if len(dif) == 1:
                guess = dif.copy()
            col_guess = set()
            for i in range(9):
                if (i, c) in guesses and (i, c) != (r, c):
                    col_guess |= guesses[(i, c)]
            dif = guess - col_guess
            if len(dif) == 1:
                guess = dif.copy()      
            square_guess = set()
            tlr, tlc = r // 3 * 3, c // 3 * 3
            for dr in range(3):
                ri = tlr + dr
                for dc in range(3):
                    ci = tlc + dc
                    if (ri, ci) in guesses and (ri, ci) != (r, c):
                        square_guess |= guesses[(ri, ci)]
            dif = guess - square_guess
            if len(dif) == 1:
                guess = dif.copy()
            if len(guess) == 0:
                return None
            if len(guess) == 1:
                fill(puzzle, guesses, r, c, guess.pop())
                progress = True
        if not progress:            
            coord, guess = guesses.popitem()
            r, c = coord
            for val in guess:
                puzzle[r][c] = val
                answer = solve(puzzle)
                if answer != None:
                    return answer
            else:
                return None
    return puzzle

t0 = time()

total = 0
i = 0
puzzle = []
for line in open('096.txt'):
    if i == 0:
        puzzle = []
    else:
        puzzle.append([int(c) for c in line.strip()])
        if i == 9:
            total += int(''.join(map(str, solve(puzzle)[0][:3])))
    i = (i + 1) % 10
print(total)

print(time() - t0)
