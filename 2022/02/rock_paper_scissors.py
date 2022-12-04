lines = open('input').read().split('\n')

rock, paper, scissors = 1, 2, 3 
loss, draw, win = 0, 3, 6

points_part_one = {
    'A X': draw + rock,
    'A Y': win + paper,
    'A Z': loss + scissors,

    'B X': loss + rock,
    'B Y': draw + paper,
    'B Z': win + scissors,

    'C X': win + rock,
    'C Y': loss + paper,
    'C Z': draw + scissors
}
print(sum(points_part_one[round] for round in lines))

points_part_two = {
    'A X': loss + scissors,
    'A Y': draw + rock,
    'A Z': win + paper,

    'B X': loss + rock,
    'B Y': draw + paper,
    'B Z': win + scissors,

    'C X': loss + paper,
    'C Y': draw + scissors,
    'C Z': win + rock
}
print(sum(points_part_two[round] for round in lines))