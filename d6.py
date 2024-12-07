import re
from copy import deepcopy

from tqdm import tqdm

mapping = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

next_direction = {(-1, 0): (0, 1), (1, 0): (0, -1), (0, -1): (-1, 0), (0, 1): (1, 0)}


def p1(inp):
    obstacles = set()

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] == "#":
                obstacles.add((r, c))
            elif inp[r][c] in ("^", "v", "<", ">"):
                loc = (r, c)
                direction = mapping[inp[r][c]]

    visited = {loc}
    while True:
        next_loc = (loc[0] + direction[0], loc[1] + direction[1])
        if (
            next_loc[0] < 0
            or next_loc[0] >= len(inp)
            or next_loc[1] < 0
            or next_loc[1] >= len(inp[0])
        ):
            return len(visited)
        if next_loc in obstacles:
            direction = next_direction[direction]
        else:
            visited.add(next_loc)
            loc = next_loc


def simulate(inp):
    obstacles = set()

    loc = None
    for r in range(len(inp)):
        for c in range(len(inp[0])):
            # print(inp[r][c])
            if inp[r][c] == "#":
                obstacles.add((r, c))
            elif inp[r][c] in ("^", "v", "<", ">"):
                loc = (r, c)
                direction = mapping[inp[r][c]]

    if loc is None:
        return 0
    visited = {loc}
    i = 0
    while i < len(inp) * len(inp[0]) * 10:
        next_loc = (loc[0] + direction[0], loc[1] + direction[1])
        if (
            next_loc[0] < 0
            or next_loc[0] >= len(inp)
            or next_loc[1] < 0
            or next_loc[1] >= len(inp[0])
        ):
            return len(visited)
        if next_loc in obstacles:
            direction = next_direction[direction]
        else:
            visited.add(next_loc)
            loc = next_loc
        i += 1
    return None


def p2(inp):
    cnt = 0
    for r in tqdm(range(len(inp))):
        for c in range(len(inp[0])):
            new_inp = deepcopy(inp)
            new_inp = [list(row) for row in new_inp]
            new_inp[r][c] = "#"
            if simulate(new_inp) is None:
                cnt += 1
    return cnt


if __name__ == "__main__":
    with open("d6_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    with open("d6.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
