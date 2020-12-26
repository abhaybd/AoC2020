import re
from functools import reduce

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


# filter out invalid tickets and add my ticket to this
tickets = [ticket for ticket in nearby_tickets if all([is_valid_any(x) for x in ticket])]
tickets.append(my_ticket)
ticket_len = len(tickets[0])

# Build the candidates list. This is a list of sets, where each set represents all the fields that can possibly be put
# in that index. A backtracking algorithm will then find the correct combination
candidates = []
for i in range(ticket_len):
    s = set(reqs.keys())
    for ticket in tickets:
        for name, thresholds in reqs.items():
            if name in s:
                valid = False
                for low, high in thresholds:
                    if low <= ticket[i] <= high:
                        valid = True
                        break
                if not valid:
                    s.remove(name)
        if len(s) == 0:
            break
    candidates.append(s)


# backtracking algorithm to explore all possible permutations of the fields
# Build the permutation until an invalid permutation is found (no possible option) and then backtrack
def solve(permutation: list, permutation_set: set) -> list or None:
    if len(permutation) == len(candidates):
        return permutation
    else:
        options = candidates[len(permutation)]
        for option in options:
            if option not in permutation_set:
                permutation.append(option)
                permutation_set.add(option)
                solution = solve(permutation, permutation_set)
                if solution is not None:
                    return solution
                permutation.pop()
                permutation_set.remove(option)
        return None


ordering = solve([], set())
print(reduce(lambda a, b: a*b, [my_ticket[i] for i, name in enumerate(ordering) if name.startswith("departure")]))
