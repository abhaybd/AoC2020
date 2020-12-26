with open("input.txt") as f:
    groups = [g.replace("\n", "") for g in f.read().split("\n\n")]

print(sum([len(set(g)) for g in groups]))
