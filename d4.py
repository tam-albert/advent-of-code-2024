import re


def p1(inp):
    directions = [
        (+1, 0),
        (0, +1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    cnt = 0

    word = "XMAS"

    n_rows = len(inp)
    n_cols = len(inp[0])

    for r in range(n_rows):
        for c in range(n_cols):
            if inp[r][c] == "X":
                for dr, dc in directions:
                    broken = False
                    for i in range(1, 4):
                        nr, nc = r + dr * i, c + dc * i
                        if nr < 0 or nr >= n_rows or nc < 0 or nc >= n_cols:
                            broken = True
                            break

                        if inp[nr][nc] != word[i]:
                            broken = True
                            break
                    if not broken:
                        cnt += 1

    return cnt


def p2(inp):
    directions = [
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    cnt = 0

    n_rows = len(inp)
    n_cols = len(inp[0])

    for r in range(n_rows):
        for c in range(n_cols):
            if inp[r][c] == "A":
                print(r, c)
                broken = False
                chars = []

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= n_rows or nc < 0 or nc >= n_cols:
                        broken = True
                        break
                    chars.append(inp[nr][nc])

                if broken:
                    continue

                if tuple(chars) in (
                    ("M", "S", "M", "S"),
                    ("S", "M", "S", "M"),
                    ("S", "M", "M", "S"),
                    ("M", "S", "S", "M"),
                ):
                    cnt += 1

    return cnt


if __name__ == "__main__":
    with open("d4.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    print("Part 1:", p1(puzzle_input))
    print("Part 2:", p2(puzzle_input))
