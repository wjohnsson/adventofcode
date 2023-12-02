import re

lines = open('input').readlines()
text_to_number_conversion = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def convert_number(x):
    if x.isnumeric():
        return x
    else:
        return text_to_number_conversion[x]


def sum_calibration_values(regex):
    summed_values = 0
    for line in lines:
        numbers = re.findall(regex, line)
        numbers = [convert_number(num) for num in numbers]
        summed_values += int(numbers[0] + numbers[-1])
    return summed_values


print('Part 1', sum_calibration_values(r"\d"))
print('Part 2', sum_calibration_values(r"(one|two|three|four|five|six|seven|eight|nine|\d)"))
