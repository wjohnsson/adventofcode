import re
from numpy import uint16

wires, known_signals = {}, {}


def main():
    global wires, known_signals
    wires = init_wires()

    print("Part 1:", signal("a"))  # 46065

    # Override and reset
    wires["b"] = "46065 -> b"
    known_signals = {}
    print("Part 2:", signal("a"))  # 14134


def init_wires():
    input_lines = open("input").read().splitlines()
    ws = {}
    for line in input_lines:
        w = re.findall(r"-> (\w+)", line).pop()
        ws[w] = line
    return ws


def signal(wire):
    """
    Recursively traverse the circuit (a computation graph).
    """
    global wires, known_signals

    if wire not in wires:
        # It's a constant signal (leaf in the graph)
        return uint16(wire)
    # A wire's signal may be used multiple times, have we already calculated its value?
    if wire in known_signals:
        return known_signals[wire]

    line = wires[wire]
    parts = line.split(" ")
    s = 0  # signal
    if len(parts) == 3:
        s = signal(parts[0])

    elif "NOT" in line:
        s = ~signal(parts[1])

    # Binary operators
    left, right = parts[0], parts[2]
    if "AND" in line:
        s = signal(left) & signal(right)

    elif "OR" in line:
        s = signal(left) | signal(right)

    elif "RSHIFT" in line:
        s = signal(left) >> signal(right)

    elif "LSHIFT" in line:
        s = signal(left) << signal(right)

    known_signals[wire] = s
    return s


if __name__ == "__main__":
    main()
