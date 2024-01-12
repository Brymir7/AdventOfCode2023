import math
import sys
from collections import deque

sys.setrecursionlimit(1000000)
_input = None
with open("inputs/10.txt", "r") as f:
    _input = f.read()
_input = _input.split("\n")

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


def dfs_without_revisiting(
    curr_x, curr_y, matrix, visited, positions, currMaxPipeLength
):
    if (curr_x, curr_y) in visited:
        return
    visited.add((curr_x, curr_y))
    positions.append((curr_x, curr_y))
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
            dfs_without_revisiting(
                next_x, next_y, matrix, visited, positions, currMaxPipeLength + 1
            )


def adjust_border_positions(curr_x, curr_y, border_positions):
    if f"max_y_for{curr_x}" not in border_positions:
        border_positions[f"curr_x{curr_x}"] = curr_x

    border_positions["MAX_X"] = max(border_positions["MAX_X"], curr_x)
    border_positions["MAX_Y"] = max(border_positions["MAX_Y"], curr_y)
    border_positions["MIN_X"] = min(border_positions["MIN_X"], curr_x)
    border_positions["MIN_Y"] = min(border_positions["MIN_Y"], curr_y)


def raytrace_polygon(curr_x, curr_y, matrix, pipe_positions):
    number_of_intersections = 0

    for x_pos in range(curr_x):
        if (x_pos, curr_y) not in pipe_positions:
            continue
        if matrix[curr_y][x_pos] in ["J", "L", "|", 'S']:
            number_of_intersections += 1

    return number_of_intersections


positions_to_explore = [(starting_tuple_position[0], starting_tuple_position[1])]
visited = set()
currMaxPipeLength = 0
positions = []

while positions_to_explore:
    curr_x, curr_y = positions_to_explore.pop()
    dfs_without_revisiting(
        curr_x, curr_y, matrix, visited, positions, currMaxPipeLength
    )
# Day 01 result
# print(len(positions) // 2)

valid_tiles = 0
for y_pos in range(0, len(matrix)):
    for x_pos in range(0, matrix[y_pos].__len__()):
        if (x_pos, y_pos) in positions:
            continue
        if raytrace_polygon(x_pos, y_pos, matrix, set(positions)) % 2 == 1:
            valid_tiles += 1

print(valid_tiles)
