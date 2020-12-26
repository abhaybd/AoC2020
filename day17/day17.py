with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    space = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            space[(x, y, 0)] = ch == "#"


def is_coord_active(space: dict, coord: tuple) -> bool:
    return space[coord] if coord in space else False


def num_active_neighbors(space: dict, x, y, z) -> int:
    num = 0
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            for dz in range(-1, 2, 1):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                num += is_coord_active(space, (x+dx, y+dy, z+dz))
    return num


def step_forward(space: dict) -> dict:
    next = {}
    for x, y, z in space.keys():
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                for dz in range(-1, 2, 1):
                    neighbor_coord = (x+dx, y+dy, z+dz)
                    if neighbor_coord in next:
                        continue
                    n_neighbors = num_active_neighbors(space, *neighbor_coord)
                    active = is_coord_active(space, neighbor_coord)
                    if active:
                        next[neighbor_coord] = n_neighbors == 2 or n_neighbors == 3
                    else:
                        next[neighbor_coord] = n_neighbors == 3
    return next


for i in range(6):
    space = step_forward(space)

print(len([coord for coord, active in space.items() if active]))
