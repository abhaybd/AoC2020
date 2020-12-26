with open("input.txt") as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

waypoint_pos = (10, 1)  # (E, N)
ship_pos = (0, 0)

for instruction in instructions:
    op, n = instruction
    if op == "F":
        for i in range(n):
            ship_pos = ship_pos[0] + waypoint_pos[0], ship_pos[1] + waypoint_pos[1]
    elif op == "N":
        waypoint_pos = waypoint_pos[0], waypoint_pos[1] + n
    elif op == "S":
        waypoint_pos = waypoint_pos[0], waypoint_pos[1] - n
    elif op == "E":
        waypoint_pos = waypoint_pos[0] + n, waypoint_pos[1]
    elif op == "W":
        waypoint_pos = waypoint_pos[0] - n, waypoint_pos[1]
    elif op == "L":
        for i in range(n//90):
            waypoint_pos = -waypoint_pos[1], waypoint_pos[0]
    elif op == "R":
        for i in range(n//90):
            waypoint_pos = waypoint_pos[1], -waypoint_pos[0]

print(abs(ship_pos[0]) + abs(ship_pos[1]))
