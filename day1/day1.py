with open("input.txt") as f:
    report = f.readlines()

expenses = set([int(x) for x in report])


def search(target, n):
    if n < 2:
        return target if target in expenses else None
    for e in expenses:
        ret = search(target - e, n - 1)
        if ret is not None:
            return e * ret
    return None


# part 1
print(search(2020, 2))
# part 2
print(search(2020, 3))
