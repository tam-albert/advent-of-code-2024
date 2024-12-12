from collections import Counter, defaultdict
from functools import cache, lru_cache
import re
from copy import copy, deepcopy

from tqdm import tqdm

from itertools import *


def get_neighbors(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def p1(inp):
    stones = [int(x) for x in inp[0].split(" ")]

    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(rep := str(stone)) % 2 == 0:
                left = rep[: len(rep) // 2]
                right = rep[len(rep) // 2 :]

                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)
        stones = copy(new_stones)
        # print(stones)
        # breakpoint()

    return len(stones)


@cache
def get_new_stone(stone):
    if stone == 0:
        return (1,)
    elif len(rep := str(stone)) % 2 == 0:
        left = rep[: len(rep) // 2]
        right = rep[len(rep) // 2 :]

        return int(left), int(right)
    else:
        return (stone * 2024,)


def p2(inp):
    stones = Counter([int(x) for x in inp[0].split(" ")])

    for _ in tqdm(range(75)):
        new_stones = Counter()
        for stone, val in stones.items():
            for new_stone in get_new_stone(stone):
                new_stones[new_stone] += val
        stones = copy(new_stones)

    return sum(stones.values())


if __name__ == "__main__":
    with open("d11_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d11.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
