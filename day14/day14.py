with open("input.txt") as f:
    ops = [tuple(x) for x in [line.strip().split(" = ", 2) for line in f.readlines()]]

and_mask = (1 << 36) - 1
override = 0
mem = {}
for loc, val in ops:
    if loc == "mask":
        and_mask = int(val.replace("1", "0").replace("X", "1"), base=2)
        override = int(val.replace("X", "0"), base=2)
    else:
        index = int(loc.split("[")[1][:-1])
        mem[index] = (int(val) & and_mask) + override

print(sum(mem.values()))
