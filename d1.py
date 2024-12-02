from collections import Counter


def p1(inp):
    pairs = [[int(x) for x in line.split("   ")] for line in inp]
    lefts, rights = zip(*pairs)

    return sum(abs(b - a) for a, b in zip(sorted(lefts), sorted(rights)))


def p2(inp):
    pairs = [[int(x) for x in line.split("   ")] for line in inp]
    lefts, rights = zip(*pairs)

    rights = Counter(rights)

    return sum(l * rights.get(l, 0) for l in lefts)


if __name__ == "__main__":
    with open("d1.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("Part 1:", p1(puzzle_input))
    print("Part 2:", p2(puzzle_input))
