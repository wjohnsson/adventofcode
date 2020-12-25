import re

# Build all regexes with dynamic programming
memoized_rules = dict()
rules = dict()


def main():
    global memoized_rules, rules
    rule_lines, messages = (data.splitlines() for data in open("input").read().split("\n\n"))

    for rule in rule_lines:
        key, value = map(str.strip, rule.split(":"))
        rules[key] = value

    # Part 1
    matches = len([msg for msg in messages if re.fullmatch(regex_produced("0"), msg)])
    print(f"Part 1: {matches}")

    # Part 2
    # rules["8"] = "42 | 42 8"
    # rules["11"] = "42 31 | 42 11 31"
    rule_8 = f"({regex_produced('42')})+"
    rule_11 = expand_rule_11(regex_produced('42'),
                             regex_produced('31'),
                             4)  # 4 is enough to get the correct answer in my case
    regex = rule_8 + rule_11
    matches = len([msg for msg in messages if re.fullmatch(regex, msg)])
    print(f"Part 2: {matches}")


def regex_produced(rule_id):
    global memoized_rules, rules
    if rule_id in memoized_rules:
        return memoized_rules[rule_id]

    rule = rules[rule_id]
    if "|" in rule:
        # Rule ids on left and right sides of '|'
        left, right = map(lambda x: x.strip().split(" "), rule.split("|"))
        left = "".join(regex_produced(r) for r in left)
        right = "".join(regex_produced(r) for r in right)

        regex = "((" + left + ")|(" + right + "))"
        memoized_rules[rule_id] = regex
        return regex

    elif '"' in rule:
        char = rule[-2]
        regex = char
        memoized_rules[rule_id] = regex
        return regex

    else:
        regex = "".join(regex_produced(r) for r in rule.split(" "))
        memoized_rules[rule_id] = regex
        return regex


def expand_rule_11(rule_42, rule_31, n):
    """Hacky solution for expanding rule_11 n times."""

    # Woah that's some wacky f-strings! Here's an example:
    #   rule_42 = r"a"
    #   rule_31 = r"b"
    # Forms rule_11 like so
    #   ((a{1}b{1})|(a{2}b{2})|...(a{n}b{n}))
    rule_11 = ["("]
    for i in range(1, n):
        rule_11.append(f"({rule_42}{{{str(i)}}}{rule_31}{{{str(i)}}})")
        rule_11.append("|")

    rule_11.append(f"({rule_42}{{{str(n)}}}{rule_31}{{{str(n)}}})")
    rule_11.append(")")
    return "".join(rule_11)


if __name__ == "__main__":
    main()
