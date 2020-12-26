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

game_history = {}


def serialize(hand):
    return ",".join(str(x) for x in hand)


# returns 1 if p1 wins, 2 if p2 wins, 0 if p1 wins game immediately
def play_round(p1, p2, game):
    entry = (serialize(p1), serialize(p2))
    if entry in game_history[game]:
        return 0
    game_history[game].add(entry)
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    if len(p1) >= p1_card and len(p2) >= p2_card:
        round_winner = play_game(p1[:p1_card], p2[:p2_card], game+1)
    else:
        round_winner = 1 if p1_card > p2_card else 2

    if round_winner == 1:
        p1.extend([p1_card, p2_card])
    elif round_winner == 2:
        p2.extend([p2_card, p1_card])
    return round_winner


def play_game(p1, p2, game=0):
    game_history[game] = set()
    while len(p1) > 0 and len(p2) > 0:
        if play_round(p1, p2, game) == 0:
            return 1
    return 1 if len(p1) > 0 else 2


winner = play_game(p1, p2)
winner_hand = p2 if winner == 2 else p1
print(winner)
print(p1)
print(p2)
print(sum(card * x for card, x in zip(winner_hand, range(len(winner_hand), 0, -1))))
