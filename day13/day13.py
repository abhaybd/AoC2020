with open("input.txt") as f:
    start = int(f.readline())
    ids = [int(x) for x in f.readline().split(",") if x != "x"]

min_time = None
for bus_id in ids:
    t = bus_id - (start % bus_id)
    if min_time is None or t < min_time:
        min_time = t
        best_id = bus_id

print(best_id * min_time)
