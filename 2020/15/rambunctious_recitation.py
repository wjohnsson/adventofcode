def memory_game(end):
    global start

    last_spoken = dict()
    for turn, n in enumerate(start[:-1]):
        last_spoken[n] = turn + 1

    last_n = start[-1]
    for turn in range(len(start) + 1, end + 1):
        if last_n not in last_spoken:  # first time spoken
            speak = 0
        else:
            speak = turn - 1 - last_spoken[last_n]

        last_spoken[last_n] = turn - 1
        last_n = speak
    return last_n


start = [0, 3, 1, 6, 7, 5]
print(f"Part 1: {memory_game(2020)}")  # 852
print(f"Part 2: {memory_game(30000000)}")  # 6007666
