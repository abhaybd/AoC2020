import re

with open("input.txt") as f:
    passport_strs = f.read().split("\n\n")
    passports = []
    for p in passport_strs:
        parts = re.split(r"\s", p.strip())
        passport = {}
        for part in parts:
            key, val = part.split(":")
            passport[key] = val
        passports.append(passport)
    del passport_strs, parts, passport, key, val


def is_valid(passport: dict, validation: dict) -> bool:
    if not set(passport.keys()).issuperset(set(validation.keys())):
        return False
    for key, rule in validation.items():
        if not rule(passport[key]):
            return False
    return True


def isint(x):
    return re.match(r"^\d+$", x)


def valid_hgt(hgt_str: str):
    if hgt_str[-2:] == "cm":
        min_hgt = 150
        max_hgt = 193
    elif hgt_str[-2:] == "in":
        min_hgt = 59
        max_hgt = 76
    else:
        return False

    hgt_str = hgt_str[:-2]
    return isint(hgt_str) and min_hgt <= int(hgt_str) <= max_hgt


colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

validation = {
    "byr": lambda x: isint(x) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: isint(x) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: isint(x) and 2020 <= int(x) <= 2030,
    "hgt": valid_hgt,
    "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x),
    "ecl": lambda x: x in colors,
    "pid": lambda x: isint(x) and len(x) == 9
}

print(sum([is_valid(x, validation) for x in passports]))
