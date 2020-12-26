with open("input.txt") as f:
    lines = f.readlines()


def is_valid(line: str):
    positions, letter, password = line.split(" ", 3)
    letter = letter[0]
    p1, p2 = [int(x)-1 for x in positions.split("-")]
    return (password[p1] == letter) ^ (password[p2] == letter)


print(sum([is_valid(line) for line in lines]))
