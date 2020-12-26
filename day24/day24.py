with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

tiles = {}  # (e, ne) => isflipped


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
            direction = line[i:i+2]
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

print(sum(tiles.values()))
