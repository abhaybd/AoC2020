with open("input.txt") as f:
    starting_nums = [int(x) for x in f.readline().strip().split(",")]


def play_game(num_rounds):
    hist = {num: i for i, num in enumerate(starting_nums, 1)}  # num => (lastSpoken, lastSpokenBeforeThat)
    last = starting_nums[-1]
    for i in range(len(starting_nums)+1, num_rounds+1):
        if last in hist:
            new_last = i - 1 - hist[last]
            hist[last] = i - 1
            last = new_last
        else:
            hist[last] = i - 1
            last = 0
    return last


# part 1
print(play_game(2020))
# part 2
print(play_game(30000000))
