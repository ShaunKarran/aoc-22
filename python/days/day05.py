from copy import deepcopy

from parse import *


def read_input(filename: str):
    stack_input = []
    move_input = []
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            if line == "":
                stack_input.pop()
            elif line.startswith("move"):
                move_input.append(line)
            else:
                stack_input.append(line)

    return stack_input, move_input


def parse_stacks(stack_input):
    stack_columns = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in stack_input:
        for i, column in enumerate(stack_columns):
            if len(line) > column and line[column] and line[column] != " ":
                stacks[i].insert(0, line[column])

    return stacks


def parse_moves(moves_input):
    moves = []
    for line in moves_input:
        result = parse("move {:d} from {:d} to {:d}", line)
        moves.append((result[0], result[1] - 1, result[2] - 1))
    
    return moves


def part_a(stacks, moves) -> int:
    for number, from_index, to_index in moves:
        from_stack = stacks[from_index]
        to_stack = stacks[to_index]

        for _ in range(number):
            if from_stack:
                to_stack.append(from_stack.pop())

    return "".join([stack[-1] for stack in stacks])


def part_b(stacks, moves) -> int:
    for number, from_index, to_index in moves:
        from_stack = stacks[from_index]
        to_stack = stacks[to_index]

        to_move = []
        for _ in range(number):
            if from_stack:
                to_move.append(from_stack.pop())
        for crate in reversed(to_move):
            to_stack.append(crate)
    
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    stack_input, move_input = read_input("input/day05.txt")
    stacks = parse_stacks(stack_input)
    moves = parse_moves(move_input)
    print(f"Part A: {part_a(deepcopy(stacks), moves)}")
    print(f"Part B: {part_b(deepcopy(stacks), moves)}")
