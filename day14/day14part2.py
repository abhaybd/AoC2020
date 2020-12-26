with open("input.txt") as f:
    ops = [tuple(x) for x in [line.strip().split(" = ", 2) for line in f.readlines()]]


def permutations(addr: int, floating_indexes: list, addrs: list, index: int):
    if index == len(floating_indexes):
        addrs.append(addr)
    else:
        permutations(addr, floating_indexes, addrs, index+1)
        permutations(addr ^ (1 << floating_indexes[index]), floating_indexes, addrs, index+1)
    return addrs


def get_addrs(override: int, floating_indexes: list, addr: int) -> list:
    addr = (addr & (~override)) + override
    return permutations(addr, floating_indexes, [], 0)


override = 0
floating_indexes = []
mem = {}
for loc, val in ops:
    if loc == "mask":
        override = int(val.replace("X", "0"), base=2)
        floating_indexes = [len(val) - i - 1 for i, ch in enumerate(val) if ch == "X"]
    else:
        addr = int(loc.split("[")[1][:-1])
        addrs = get_addrs(override, floating_indexes, addr)
        v = int(val)
        for a in addrs:
            mem[a] = v

print(sum(mem.values()))
