with open("input.txt") as f:
    area = [line.strip() for line in f.readlines() if len(line.strip())]


def is_tree(row, col):
    if row < 0 or row >= len(area):
        return False
    else:
        col %= len(area[0])
        return area[row][col] == "#"


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # defined as right, down

prod = 1
for slope in slopes:
    trees = 0
    for i in range(0, len(area)):
        trees += is_tree(i * slope[1], i * slope[0])
    print(slope, trees)
    prod *= trees

print(prod)
