
OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def read_input(filename: str):
    input = {}

    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            monkey, expr = line.split(": ")
            input[monkey] = expr

    return input


def eval_expr(monkey: str, input: dict) -> int:
    expr = input[monkey]
    try:
        return int(expr)
    except ValueError:
        monkey_a, op, monkey_b = expr.split(" ")
        a = eval_expr(monkey_a, input)
        b = eval_expr(monkey_b, input)
        return int(OPERATIONS[op](a, b))


def part_a(input) -> int:
    return eval_expr("root", input)


def part_b(input) -> int:
    return 0


if __name__ == "__main__":
    input = read_input("../input/day21_test.txt")
    print(f"Part A: {part_a(input)}")
    print(f"Part B: {part_b(input)}")
