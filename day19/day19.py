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


def _matches_rule(rule_num: int, message: str) -> (bool, int):
    if len(message) == 0:
        return False, 0
    rule = rules[rule_num]
    if len(rule) == 1 and "\"" in rule[0]:
        if message[0] == rule[0][1]:
            return True, 1
        else:
            return False, -1
    for sub_rule in rule:
        i = 0
        matches = True
        for r in sub_rule.split(" "):
            m, consumed = _matches_rule(int(r), message[i:])
            if not m:
                matches = False
                break
            i += consumed
        if matches:
            return True, i
    return False, -1


def matches_rule(rule_num, message):
    m, c = _matches_rule(rule_num, message)
    return m and c == len(message)


print(sum(matches_rule(0, message) for message in messages))
