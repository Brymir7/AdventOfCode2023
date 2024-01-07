_input = None
with open("inputs/03.txt", "r") as f:
    _input = f.read()
_input = _input.split("\n")


def check_around_position_for_other_than_symbol(
    matrix, curr_pos_x, curr_pos_y, min_x, max_x, min_y, max_y, symbol
):
    if not matrix[curr_pos_y][curr_pos_x].isdigit():
        print("error")

    res = False
    offsets = [
        (0, -1),
        (0, 1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
    ]
    assert(len(set(offsets)) == len(offsets))
    for offset_x, offset_y in offsets:
        if (
            curr_pos_x + offset_x < min_x
            or curr_pos_x + offset_x >= max_x
            or curr_pos_y + offset_y < min_y
            or curr_pos_y + offset_y >= max_y
        ):
            continue
        if matrix[curr_pos_y + offset_y][curr_pos_x + offset_x] != symbol and not matrix[curr_pos_y + offset_y][curr_pos_x + offset_x].isdigit():
            res = True
            break
    return res


def check_number_for_validity(matrix, list_of_positions) -> int:
    valid = False
    print(list_of_positions)
    res = 0
    for x_pos, y_pos in list_of_positions:
        if check_around_position_for_other_than_symbol(
            matrix,
            x_pos,
            y_pos,
            min_x=0,
            max_x=len(matrix[0]),
            min_y=0,
            max_y=len(matrix),
            symbol=".",
        ):
            valid = True
            break
    if valid:
        number = ""
        for x_pos, y_pos in list_of_positions:
            number += matrix[y_pos][x_pos]
        print(number)
        res = int(number)
    return res


def convert_input_to_matrix(_input):
    matrix = []
    for line in _input:
        matrix.append(list(line))
    return matrix


convert_input_to_matrix(_input)
print(convert_input_to_matrix(_input))
matrix = convert_input_to_matrix(_input)
res = 0
for y_pos in range(0, len(matrix)):
    accumulated_positions_with_number = []
    for x_pos in range(0, matrix[y_pos].__len__()):
        if not matrix[y_pos][x_pos].isdigit():
            if accumulated_positions_with_number != []:
                res += check_number_for_validity(
                    matrix, accumulated_positions_with_number
                )

            accumulated_positions_with_number = []
            continue
        accumulated_positions_with_number.append((x_pos, y_pos))


print(res)
