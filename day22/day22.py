with open("input.txt") as f:
    p1 = []
    f.readline()
    line = f.readline()
    while line != "\n":
        p1.append(int(line.strip()))
        line = f.readline()
    f.readline()
    p2 = []
    line = f.readline()
    while line != "":
        p2.append(int(line.strip()))
        line = f.readline()


def play_round():
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    if p1_card > p2_card:
        p1.extend([p1_card, p2_card])
    else:
        p2.extend([p2_card, p1_card])


while len(p1) > 0 and len(p2) > 0:
    play_round()

winner = p1 if len(p1) > 0 else p2
print(sum(card * x for card, x in zip(winner, range(len(winner), 0, -1))))
