with open("input.txt") as f:
    joltages = sorted([int(x) for x in f.readlines()])

joltages.insert(0, 0)
joltages.append(joltages[-1] + 3)

arrangements = [0] * len(joltages)
arrangements[-1] = 1

for i in range(len(joltages) - 2, -1, -1):
    num_permutations = 0
    max_joltage = joltages[i] + 3
    for j, joltage in enumerate(joltages[i + 1:], i + 1):
        if joltage <= max_joltage:
            num_permutations += arrangements[j]
        else:
            break
    arrangements[i] = num_permutations

print(arrangements[0])
