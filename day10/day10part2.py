with open("input.txt") as f:
    joltages = sorted([int(x) for x in f.readlines()])

joltages.insert(0, 0)
joltages.append(joltages[-1] + 3)


cache = {}


def count_combos(start: int):
    if start == len(joltages)-1:
        return 1
    elif start in cache:
        return cache[start]

    options = []
    for i, n in enumerate(joltages[start+1:]):
        if n - joltages[start] <= 3:
            options.append(i + start + 1)
        else:
            break

    ret = sum([count_combos(i) for i in options])
    cache[start] = ret
    return ret


print(count_combos(0))
