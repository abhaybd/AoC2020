with open("input.txt") as f:
    lines = [(op, int(n)) for op, n in [line.strip().split(" ") for line in f.readlines()]]

visited = [False] * len(lines)

i = 0
acc = 0
while True:
    if visited[i]:
        break
    visited[i] = True
    op, n = lines[i]
    if op == "acc":
        acc += n
    elif op == "jmp":
        i += n - 1
    i += 1

print(acc)
