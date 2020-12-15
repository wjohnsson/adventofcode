def run(mem, add_candidates=False):
    candidates = []
    seen_pcs = set()
    acc = pc = 0
    while True:
        if pc in seen_pcs:  # we looped!
            return True, acc, candidates
        elif pc == len(mem):  # we have reached the end of the code
            return False, acc, candidates
        seen_pcs.add(pc)

        op, arg = mem[pc][:3], int(mem[pc][4:])
        if op == "nop" and add_candidates:
            candidates.append((pc, op))
        elif op == "acc":
            acc += arg
        elif op == "jmp":
            if add_candidates:
                candidates.append((pc, op))
            pc += arg
            continue
        pc += 1


def main():
    mem = list(map(str.strip, open("input").readlines()))

    # Part 1
    acc, candidates = run(mem, add_candidates=True)[1:]
    print(f"Part 1: {acc}")  # 1766

    # Part 2
    # candidates are the nop and jmp instructions that were performed in part one
    while candidates:
        pc, op = candidates.pop()
        old_mem = mem
        if op == "nop":
            mem[pc] = mem[pc].replace("nop", "jmp")
        elif op == "jmp":
            mem[pc] = mem[pc].replace("jmp", "nop")
        looped, acc = run(mem)[:2]

        if not looped:
            print(f"Part 2: {acc}")  # 1639
            break

        mem = old_mem


if __name__ == "__main__":
    main()
