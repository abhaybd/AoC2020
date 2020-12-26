with open("input.txt") as f:
    cups_numbering = [int(x)-1 for x in f.read().strip()]  # change to 0-indexed
    cups = [0]*1000000  # represents a linked list, where cups[cup] = next_cup
    for i, cup in enumerate(cups_numbering[:-1]):
        cups[cup] = cups_numbering[i+1]
    cups[cups_numbering[-1]] = len(cups_numbering)
    for i in range(len(cups_numbering), len(cups)):
        cups[i] = i+1
    cups[-1] = cups_numbering[0]
    curr = cups_numbering[0]  # used later in game


def insert_after(cup: int, to_insert: list or int):
    if isinstance(to_insert, int):
        to_insert = [to_insert]
    next_node = cups[cup]
    cups[cup] = to_insert[0]
    for i, c in enumerate(to_insert[:-1]):
        cups[c] = to_insert[i+1]
    cups[to_insert[-1]] = next_node


def remove_after(cup: int, num: int) -> list:
    new_next = cup
    removed = []
    for _ in range(num+1):
        new_next = cups[new_next]
        removed.append(new_next)
    cups[cup] = new_next
    removed.pop()
    return removed


def play_round(curr_cup: int) -> int:
    removed = remove_after(curr_cup, 3)
    removed_set = set(removed)
    for min_cup in range(len(removed)+1):
        if min_cup not in removed_set:
            break
    if min_cup == curr_cup:
        dest_cup = len(cups)-1
    else:
        dest_cup = curr_cup - 1
    while dest_cup in removed_set:
        dest_cup -= 1
    insert_after(dest_cup, removed)
    return cups[curr_cup]


for _ in range(10000000):
    curr = play_round(curr)

cup1 = cups[0]
cup2 = cups[cup1]
print((cup1+1) * (cup2+1))  # convert back to 1-indexed
