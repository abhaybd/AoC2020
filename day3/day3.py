with open("input.txt") as f:
    area = [line.strip() for line in f.readlines() if len(line.strip())]


def is_tree(row, col):
    if row < 0 or row >= len(area):
        return True
    else:
        col %= len(area[0])
        return area[row][col] == "#"


trees = 0
for i in range(len(area)):
    trees += is_tree(i, 3*i)

print(trees)
