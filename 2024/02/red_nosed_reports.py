import re
from typing import List

lines = open('input').readlines()
reports = [list(map(int, re.findall("\d+", line))) for line in lines]

def is_safe(report):
    increasing = (report[1] - report[0]) > 0
    for a, b in zip(report, report[1:]):
        diff = abs(a - b)
        if diff < 1 or diff > 3:
            return False
        if (increasing and a > b) or (not increasing and a < b):
            return False
    return True

def dampen(report) -> List[List[int]]:
    dampened_reports = [report[:]]
    for i in range(len(report)):
        copy = report[:]
        del copy[i]
        dampened_reports.append(copy)
    return dampened_reports

print("Part 1 :", sum(1 for report in reports if is_safe(report)))
print("Part 2 :", sum(1 for report in reports if any(is_safe(dampened_reports) for dampened_reports in dampen(report))))