# n_body_problem.py
# solution to https://adventofcode.com/2019/day/12

from re import findall
from math import gcd
from functools import reduce


class Moon():
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]

    def apply_gravity(self, moons):
        for moon in moons:
            for i, p in enumerate(self.pos):
                if p < moon.pos[i]:
                    self.vel[i] += 1
                elif p > moon.pos[i]:
                    self.vel[i] -= 1

    def move(self):
        for i, v in enumerate(self.vel):
            self.pos[i] += v

    def periods_found(self):
        return all(self.periods)

    def pot_energy(self):
        return sum(map(abs, self.pos))

    def kin_energy(self):
        return sum(map(abs, self.vel))

    def __repr__(self):
        p, v = self.pos, self.vel
        return "pos=<x={:>3}, y={:>3}, z={:>3}>, ".format(p[0], p[1], p[2]) + \
            "vel=<x={:>3}, y={:>3}, z={:>3}>".format(v[0], v[1], v[2])


def state(moons):
    return [tuple([(moon.pos[i], moon.vel[i]) for moon in moons])
            for i in range(3)]


def simulate(moons, steps=1000):
    te = 0  # for part 1

    # periodicity means the first state will be repeated first
    initial_state = state(moons)
    periods = [None, None, None]
    for step in range(steps):
        if all(periods):
            break

        for moon in moons:
            moon.apply_gravity(moons)
        for moon in moons:
            moon.move()
        if step + 1 == 1000:
            te = total_energy(moons)

        for i, s in enumerate(state(moons)):
            if s == initial_state[i] and not periods[i]:
                periods[i] = step + 1
    return te, periods


def total_energy(moons):
    return sum([m.kin_energy() * m.pot_energy() for m in moons])


def lcm(nums):
    return reduce(lambda a, b: a*b // gcd(a, b), nums)


moons = [Moon(list(map(int, findall(r"-?\d+", line))))
         for line in open("input.txt").readlines()]

te, periods = simulate(moons, 1000000)

print(periods)

# Part 1
print(te)  # 7202

# Part 2
print(lcm(periods))  # 537881600740876
