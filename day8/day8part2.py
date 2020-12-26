with open("input.txt") as f:
    lines = [(op, int(n)) for op, n in [line.strip().split(" ") for line in f.readlines()]]


def terminates(lines):
    visited = [False] * len(lines)
    i = 0
    acc = 0
    while i < len(lines):
        if visited[i]:
            return False, acc
        visited[i] = True
        op, n = lines[i]
        if op == "acc":
            acc += n
        elif op == "jmp":
            i += n - 1
        i += 1
    return True, acc


def switch(op):
    return "jmp" if op == "nop" else "nop"


for i, (op, n) in enumerate(lines):
    if op == "jmp" or op == "nop":
        lines[i] = (switch(op), n)
        t, acc = terminates(lines)
        if t:
            print(acc)
            break
        else:
            lines[i] = (op, n)
