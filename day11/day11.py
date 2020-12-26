with open("input.txt") as f:
    lines = [list(x.strip()) for x in f.readlines()]


def is_occupied(seats, row, col) -> bool:
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return False
    return seats[row][col] == "#"


def num_adj_occ(seats: list, row, col) -> int:
    num = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue
            elif is_occupied(seats, r, c):
                num += 1
    return num


def update(seats: list) -> (list, int):
    updated = []
    n_updates = 0
    for row, arr in enumerate(seats):
        new_row = []
        for col, seat in enumerate(arr):
            s = seat
            adj_occ = num_adj_occ(lines, row, col)
            if seat == "#" and adj_occ >= 4:
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
