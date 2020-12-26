with open("input.txt") as f:
    lines = f.readlines()


def is_valid(line: str):
    occurrences, letter, password = line.split(" ", 3)
    letter = letter[0]
    min_occ, max_occ = [int(x) for x in occurrences.split("-")]
    occ = 0
    for ch in password:
        if ch == letter:
            occ += 1
    return min_occ <= occ <= max_occ


print(sum([is_valid(line) for line in lines]))
