with open("input.txt") as f:
    groups = [g.split("\n") for g in f.read().split("\n\n")]


def num_questions(answers):
    s = set(answers[0])
    for a in answers[1:]:
        s &= set(a)
    return len(s)


print(sum([num_questions(g) for g in groups]))