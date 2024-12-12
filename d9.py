from collections import defaultdict
import re
from copy import deepcopy

from tqdm import tqdm

from itertools import *


def p1(inp):
    ids = []
    curr = 0

    disk = True
    for x in inp[0]:
        if disk:
            ids.extend([curr] * int(x))
            curr += 1
        else:
            ids.extend([None] * int(x))

        disk = not disk

    # find first free
    first_free = 0
    while ids[first_free] is not None:
        first_free += 1

    last_id = len(ids) - 1
    while ids[last_id] is None:
        last_id -= 1

    while last_id > first_free:
        if ids[last_id] is None:
            last_id -= 1
            continue

        if ids[first_free] is None:
            ids[first_free] = ids[last_id]
            ids[last_id] = None
            first_free += 1
            last_id -= 1
        else:
            first_free += 1

    return sum(i * val for i, val in enumerate(ids) if val is not None)


def convert(intervals, free):
    length = max(max(t[1] for t in intervals.values()), max(t[1] for t in free))

    disk = [None] * length

    for curr, interval in intervals.items():
        for i in range(interval[0], interval[1]):
            disk[i] = curr

    return disk


def p2(inp):
    curr_id = 0
    pos = 0

    intervals = {}  # semi-open intervals
    free = []

    disk = True
    for x in inp[0]:
        if disk:
            intervals[curr_id] = (pos, pos + int(x))
            curr_id += 1
        else:
            free.append((pos, pos + int(x)))
        pos += int(x)

        disk = not disk

    for curr in range(curr_id - 1, -1, -1):
        length = intervals[curr][1] - intervals[curr][0]
        for i, span in enumerate(free):
            if span[0] >= intervals[curr][0]:
                break
            if span[1] - span[0] >= length:
                intervals[curr] = (span[0], span[0] + length)
                if span[0] + length == span[1]:
                    free.remove(span)
                elif span[0] + length < span[1]:
                    free[i] = (span[0] + length, span[1])
                break

        # print("".join("." if i is None else str(i) for i in convert(intervals, free)))

    total = 0
    for curr, (start, end) in intervals.items():
        total += sum(curr * i for i in range(start, end))

    return total


if __name__ == "__main__":
    with open("d9_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d9.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
