import json

from boltons.iterutils import chunked


def read_input(filename: str):
    input = []

    with open(filename, "r") as fp:
        for left, right, _ in chunked(fp, 3):
            # print(f"left: {left}")
            # print(f"right: {right}")
            input.append((json.loads(left), json.loads(right)))

    return input


def compare(left, right):
    print(f"compare {left}, {right}")
    if isinstance(left, int) and isinstance(right, int):
        result = left < right

    elif isinstance(left, list) and isinstance(right, list):
        result = any(compare(a, b) for a, b in zip(left, right))
        if result is False and len(left) < len(right):
            if not left:
                result = True
            elif right and left[-1] == right[-1]:
                result = True

    elif isinstance(left, int):
        left = [left]
        result = any(compare(a, b) for a, b in zip(left, right))

    elif isinstance(right, int):
        right = [right]
        result = any(compare(a, b) for a, b in zip(left, right))
    
    print(f"result {result}\n")
    return result


def part_a(input) -> int:
    return sum(i for i, (left, right) in enumerate(input, start=1) if compare(left, right))

def part_b(input) -> int:
    return 0


if __name__ == "__main__":
    input = read_input("../input/day13.txt")
    print(f"Part A: {part_a(input)}")
    print(f"Part B: {part_b(input)}")
