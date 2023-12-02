import re
from collections import namedtuple

lines = open('input').readlines()
Game = namedtuple('Game', 'red green blue')
max_allowed = {'red': 12, 'green': 13, 'blue': 14}


def get_number_of_cubes(game, color):
    return [int(count) for count in re.findall(rf'(\d+) {color}', game)]


def is_possible(game: Game):
    return all(max(counts) <= max_allowed[color] for color, counts in game._asdict().items())


games = []
for line in lines:
    reds = get_number_of_cubes(line, 'red')
    greens = get_number_of_cubes(line, 'green')
    blues = get_number_of_cubes(line, 'blue')
    games.append(Game(reds, greens, blues))

print('Part 1:', sum(i + 1 for i, game in enumerate(games) if is_possible(game)))
print('Part 2:', sum(max(game.red) * max(game.green) * max(game.blue) for game in games))
