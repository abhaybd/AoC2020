from functools import reduce
from collections import Counter
import re

with open("input.txt") as f:
    tiles = {}
    line = f.readline()
    while line != "":
        title = line[:-1]
        tile_id = int(title.split(" ", 2)[1][:-1])
        tile = []
        line = f.readline()
        while line != "\n" and line != "":
            tile.append(line[:-1])
            line = f.readline()
        tiles[tile_id] = tile
        line = f.readline()


def get_edges(tile):
    edges = [tile[0], tile[-1], "".join(row[0] for row in tile), "".join(row[-1] for row in tile)]
    edges = edges + [s[::-1] for s in edges]
    return edges


edge_map = {}
for tile_id, tile in tiles.items():
    tile_edges = get_edges(tile)
    for edge in tile_edges:
        if edge not in edge_map:
            edge_map[edge] = set()
        edge_map[edge].add(tile_id)

grid_edges = reduce(lambda a, b: a + b, [list(ids) for _, ids in edge_map.items() if len(ids) == 1])
counter = Counter(grid_edges)
# corners are all the ids that have 2 solitary edges (divide by two to account for reverses)
corner_ids = [tile_id for tile_id, count in counter.most_common() if count // 2 == 2]

# build connection map to show connections between ids
seen_edges = set()
connections = {}
for edge, ids in edge_map.items():
    if edge not in seen_edges and edge[::-1] not in seen_edges:
        seen_edges.add(edge)
        if len(ids) == 2:
            id1, id2 = list(ids)
            if id1 not in connections:
                connections[id1] = []
            if id2 not in connections:
                connections[id2] = []
            connections[id1].append(id2)
            connections[id2].append(id1)

print(corner_ids)
print(connections)


# Implementation of Dijkstra's Algorithm, we can use this to navigate the connection map to find straight lines
def pathfind(from_id, to_id):
    node_map = {from_id: [from_id]}

    def get(node_id):
        if node_id in node_map:
            return node_map[node_id]
        val = []
        node_map[node_id] = val
        return val

    queue = []
    to_search = from_id
    while to_search != to_id:
        neighbors = connections[to_search]
        path_to_curr = get(to_search)
        for n in neighbors:
            path = get(n)
            if len(path) == 0 or len(path) > len(path_to_curr) + 1:
                path.clear()
                path.extend(path_to_curr + [n])
                queue.append(n)
        to_search = min(queue, key=lambda x: len(get(x)))
        queue.remove(to_search)
    return get(to_id)


# find two parallel edges of the grid
side1 = pathfind(corner_ids[0], corner_ids[2])
side2 = pathfind(corner_ids[1], corner_ids[3])
# if the second coord in these lines have a different distance, this is a diagonal, so swap endpoints to make parallel
if len(pathfind(side1[1], side2[1])) != len(side1):
    side1 = pathfind(corner_ids[0], corner_ids[3])
    side2 = pathfind(corner_ids[1], corner_ids[2])

grid = []
for id1, id2 in zip(side1, side2):
    grid.append(pathfind(id1, id2))

print("\n".join(str(x) for x in grid))


def flip_h(tile):
    return [row[::-1] for row in tile]


def flip_v(tile):
    return tile[::-1]


def rotate180(tile):
    return flip_h(flip_v(tile))


def rotate90(tile):
    rotated = [[""] * len(tile) for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile)):
            rotated[j][-1 - i] = tile[i][j]
    return ["".join(row) for row in rotated]


def rotate270(tile):
    rotated = [[""] * len(tile) for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile)):
            rotated[-1 - j][i] = tile[i][j]
    return ["".join(row) for row in rotated]


transformations = [lambda x: x, flip_v, flip_h, rotate90, rotate180, rotate270, lambda x: flip_v(rotate90(x)),
                   lambda x: rotate90(flip_v(x))]
grid_size = len(grid)


def is_last_valid(img):
    i = len(img) - 1
    tile = img[i]
    if i // grid_size > 0:
        top_row = tile[0]
        tile_up = img[i - grid_size]
        bottom_row_up = tile_up[-1]
        if top_row != bottom_row_up:
            return False
    if i % grid_size > 0:
        left_col = "".join(row[0] for row in tile)
        tile_left = img[i - 1]
        right_col_left = "".join(row[-1] for row in tile_left)
        if left_col != right_col_left:
            return False
    return True


def solve(img: list, i: int):
    if i == grid_size ** 2:
        return True
    r, c = i // grid_size, i % grid_size
    tile = tiles[grid[r][c]]
    for trf in transformations:
        img.append(trf(tile))
        if is_last_valid(img):
            if solve(img, i + 1):
                return True
        img.pop()
    return False


image_1d_wrapped = []
solve(image_1d_wrapped, 0)
cropped_1d = [[row[1:-1] for row in x[1:-1]] for x in image_1d_wrapped]
tile_size = len(cropped_1d[0])
size = grid_size * tile_size

image = [[""] * size for _ in range(size)]
for i, tile in enumerate(cropped_1d):
    r, c = i // grid_size, i % grid_size
    for i in range(tile_size):
        for j in range(tile_size):
            image[r*tile_size+i][c*tile_size+j] = tile[i][j]

image = ["".join(row) for row in image]
# print("\n".join(image))


def flatten(img):
    return "".join(image)


det_regex = r"..................#.[.#\n]{%d}#....##....##....###[.#\n]{%d}.#..#..#..#..#..#..." % (size-19, size-19)
# 19 comes from width of sea monster - 1 because of newline character
for trf in transformations:
    transformed = trf(image)
    image_str = "\n".join(transformed)
    matches = re.findall(det_regex, image_str)
    if len(matches) > 0:
        print(image_str)
        image = transformed
        break

monster_regexes = ["..................#.", "#....##....##....###", ".#..#..#..#..#..#..."]
monster_width = len(monster_regexes[0])
expectations = {}  # (pos in str, index in regex)
num_monsters = 0
for line in image:
    # handle expectations
    next_expectations = {}
    for pos, indexes in expectations.items():
        for index in indexes:
            if re.match(monster_regexes[index], line[pos:pos+monster_width]):
                index += 1
                if index == len(monster_regexes):
                    num_monsters += 1
                else:
                    if pos not in next_expectations:
                        next_expectations[pos] = []
                    next_expectations[pos].append(index)
    expectations = next_expectations
    # handle new monsters
    for i in range(len(line) - monster_width):
        substr = line[i:i+monster_width]
        if re.match(monster_regexes[0], substr):
            if i not in expectations:
                expectations[i] = []
            expectations[i].append(1)

print("Num monsters: " + str(num_monsters))
print(sum(row.count("#") for row in image) - 15 * num_monsters)

