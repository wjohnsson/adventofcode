import re

commands = re.findall(r"(\w*) (\d*)", open("input").read())


def part1():
    deltas = {
        "forward": 1,
        "down": -1j,
        "up": 1j
    }

    pos = 0 + 0j
    for cmd, x in commands:
        pos += deltas[cmd] * int(x)
    return pos


def part2():
    sub = Sub()
    for cmd, x in commands:
        x = int(x)
        if cmd == "down":
            sub.down(x)
        elif cmd == "up":
            sub.up(x)
        elif cmd == "forward":
            sub.forward(x)
    return sub.pos


def answer(pos):
    return abs(int(pos.real * pos.imag))


class Sub:
    def __init__(self):
        self.pos = 0 + 0j
        self.aim = 0

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x

    def forward(self, x):
        self.pos += x + self.aim * x * 1j


print("Part 1:", answer(part1()))
print("Part 2:", answer(part2()))
