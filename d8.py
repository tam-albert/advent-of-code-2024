from collections import defaultdict
import re
from copy import deepcopy

from tqdm import tqdm

from itertools import *


def p1(inp):
    pos = defaultdict(list)

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] != ".":
                pos[inp[r][c]].append((r, c))

    antinodes = set()
    for item in pos:
        for r1, c1 in pos[item]:
            for r2, c2 in pos[item]:
                if (r1, c1) == (r2, c2):
                    continue

                # calculate antinodes
                delta = (r2 - r1, c2 - c1)

                antinodes.add((r1 - delta[0], c1 - delta[1]))
                antinodes.add((r2 + delta[0], c2 + delta[1]))

    cnt = 0
    for r, c in antinodes:
        if r < 0 or c < 0 or r >= len(inp) or c >= len(inp[0]):
            cnt += 1

    return len(antinodes) - cnt


def p2(inp):
    pos = defaultdict(list)

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] != ".":
                pos[inp[r][c]].append((r, c))

    antinodes = set()
    for item in pos:
        for r1, c1 in pos[item]:
            for r2, c2 in pos[item]:
                if (r1, c1) == (r2, c2):
                    continue

                # calculate antinodes
                delta = (r2 - r1, c2 - c1)

                nr2, nc2 = r2, c2
                while 0 <= nr2 < len(inp) and 0 <= nc2 < len(inp[0]):
                    antinodes.add((nr2, nc2))
                    nr2 += delta[0]
                    nc2 += delta[1]

                nr1, nc1 = r1, c1
                while 0 <= nr1 < len(inp) and 0 <= nc1 < len(inp[0]):
                    antinodes.add((nr1, nc1))
                    nr1 -= delta[0]
                    nc1 -= delta[1]

    return len(antinodes)


if __name__ == "__main__":
    with open("d8_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d8.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
