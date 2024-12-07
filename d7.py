import re
from copy import deepcopy

from tqdm import tqdm

from itertools import *


def eval_expr(nums, ops):
    val = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            val += nums[i + 1]
        elif ops[i] == "*":
            val *= nums[i + 1]
        else:
            val = int(str(val) + str(nums[i + 1]))
    return val


def p1(inp):
    res = 0
    for line in tqdm(inp):
        val, nums = line.split(": ")
        val = int(val)
        nums = [int(x) for x in nums.split(" ")]

        for combo in product("+*", repeat=len(nums) - 1):
            if eval_expr(nums, combo) == val:
                res += val
                break

    return res


def p2(inp):
    res = 0
    for line in tqdm(inp):
        val, nums = line.split(": ")
        val = int(val)
        nums = [int(x) for x in nums.split(" ")]

        for combo in product("+*|", repeat=len(nums) - 1):
            if eval_expr(nums, combo) == val:
                res += val
                break

    return res


if __name__ == "__main__":
    with open("d7_test.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(TEST DATA) Part 1:", p1(puzzle_input))
    print("(TEST DATA) Part 2:", p2(puzzle_input))

    breakpoint()

    with open("d7.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("(REAL DATA) Part 1:", p1(puzzle_input))
    print("(REAL DATA) Part 2:", p2(puzzle_input))
