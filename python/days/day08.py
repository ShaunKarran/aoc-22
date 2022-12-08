
def read_input(filename: str):
    map = []
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            map.append([int(c) for c in line])

    return map


def get_column(map, i):
    return [row[i] for row in map]


def part_a(map) -> int:    
    height = len(map)
    width = len(map[0])
    num_visible = (height * 2) + ((width - 2) * 2)

    for row_index, row in enumerate(map):
        if row_index == 0 or row_index == len(map) - 1:
            continue

        for column_index, tree in enumerate(row):
            if column_index == 0 or column_index == len(map[0]) - 1:
                continue

            trees_left = row[:column_index]
            trees_right = row[column_index + 1:]
            column = get_column(map, column_index)
            trees_top = column[:row_index]
            trees_bottom = column[row_index + 1:]
            if (
                all(other < tree for other in trees_left)
                or all(other < tree for other in trees_right)
                or all(other < tree for other in trees_top)
                or all(other < tree for other in trees_bottom)
            ):
                num_visible += 1

    return num_visible

def part_b(map) -> int:
    max_score = 0
    for row_index, row in enumerate(map):
        for column_index, tree in enumerate(row):
            trees_left = row[:column_index]
            trees_right = row[column_index + 1:]
            column = get_column(map, column_index)
            trees_top = column[:row_index]
            trees_bottom = column[row_index + 1:]

            score_left = 0
            for other in trees_left[::-1]:
                score_left += 1
                if other >= tree:
                    break

            score_right = 0
            for other in trees_right:
                score_right += 1
                if other >= tree:
                    break
                    
            score_top = 0
            for other in trees_top[::-1]:
                score_top += 1
                if other >= tree:
                    break

            score_bottom = 0
            for other in trees_bottom:
                score_bottom += 1
                if other >= tree:
                    break
            
            max_score = max(max_score, score_left * score_right * score_top * score_bottom)
    return max_score


if __name__ == "__main__":
    map = read_input("../input/day08.txt")
    print(f"Part A: {part_a(map)}")
    print(f"Part B: {part_b(map)}")
