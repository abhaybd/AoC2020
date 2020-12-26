import re

with open("input.txt") as f:
    graph = {}
    for line in f.readlines():
        line = line.strip()
        bag_type = re.match(r"(.+?) bags", line).group(1)
        children = re.findall(r"\d+ (.+?) bag", line)
        graph[bag_type] = set(children)
    del line, bag_type, children


contains = {}


def can_contain(bag: str, target: str) -> int:
    if bag in contains:
        return contains[bag]

    if target in graph[bag]:
        ret = True
    else:
        ret = any(can_contain(c, target) for c in graph[bag])
    contains[bag] = ret
    return ret


print(sum([can_contain(bag, "shiny gold") for bag in graph]))
