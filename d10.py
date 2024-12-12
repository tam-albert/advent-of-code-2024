from collections import defaultdict
import re
from copy import deepcopy

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
    inp = [[int(x) for x in line] for line in inp]

    score = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == 0:
                # trailhead
                queue = [(i, j)]
                visited = set()

                while queue:
                    x, y = queue.pop(0)

                    if (x, y) not in visited and inp[x][y] == 9:
                        score += 1

                    visited.add((x, y))
                    for neighbor in get_neighbors(x, y):
                        nx, ny = neighbor
                        if nx >= 0 and nx < len(inp) and ny >= 0 and ny < len(inp[i]):
                            if inp[nx][ny] == inp[x][y] + 1 and neighbor not in visited:
                                queue.append(neighbor)

    return score


def p2(inp):
    inp = [[int(x) for x in line] for line in inp]

    rating = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == 0:
                # trailhead
                queue = [((i, j),)]
                visited = set()

                while queue:
                    path = queue.pop(0)
                    if path not in visited and inp[path[-1][0]][path[-1][1]] == 9:
                        rating += 1

                    visited.add(path)

                    x, y = path[-1]
                    for neighbor in get_neighbors(x, y):
                        nx, ny = neighbor
                        if nx >= 0 and nx < len(inp) and ny >= 0 and ny < len(inp[i]):
                            if inp[nx][ny] == inp[x][y] + 1 and neighbor not in visited:
                                queue.append((*path, neighbor))

    return rating


if __name__ == "__main__":
    with open("d10_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d10.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
