with open("input.txt") as f:
    f.readline()
    ids = [(i, int(x)) for i, x in enumerate(f.readline().split(",")) if x != "x"]


# calculate the bezout identity for a given pair of integers
def bezout(a, b) -> tuple:
    old_rst = (a, 1, 0)
    rst = (b, 0, 1)

    while rst[0] != 0:
        q = old_rst[0] // rst[0]
        old_rst, rst = rst, (old_rst[0] - q * rst[0], old_rst[1] - q * rst[1], old_rst[2] - q * rst[2])

    return old_rst[1], old_rst[2]


# solve the chinese remainder theorem
def solve_crt(schedule: list) -> int:
    cum_sol = schedule[0][0]
    cum_prod = schedule[0][1]
    for a, n in schedule[1:]:
        m1, m2 = bezout(cum_prod, n)
        cum_sol = cum_sol * m2 * n + a * m1 * cum_prod
        cum_prod *= n
        cum_sol = cum_sol % cum_prod
    return cum_sol


print(ids)
print(solve_crt([((n-a) % n, n) for a, n in ids]))
