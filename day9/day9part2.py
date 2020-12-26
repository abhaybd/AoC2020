with open("input.txt") as f:
    numbers = [int(line) for line in f.readlines()]

target = 530627549  # answer to part 1

for start in range(len(numbers)):
    running_sum = 0
    for end, n in enumerate(numbers[start:]):
        running_sum += n
        if running_sum >= target:
            break
    if running_sum == target:
        end += start
        min_num = min(numbers[start:end+1])
        max_num = max(numbers[start:end+1])
        print(min_num + max_num)
        break
