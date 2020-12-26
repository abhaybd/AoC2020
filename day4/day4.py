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


def is_valid(passport: dict, req: list) -> bool:
    return set(passport.keys()).issuperset(set(req))


print(sum([is_valid(x, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) for x in passports]))
