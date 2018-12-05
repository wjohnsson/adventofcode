def part_one(file_path):
    input_file = open(file_path)

    frequency_sum = 0;
    for line in input_file:
        # Assumes each line contains only a sign and a number.
        frequency_sum += int(line)

    input_file.close()
    return frequency_sum


def part_two(file_path):
    input_file = open(file_path)

    results = {0}
    frequency_sum = 0

    while True:
        for line in input_file:
            # Assumes each line contains only a sign and a number.
            frequency_sum += int(line)

            if frequency_sum not in results:
                results.add(frequency_sum)
            else:
                input_file.close()
                return frequency_sum
        # Start reading from beginning.
        input_file.seek(0)


print("Part one answer: " + str(part_one("frequencies.txt")))
print("Part two answer: " + str(part_two("frequencies.txt")))
