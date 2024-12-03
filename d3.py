import re


def p1(inp):
    res = 0
    for line in inp:
        items = re.findall(r"mul\(\d+,\d+\)", line)

        for item in items:
            item = item.split(",")
            item1 = item[0][4:]
            item2 = item[-1][:-1]

            if len(item1) > 3 or len(item2) > 3:
                continue

            res += int(item1) * int(item2)

    return res


def p2(inp):
    res = 0

    active = True
    for line in inp:

        dos = [x.start() for x in re.finditer(r"do\(\)", line)]
        donts = [x.start() for x in re.finditer(r"don't\(\)", line)]

        changes = [(i, True) for i in dos] + [(i, False) for i in donts]
        changes.sort()

        print(changes)

        for item in re.finditer(r"mul\(\d+,\d+\)", line):
            while changes and item.start() > changes[0][0]:
                _, active = changes.pop(0)

            if not active:
                continue

            item = item.group(0).split(",")
            item1 = item[0][4:]
            item2 = item[-1][:-1]

            if len(item1) > 3 or len(item2) > 3:
                continue

            res += int(item1) * int(item2)

    return res


if __name__ == "__main__":
    with open("d3.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("Part 1:", p1(puzzle_input))
    print("Part 2:", p2(puzzle_input))
