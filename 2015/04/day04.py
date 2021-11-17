from hashlib import md5

secret = "bgvyzdsv"


def find_number(n_zeroes):
    found = False
    num = 0
    while not found:
        num += 1
        md5_hash = md5((secret + str(num)).encode("utf-8")).hexdigest()

        if md5_hash[:n_zeroes] == "0" * n_zeroes:
            found = True
    return num


print("Part 1:", find_number(5))  # 254575
print("Part 2:", find_number(6))  # 1038736
