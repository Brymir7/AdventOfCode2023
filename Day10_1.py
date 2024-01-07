import math
import sys

sys.setrecursionlimit(1000000)
_input = None
with open("inputs/10.txt", "r") as f:
    _input = f.read()
_input = _input.split("\n")

# def dfs(
#     matrix, curr_pos_x, curr_pos_y, min_x, max_x, min_y, max_y, prev_symbol, currLength, maxLength
# ):
#     if not matrix[curr_pos_y][curr_pos_x].isdigit():
#         return currLength

#     res = False
#     offsets = [
#         (0, -1),
#         (0, 1),
#         (1, 0),
#         (-1, 0),
#         (1, 1),
#         (-1, -1),
#         (-1, 1),
#         (1, -1),
#     ]
#     assert(len(set(offsets)) == len(offsets))
#     for offset_x, offset_y in offsets:
#         if (
#             curr_pos_x + offset_x < min_x
#             or curr_pos_x + offset_x >= max_x
#             or curr_pos_y + offset_y < min_y
#             or curr_pos_y + offset_y >= max_y
#         ):
#             continue
#         if matrix[curr_pos_y + offset_y][curr_pos_x + offset_x] != symbol and not matrix[curr_pos_y + offset_y][curr_pos_x + offset_x].isdigit():
#             res = True
#             break
#     return res

# DOWN, UP, LEFT, RIGHT
valid_direction_into_pipe_mapping = {
    "S": ["L", "R", "D", "U"],
    "L": ["D", "L"],
    "J": ["D", "R"],
    "7": ["U", "R"],
    "F": ["U", "L"],
    "-": ["L", "R"],
    "|": ["U", "D"],
}

valid_directions_out_of_pipe_mapping = {
    "S": ["L", "R", "D", "U"],
    "L": ["U", "R"],
    "J": ["U", "L"],
    "7": ["D", "L"],
    "F": ["D", "R"],
    "-": ["R", "L"],
    "|": ["D", "U"],
}


def convert_input_to_matrix(_input):
    matrix = []
    for line in _input:
        matrix.append(list(line))
    return matrix


def check_valid_path(currPos: tuple, direction: str, max_x, max_y) -> bool:
    curr_x, curr_y = currPos
    if direction == "D":
        if curr_y + 1 >= max_y:
            return False
        else:
            valid_input_to_next_pipe = valid_direction_into_pipe_mapping[
                matrix[curr_y + 1][curr_x]
            ]
            if direction in valid_input_to_next_pipe:
                return True
    if direction == "U":
        if curr_y - 1 < 0:
            return False
        else:
            valid_input_to_next_pipe = valid_direction_into_pipe_mapping[
                matrix[curr_y - 1][curr_x]
            ]
            if direction in valid_input_to_next_pipe:
                return True
    if direction == "L":
        if curr_x - 1 < 0:
            return False
        else:
            valid_input_to_next_pipe = valid_direction_into_pipe_mapping[
                matrix[curr_y][curr_x - 1]
            ]
            if direction in valid_input_to_next_pipe:
                return True
    if direction == "R":
        if curr_x + 1 >= max_x:
            return False
        else:
            valid_input_to_next_pipe = valid_direction_into_pipe_mapping[
                matrix[curr_y][curr_x + 1]
            ]
            if direction in valid_input_to_next_pipe:
                return True


matrix = convert_input_to_matrix(_input)
res = 0
starting_tuple_position = ()
for y_pos in range(0, len(matrix)):
    for x_pos in range(0, matrix[y_pos].__len__()):
        if matrix[y_pos][x_pos] == "S":
            starting_tuple_position = (x_pos, y_pos)
            break


def dfs(curr_x, curr_y, matrix, visited, positions, currMaxPipeLength):
    if (curr_x, curr_y) in visited:
        return
    visited.add((curr_x, curr_y))
    positions.append(matrix[curr_y][curr_x])
    valid_directions = valid_directions_out_of_pipe_mapping[matrix[curr_y][curr_x]]
    for direction in valid_directions:
        if check_valid_path((curr_x, curr_y), direction, len(matrix[0]), len(matrix)):
            if direction == "D":
                next_x, next_y = curr_x, curr_y + 1
            elif direction == "U":
                next_x, next_y = curr_x, curr_y - 1
            elif direction == "L":
                next_x, next_y = curr_x - 1, curr_y
            elif direction == "R":
                next_x, next_y = curr_x + 1, curr_y
            dfs(next_x, next_y, matrix, visited, positions, currMaxPipeLength + 1)


positions_to_explore = [(starting_tuple_position[0], starting_tuple_position[1])]
visited = set()
currMaxPipeLength = 0
positions = []

while positions_to_explore:
    curr_x, curr_y = positions_to_explore.pop()
    dfs(curr_x, curr_y, matrix, visited, positions, currMaxPipeLength)

print(len(positions)//2)