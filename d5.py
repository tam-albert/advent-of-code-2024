import re


def p1(inp):
    for i, line in enumerate(inp):
        if line == "":
            break

    rules = inp[:i]
    updates = inp[i + 1 :]

    rules = [[int(pg) for pg in rule.split("|")] for rule in rules]

    res = 0

    for update in updates:
        update = [int(pg) for pg in update.split(",")]
        broken = False
        for a, b in rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    broken = True
                    break

        if not broken:
            print(update)
            res += update[len(update) // 2]

    return res


def p2(inp):
    for i, line in enumerate(inp):
        if line == "":
            break

    rules = inp[:i]
    updates = inp[i + 1 :]

    rules = [[int(pg) for pg in rule.split("|")] for rule in rules]
    updates = [[int(pg) for pg in update.split(",")] for update in updates]

    bad_updates = []

    for update in updates:
        broken = False
        for a, b in rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    broken = True
                    break

        if broken:
            bad_updates.append(update)

    for update in bad_updates:
        broken = True
        while broken:
            swapped = False
            for a, b in rules:
                if a in update and b in update:
                    if (ia := update.index(a)) > (ib := update.index(b)):
                        update[ia], update[ib] = update[ib], update[ia]
                        swapped = True
            if not swapped:
                broken = False

    res = 0
    for update in bad_updates:
        res += update[len(update) // 2]

    return res


if __name__ == "__main__":
    with open("d5.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("Part 1:", p1(puzzle_input))
    print("Part 2:", p2(puzzle_input))
