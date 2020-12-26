import re

with open("input.txt") as f:
    graph = {}
    for line in f.readlines():
        line = line.strip()
        bag_type = re.match(r"(.+?) bags", line).group(1)
        children = re.findall(r"(\d+) (.+?) bag", line)
        graph[bag_type] = children
    del line, bag_type, children


bag_map = {}


def num_bags(bag: str) -> int:
    if bag in bag_map:
        return bag_map[bag]

    ret = sum([int(count) * (1 + num_bags(bag_type)) for count, bag_type in graph[bag]])
    bag_map[bag] = ret
    return ret


print(num_bags("shiny gold"))
