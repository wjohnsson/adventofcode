import re

# Parse and clean up input.
passports = []
for passport in open("input").read().split("\n\n"):
    passports.append(str.rstrip(passport).replace("\n", " "))


def format_passport(p):
    """
    Turns a passport formatted as a string such as:
      "pid:087499704 hgt:74in ecl:grn"
    into a dict:
      {pid: 087499704, hgt: 74in, ecl: grn}
    whose keys and values are strings.
    """
    formatted_passport = dict()
    for kv in p.split(" "):
        k, v = kv.split(":")
        formatted_passport[k] = v
    return formatted_passport


def valid_values(p):
    """Returns True if the passport has valid values according to part 2."""
    try:
        h = int(p["hgt"][:-2])  # height
        hu = p["hgt"][-2:]  # height unit
        return 1920 <= int(p["byr"]) <= 2002 \
            and 2010 <= int(p["iyr"]) <= 2020 \
            and 2020 <= int(p["eyr"]) <= 2030 \
            and ((hu == "cm" and 150 <= h <= 193) or (hu == "in" and 59 <= h <= 76)) \
            and re.fullmatch("#[0-9a-f]{6}", p["hcl"]) \
            and re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", p["ecl"]) \
            and re.fullmatch("[0-9]{9}", p["pid"])
    except (KeyError, ValueError):  # missing field or invalid height
        return False


# Count valid passports for part 1 and 2.
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # 'cid' omitted
valid_p1 = valid_p2 = 0
for passport in passports:
    if all([f in passport for f in fields]):
        valid_p1 += 1
        if valid_values(format_passport(passport)):
            valid_p2 += 1

print(f"Part 1: {valid_p1}")  # 222
print(f"Part 2: {valid_p2}")  # 140
