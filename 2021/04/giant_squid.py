import re
import numpy as np


def main():
    inp = open("input").read().split("\n\n")
    nums = [int(num) for num in inp[0].split(",")]

    # Split the rows inside a board
    boards = [s.rstrip().split("\n") for s in inp[1:]]
    # Split into digits
    boards = [[re.findall(r"\d+", s) for s in ll] for ll in boards]
    # Turn strings into ints
    boards = [[list(map(int, ll)) for ll in board] for board in boards]
    # Numpy ftw
    boards = [np.array(board) for board in boards]

    print("Part 1:", score_of_best_board(nums, boards))  # 31424
    print("Part 2:", score_of_last_board(nums, boards))  # 23042


# Part 1
def score_of_best_board(nums, boards):
    for i in range(len(nums)):
        drawn = nums[:i + 1]
        for board in boards:
            if win(board, drawn) or win(board.T, drawn):
                return score(board, drawn)

    raise ValueError("No one wins at bingo today")


# Part 2
def score_of_last_board(nums, boards):
    boards = np.array(boards)  # for filtering boards
    i = 0
    # Play until one board left
    while len(boards) > 1:
        drawn = nums[:i + 1]
        mask = [not (win(board, drawn) or win(board.T, drawn)) for board in boards]
        boards = boards[mask]
        i += 1

    # Play until the last board wins
    board = boards[0]
    for i in range(i, len(nums)):
        drawn = nums[:i + 1]
        if win(board, drawn) or win(board.T, drawn):
            return score(board, drawn)


def score(board, drawn):
    mask = np.isin(board, drawn, invert=True)
    return sum(board[mask]) * drawn[-1]


def win(board, drawn):
    for row in board:
        if np.isin(row, drawn).all():
            return True
    return False


if __name__ == "__main__":
    main()
