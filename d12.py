from collections import Counter, defaultdict
from functools import cache, lru_cache
from pprint import pprint
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
    total = 0

    visited = set()

    def get_perimeter(region):
        total = 0
        for r, c in region:
            for nr, nc in get_neighbors(r, c):
                if not (
                    0 <= nr < len(inp) and 0 <= nc < len(inp[0]) and (nr, nc) in region
                ):
                    total += 1
        return total

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if (r, c) in visited:
                continue

            region = set()
            queue = [(r, c)]
            while queue:
                cr, cc = queue.pop(0)
                region.add((cr, cc))

                for nr, nc in get_neighbors(cr, cc):
                    if ((nr, nc) not in visited) and (
                        0 <= nr < len(inp)
                        and 0 <= nc < len(inp)
                        and inp[cr][cc] == inp[nr][nc]
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            print(
                inp[list(region)[0][0]][list(region)[0][1]],
                len(region),
                get_perimeter(region),
            )
            total += len(region) * get_perimeter(region)

    return total


def p2(inp):
    total = 0

    visited = set()

    def get_sides(region):
        edges = defaultdict(set)
        for r, c in region:
            for nr, nc in get_neighbors(r, c):
                if not (
                    0 <= nr < len(inp) and 0 <= nc < len(inp[0]) and (nr, nc) in region
                ):
                    direction = (nr - r, nc - c)
                    edges[direction].add((r, c))

        # join in adjacent edges
        sides = 0
        for direction in edges:
            while edges[direction]:
                queue = [edges[direction].pop()]
                while queue:
                    r, c = queue.pop(0)
                    for nr, nc in get_neighbors(r, c):
                        if (nr, nc) in edges[direction]:
                            queue.append((nr, nc))
                            edges[direction].remove((nr, nc))
                sides += 1

        return sides

    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if (r, c) in visited:
                continue

            region = set()
            queue = [(r, c)]
            while queue:
                cr, cc = queue.pop(0)
                region.add((cr, cc))

                for nr, nc in get_neighbors(cr, cc):
                    if ((nr, nc) not in visited) and (
                        0 <= nr < len(inp)
                        and 0 <= nc < len(inp)
                        and inp[cr][cc] == inp[nr][nc]
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            # print(
            #     inp[list(region)[0][0]][list(region)[0][1]],
            #     len(region),
            #     get_perimeter(region),
            # )

            total += len(region) * get_sides(region)

    return total


if __name__ == "__main__":
    with open("d12_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d12.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
