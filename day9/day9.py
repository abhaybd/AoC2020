with open("input.txt") as f:
    numbers = [int(line) for line in f.readlines()]


def valid(s: set, target: int) -> bool:
    return any(target-term in s for term in s)


queue = numbers[:25]
queueSet = set(queue)

for n in numbers[25:]:
    if not valid(queueSet, n):
        print(n)
        break
    else:
        queueSet.remove(queue.pop(0))
        queue.append(n)
        queueSet.add(n)
