import re

with open("input.txt") as f:
    lines = f.readlines()
    rules = {}
    sep = None
    for i, line in enumerate(lines):
        line = line.strip()
        if line == "":
            sep = i
            break
        else:
            index = line.index(":")
            rule_num = int(line[:index])
            rule = [r.strip() for r in line[index+1:].split("|")]
            rules[rule_num] = rule

    messages = [line.strip() for line in lines[sep+1:]]


def create_regex(rule_num: int):
    rule = rules[rule_num]
    if len(rule) == 1 and "\"" in rule[0]:
        return rule[0][1]
    return "(" + "|".join("".join(create_regex(int(r)) for r in option.split(" ")) for option in rule) + ")"


# this is a hack and a half, but whatever
# in theory, the input could repeat 10 or more times in which case this would fail, but it works so fuck it
for i in range(2, 10):
    rules[8].append(" ".join(["42"]*i))
    rules[11].append(" ".join(["42"]*i) + " " + " ".join(["31"]*i))

regex = "^" + create_regex(0) + "$"
print(sum(re.match(regex, message) is not None for message in messages))
