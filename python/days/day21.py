
OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

INVERSE_OPERATIONS = {
    "+": lambda a, b: a - b,
    "-": lambda a, b: a + b,
    "*": lambda a, b: a / b,
    "/": lambda a, b: a * b,
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


def eval_expr_b(monkey: str, input: dict, results: dict) -> int:
    expr = input[monkey]
    try:
        return int(expr)
    except ValueError:
        monkey_a, op, monkey_b = expr.split(" ")
        a = eval_expr_b(monkey_a, input, results)
        b = eval_expr_b(monkey_b, input, results)
        results[monkey] = int(OPERATIONS[op](a, b))
        return results[monkey]


def part_b(input) -> int:
    # Pop root & human.
    root = input.pop("root")
    root_a, _, root_b = root.split(" ")
    humn = input.pop("humn")
    # Eval into results dict until hitting a key error.
    results = {}
    a = b = None
    try:
        a = eval_expr_b(root_a, input, results)
    except KeyError:
        b = eval_expr_b(root_b, input, results)

    from pprint import pprint
    pprint(results)

    # Find the monkey that depends on humn.
    m = next(k for k, expr in input.items() if "humn" in expr)
    # Use known values of the monkey and non-humn operand to calculate humn.
    _, op, m2 = input[m].split(" ")

    # return INVERSE_OPERATIONS[op](results[m], results[m2])
    return 0


if __name__ == "__main__":
    input = read_input("../input/day21_test.txt")
    print(f"Part A: {part_a(input)}")
    print(f"Part B: {part_b(input)}")
