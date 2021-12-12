from statistics import median

closes = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def main():
    inp = open('input').read().splitlines()

    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points_part2 = {')': 1, ']': 2, '}': 3, '>': 4}

    opens = {v: k for k, v in closes.items()}

    score = 0
    scores = []
    for chunk in inp:
        corrupted, char, stack = check_syntax(chunk)
        if corrupted:
            score += points[char]
        else:
            # Incomplete
            score_part2 = 0
            for char in stack[::-1]:
                score_part2 *= 5
                score_part2 += points_part2[opens[char]]
            scores.append(score_part2)

    print('Part 1:', score)  # 343863
    print('Part 2:', median(scores))  # 2924734236


def check_syntax(chunk):
    global closes

    stack = []
    for char in chunk:
        if char in closes.keys():
            if closes[char] != stack[-1]:
                # Chunk is corrupted
                return True, char, stack
            else:
                stack.pop()
        else:
            stack.append(char)
    # Chunk is incomplete
    return False, None, stack


if __name__ == '__main__':
    main()
