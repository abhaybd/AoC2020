with open("input.txt") as f:
    cups = [int(x) for x in f.read().strip()]


def play_round(index):
    cup_id = cups[index]
    removed = []
    # print("\tCurr: " + str(cup_id))
    for i in range(index + 1, index + 4):
        removed.append(cups[i % len(cups)])
    for c in removed:
        cups.remove(c)
    # print("\t" + str(removed))
    if cup_id == min(cups):
        insert_index = cups.index(max(cups))
    else:
        cup_id -= 1
        while cup_id not in cups:
            cup_id -= 1
        insert_index = cups.index(cup_id)
    # print("\tDest: " + str(cups[insert_index]))
    for cup in reversed(removed):
        cups.insert(insert_index + 1, cup)


# print("".join([str(x) for x in cups]))
curr = cups[0]
for _ in range(100):
    play_round(cups.index(curr))
    curr = cups[(cups.index(curr) + 1) % len(cups)]

idx = cups.index(1)
for _ in range(len(cups)-1):
    idx = (idx+1) % len(cups)
    print(cups[idx], end="")
print()
