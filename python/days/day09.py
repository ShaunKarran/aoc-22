
def read_input(filename: str):
    input = []
    with open(filename, "r") as fp:
        for line in fp:
            direction, distance = line.strip().split(" ")
            if direction == "R":
                dir_vec = (1, 0)
            elif direction == "L":
                dir_vec = (-1, 0)
            elif direction == "U":
                dir_vec = (0, 1)
            elif direction == "D":
                dir_vec = (0, -1)

            input.append((dir_vec, distance))

    return input


def part_a(input) -> int:
    head = tail = (0, 0)

    def is_touching(a, b) -> bool:
        return (abs(b[0] - a[0]) <= 1) and (abs(b[1] - a[1]) <= 1)

    for direction, distance in input:
        for _ in range(distance):
            head[0] += direction[0]
            head[1] += direction[1]

        if not is_touching(head, tail):
            if direction[0] == 1:
                t

    return 0

def part_b(input) -> int:
    return 0


if __name__ == "__main__":
    input = read_input("../input/day09_test.txt")
    print(f"Part A: {part_a(input)}")
    print(f"Part B: {part_b(input)}")
