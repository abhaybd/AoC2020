import re

with open("input.txt") as f:
    line = f.readline().strip()
    reqs = {}
    while line != "":
        name = line.split(":")[0]
        values = re.findall(r"(\d+)-(\d+)", line)
        reqs[name] = [(int(low), int(high)) for low, high in values]
        line = f.readline().strip()

    assert f.readline().strip() == "your ticket:"
    my_ticket = [int(x) for x in f.readline().strip().split(",")]

    assert f.readline().strip() == ""
    assert f.readline().strip() == "nearby tickets:"
    nearby_tickets = []
    line = f.readline().strip()
    while line != "":
        nearby_tickets.append([int(x) for x in line.split(",")])
        line = f.readline().strip()


def is_valid_any(n):
    for thresholds in reqs.values():
        for low, high in thresholds:
            if low <= n <= high:
                return True
    return False


error_rate = 0
for ticket in nearby_tickets:
    error_rate += sum([x for x in ticket if not is_valid_any(x)])
print(error_rate)
