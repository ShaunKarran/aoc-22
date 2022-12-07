from copy import deepcopy

from boltons.iterutils import windowed_iter


def read_input(filename: str):
    files = {"/": {}}
    current_dir = files["/"] 
    dir_stack = []
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            if line == "$ ls":
                pass
            elif line.startswith("$ cd"):
                cd_dir = line.split(" ")[2]
                if cd_dir == "..":
                    current_dir = dir_stack.pop()
                else:
                    dir_stack.append(current_dir)
                    current_dir = current_dir[cd_dir]
            elif line.startswith("dir"):
                dir_name = line.split(" ")[1]
                current_dir[dir_name] = {}
            else:
                file_size, file_name = line.split(" ")
                current_dir[file_name] = int(file_size)
    
    return files

def sum_dir(directory):
    sum = 0
    for k, v in directory.items():
        if isinstance(v, dict):
            sum += sum_dir(v)
        else:
            sum += v
    return sum


def part_a(files) -> int:
    def s(d):
        total = 0
        for k, v in d.items():
            if isinstance(v, dict):
                dir_sum = sum_dir(v)
                if sum_dir(v) < 100_000:
                    total += dir_sum
                total += s(v)
        return total

    return s(files)

def part_b(files) -> int:
    total_used_space = sum_dir(files)

    options = []
    def s(d):
        for k, v in d.items():
            if isinstance(v, dict):
                dir_sum = sum_dir(v)
                if (total_used_space - sum_dir(v)) < 40_000_000:
                    options.append(dir_sum)
                s(v)

    s(files)
    return min(options)

if __name__ == "__main__":
    files = read_input("../input/day07.txt")
    print(f"Part A: {part_a(files)}")
    print(f"Part B: {part_b(files)}")
