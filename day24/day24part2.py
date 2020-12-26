with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

tiles = {}  # (e, ne) => is_black


# decomposes a movement direction on a hex grid to one or two movements in two axes (this allows for unique coords)
def decompose(direction: str) -> list:
    if direction == "se":
        return ["e", "sw"]
    elif direction == "nw":
        return ["w", "ne"]
    else:
        return [direction]


for line in lines:
    directions = []
    i = 0
    while i < len(line):
        if line[i] in {"s", "n"}:
            direction = line[i:i + 2]
            i += 2
        else:
            direction = line[i]
            i += 1
        directions.extend(decompose(direction))
    e, ne = 0, 0
    for d in directions:
        if d == "w":
            e -= 1
        elif d == "e":
            e += 1
        elif d == "ne":
            ne += 1
        elif d == "sw":
            ne -= 1
    coord = (e, ne)
    if coord in tiles:
        tiles[coord] = not tiles[coord]
    else:
        tiles[coord] = True

to_neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, 1)]
self_and_neighbors = to_neighbors + [(0, 0)]


def num_black_neighbors(e, ne) -> int:
    num = 0
    for de, dne in to_neighbors:
        coord = (e + de, ne + dne)
        num += tiles[coord] if coord in tiles else False
    return num


def do_step() -> dict:
    new_tiles = {}
    for e, ne in tiles.keys():
        for de, dne in self_and_neighbors:
            coord = (e + de, ne + dne)
            if coord in new_tiles:
                continue
            is_black = tiles[coord] if coord in tiles else False
            n_black_neighbors = num_black_neighbors(*coord)
            if is_black:
                new_tiles[coord] = n_black_neighbors != 0 and n_black_neighbors <= 2
            else:
                new_tiles[coord] = n_black_neighbors == 2
    return new_tiles


for _ in range(100):
    tiles = do_step()

print(sum(tiles.values()))

