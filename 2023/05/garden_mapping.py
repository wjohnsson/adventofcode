import re
from typing import List, Set


def main():
    almanac = open('input').read()
    maps = parse_maps(almanac)

    # Part 1
    first_line = almanac.split('\n', maxsplit=1)[0]
    seeds = [int(seed) for seed in re.findall(r'(\d+)', first_line)]
    print('Part 1', min(locations(maps, seeds)))

    # Part 2
    seed_ranges = [range(start, start + length) for start, length in pairwise(seeds)]
    candidates = set()
    for garden_map in reversed(maps):
        garden_map.reverse_map(candidates)  # Undo the mapping for the current candidates, "moving up" a layer
        candidates.update(garden_map.boundaries())  # All range boundaries of this layer are potential best seeds

    # After moving backwards through the layers we have a set of candidate seeds
    # But first do some preprocessing, removing candidates that aren't in any of the initial ranges
    candidate_seeds = filter(lambda candidate: any(candidate in r for r in seed_ranges), candidates)
    print('Part 2', min(locations(maps, candidate_seeds)))


def pairwise(items):
    for item1, item2 in zip(items[::2], items[1::2]):
        yield item1, item2


def locations(maps, candidate_seeds):
    for seed in candidate_seeds:
        entity = seed
        for m in maps:
            entity = m[entity]
        location = entity  # after passing through all the maps we have a location
        yield location


class Range:
    def __init__(self, dest, source, length):
        self.source_start = source
        self.source_end = self.source_start + length - 1
        self.offset = dest - source

    def __contains__(self, point):
        return self.source_start <= point <= self.source_end

    def can_output(self, mapped_point: int):
        """Can the given point be in the output of this range?"""
        return self.map(self.source_start) <= mapped_point <= self.map(self.source_end)

    def map(self, point):
        return point + self.offset

    def reverse_map(self, mapped_point):
        """Apply the mapping, but in reverse, effectively moving up a layer"""
        return mapped_point - self.offset


class GardenMap:
    """One layer of the almanac"""

    def __init__(self):
        self.ranges: List[Range] = []

    def add_range(self, nums):
        self.ranges.append(Range(*nums))

    def __getitem__(self, point):
        """Find the relevant range, apply the map using this range"""
        for r in self.ranges:
            if point in r:
                return r.map(point)
        return point

    def reverse_map(self, candidates: Set[int]):
        """For a set of points, find the points in the upper layer that could have mapped to them.
           If a point does not exist in any range of the upper layer it will not be transformed."""
        new_candidates = set()
        for r in self.ranges:
            for mapped_point in candidates:
                if r.can_output(mapped_point):
                    new_candidates.add(r.reverse_map(mapped_point))
        candidates.update(new_candidates)

    def boundaries(self):
        boundaries = set()
        for r in self.ranges:
            boundaries.add(r.source_start)
            boundaries.add(r.source_end)
        return boundaries


def parse_maps(almanac) -> List[GardenMap]:
    maps = []
    for garden_map in almanac.split('\n\n')[1:]:
        gm = GardenMap()
        for line in garden_map.splitlines()[1:]:  # skip header
            nums = list(map(int, re.findall(r'(\d+)', line)))
            gm.add_range(nums)
        maps.append(gm)
    return maps


if __name__ == "__main__":
    main()
