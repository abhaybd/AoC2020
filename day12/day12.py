with open("input.txt") as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]


def move(x, y, direction, dist):
    if direction == "N":
        return x, y+dist
    elif direction == "S":
        return x, y-dist
    elif direction == "E":
        return x+dist, y
    elif direction == "W":
        return x-dist, y


def rotate_r(direction):
    if direction == "N":
        return "E"
    elif direction == "S":
        return "W"
    elif direction == "E":
        return "S"
    elif direction == "W":
        return "N"


def rotate_l(direction):
    if direction == "N":
        return "W"
    elif direction == "S":
        return "E"
    elif direction == "E":
        return "N"
    elif direction == "W":
        return "S"


x, y = 0, 0
direction = "E"
dirs = {"N", "S", "E", "W"}
for instruction in instructions:
    if instruction[0] in dirs:
        x, y = move(x,  y, *instruction)
    elif instruction[0] == "F":
        x, y, = move(x, y, direction, instruction[1])
    else:
        angle = instruction[1]
        rot_func = rotate_l if instruction[0] == "L" else rotate_r
        while angle > 0:
            angle -= 90
            direction = rot_func(direction)

print(abs(x) + abs(y))
