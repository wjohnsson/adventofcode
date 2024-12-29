from typing import List
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict
from itertools import pairwise

class SideType(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

@dataclass
class Side():
    x: int
    y: int
    type: SideType

@dataclass(frozen=True)
class Node:
    x: int
    y: int
    sides: List[Side]

@dataclass
class Region:
    char: str
    nodes: List[Node]
    
    def price(self):
        area = len(self.nodes)
        perimiter = sum(len(node.sides) for node in self.nodes)
        return area * perimiter
    
    @staticmethod
    def count_line_segments(values):
        return sum(1 for a, b in pairwise(sorted(values)) if b - a > 1) + 1
    
    def count_lines(self):
        sides = [side for node in self.nodes for side in node.sides]

        sides_on_same_line = defaultdict(list)
        for side in sides:
            if side.type in [SideType.LEFT, SideType.RIGHT]:
                sides_on_same_line[(side.x, side.type)].append(side.y)
            else:
                sides_on_same_line[(side.y, side.type)].append(side.x)

        return sum(self.count_line_segments(points) for points in sides_on_same_line.values())

    def discount_price(self):
        area = len(self.nodes)
        lines = self.count_lines()
        return area * lines


def find_region(char, x, y) -> List[Node]:
    """Flood fill using recursion and DFS"""
    nodes = []
    sides = []
    seen.add((x, y))
    for dx, dy, side_type in directions:
        new_x, new_y = x + dx, y + dy
        in_bounds = 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)
        in_region = in_bounds and grid[y][x] == grid[new_y][new_x]
        if in_region:
            if (new_x, new_y) not in seen:
                nodes += find_region(char, new_x, new_y)
        else:
            sides.append(Side(new_x, new_y, side_type))

    nodes.append(Node(x, y, sides))
    return nodes


grid = open("input").read().splitlines()

directions = [
    (0, -1, SideType.UP),
    (1, 0, SideType.RIGHT),
    (0, 1, SideType.DOWN),
    (-1, 0, SideType.LEFT)
]

seen = set()
regions = []
for y, row in enumerate(grid):
    for x, char in enumerate(grid[y]):
        if (x, y) not in seen:
            regions.append(Region(char, find_region(char, x, y)))


print("Part 1", sum(region.price() for region in regions))
print("Part 2", sum(region.discount_price() for region in regions))