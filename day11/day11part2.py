from typing import List

with open("input.txt") as f:
    lines = [list(x.strip()) for x in f.readlines()]


def is_occupied(seats, row, col) -> bool:
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return False
    return seats[row][col] == "#"


def num_occ_seen(seats: List[list], row, col) -> int:
    # yes, I know this method is gross. whatever.
    num = 0
    rows = len(seats)
    cols = len(seats[0])
    for r in range(row+1, rows):
        if seats[r][col] != ".":
            num += seats[r][col] == "#"
            break
    for r in reversed(range(0, row)):
        if seats[r][col] != ".":
            num += seats[r][col] == "#"
            break

    for c in range(col+1, cols):
        if seats[row][c] != ".":
            num += seats[row][c] == "#"
            break
    for c in reversed(range(0, col)):
        if seats[row][c] != ".":
            num += seats[row][c] == "#"
            break

    r, c = row+1, col+1
    while r < rows and c < cols:
        if seats[r][c] != ".":
            num += seats[r][c] == "#"
            break
        r += 1
        c += 1
    r, c = row+1, col-1
    while r < rows and c >= 0:
        if seats[r][c] != ".":
            num += seats[r][c] == "#"
            break
        r += 1
        c -= 1
    r, c = row-1, col-1
    while r >= 0 and c >= 0:
        if seats[r][c] != ".":
            num += seats[r][c] == "#"
            break
        r -= 1
        c -= 1
    r, c = row-1, col+1
    while r >= 0 and c < cols:
        if seats[r][c] != ".":
            num += seats[r][c] == "#"
            break
        r -= 1
        c += 1
    return num


def update(seats: list) -> (list, int):
    updated = []
    n_updates = 0
    for row, arr in enumerate(seats):
        new_row = []
        for col, seat in enumerate(arr):
            s = seat
            adj_occ = num_occ_seen(lines, row, col)
            if seat == "#" and adj_occ >= 5:
                s = "L"
            elif seat == "L" and adj_occ == 0:
                s = "#"
            if s != seat:
                n_updates += 1
            new_row.append(s)
        updated.append(new_row)
    return updated, n_updates


updates = -1
while updates != 0:
    lines, updates = update(lines)

print(sum([sum([seat == "#" for seat in row]) for row in lines]))
