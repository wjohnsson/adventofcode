import re

lines = [line.strip() for line in open('input').readlines()]


class Card:
    def __init__(self, winning, numbers):
        self.winning = set(winning)
        self.numbers = set(numbers)
        self.copies = 1

    def matches(self):
        return len(self.winning & self.numbers)

    def points(self):
        return int(2 ** (self.matches() - 1))


def main():
    cards = parse_cards()
    print('Part 1', sum(card.points() for card in cards))
    create_copies(cards)
    print('Part 2', sum(card.copies for card in cards))


def parse_cards():
    cards = []
    for line in lines:
        parts = line.split('|')
        winning = re.findall(r'(\d+) ', parts[0])
        nums = re.findall(r'(\d+)', parts[1])

        cards.append(Card(winning, nums))
    return cards


def create_copies(cards):
    for i, card in enumerate(cards):
        start = min(i + 1, len(cards) - 1)
        end = min(start + card.matches(), len(cards))
        for j in range(start, end):
            cards[j].copies += card.copies


if __name__ == "__main__":
    main()
