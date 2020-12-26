from functools import reduce
from collections import Counter

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

grid_edges = reduce(lambda a, b: a+b, [list(ids) for _, ids in edge_map.items() if len(ids) == 1])
counter = Counter(grid_edges)
print(reduce(lambda a, b: a * b, [tile_id for tile_id, count in counter.most_common() if count//2 == 2]))
