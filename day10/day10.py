with open("input.txt") as f:
    joltages = sorted([int(x) for x in f.readlines()])

diffs = {3: 1}

prev = 0
for joltage in joltages:
    diff = joltage - prev
    prev = joltage
    if diff not in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] += 1

print(diffs[1] * diffs[3])
