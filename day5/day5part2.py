with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def seat_id(encoding: str) -> int:
    row = int(encoding[:7].replace("B", "1").replace("F", "0"), base=2)
    col = int(encoding[7:].replace("R", "1").replace("L", "0"), base=2)
    return row * 8 + col


seats = set([seat_id(enc) for enc in lines])
min_id = min(seats)
max_id = max(seats)

for i in range(min_id, max_id):
    if i not in seats:
        print(i)
        break
