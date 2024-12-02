def p1(inp):
    cnt = 0
    for line in inp:
        nums = [int(x) for x in line.split(" ")]

        if not (sorted(nums) == nums or sorted(nums, reverse=True) == nums):
            continue

        if not (
            all(abs(nums[i + 1] - nums[i]) in [1, 2, 3] for i in range(len(nums) - 1))
        ):
            continue

        cnt += 1
    return cnt


def test(arr):
    return (sorted(arr) == arr or sorted(arr, reverse=True) == arr) and all(
        abs(arr[i + 1] - arr[i]) in [1, 2, 3] for i in range(len(arr) - 1)
    )


def p2(inp):
    cnt = 0
    for line in inp:
        nums = [int(x) for x in line.split(" ")]

        for i in range(len(nums)):
            new_n = nums[:i] + nums[i + 1 :]
            if test(new_n):
                cnt += 1
                break

    return cnt


if __name__ == "__main__":
    with open("d2.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("Part 1:", p1(puzzle_input))
    print("Part 2:", p2(puzzle_input))
