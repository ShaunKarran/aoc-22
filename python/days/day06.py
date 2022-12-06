from copy import deepcopy

from boltons.iterutils import windowed_iter


def read_input(filename: str):
    with open(filename, "r") as fp:
        return next(fp)

def part_a(input) -> int:
    for i, window in enumerate(windowed_iter(input, 4), start=4):
        if len(set(window)) == len(window):
            return i


def part_b(input) -> int:
    for i, window in enumerate(windowed_iter(input, 14), start=14):
        if len(set(window)) == len(window):
            return i

if __name__ == "__main__":
    input = read_input("../input/day06.txt")
    print(f"Part A: {part_a(input)}")
    print(f"Part B: {part_b(input)}")
