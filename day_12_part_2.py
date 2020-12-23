from day_12 import (
    test_data,
    process_data,
    get_data,
    north,
    east,
    south,
    west,
    forward,
    right,
    left,
)
import copy
from math import cos, sin, radians


# state keys
cx = "cx"  # current x
cy = "cy"  # current y
wx = "wx"  # waypoint x
wy = "wy"  # waypoint y


# reducer
# ----------------------
initial_state = {
    cx: 0,
    cy: 0,
    wx: 10,
    wy: 1,
}


def reducer(action=(None, None), state=initial_state):

    action_type, payload = action
    new_state = copy.deepcopy(state)

    if action_type == north:
        new_state[wy] += payload

    if action_type == south:
        new_state[wy] -= payload

    if action_type == east:
        new_state[wx] += payload

    if action_type == west:
        new_state[wx] -= payload

    if action_type == right:
        x, y = rotate_origin(
            [new_state[wx], new_state[wy]],
            radians(payload),
        )
        new_state[wx] = x
        new_state[wy] = y

    if action_type == left:
        x, y = rotate_origin(
            [new_state[wx], new_state[wy]],
            radians(-payload),
        )
        new_state[wx] = x
        new_state[wy] = y

    if action_type == forward:
        for i in range(payload):
            new_state[cx] += new_state[wx]
            new_state[cy] += new_state[wy]

    return new_state


# helpers
# ----------------------
def rotate_origin(point, radians):
    """Rotate a point around the origin (0, 0)"""
    x, y = point
    xx = x * cos(radians) + y * sin(radians)
    yy = -x * sin(radians) + y * cos(radians)
    return xx, yy


def get_manhattan_distance(state):
    return int(abs(state[cx]) + abs(state[cy]))


# implemention
# ----------------------

# 214 + 72 = 286
# print(get_manhattan_distance(process_data(test_data, reducer=reducer, log=True)))

# part 2
def part_two():
    print(get_manhattan_distance(process_data(get_data(), reducer=reducer, log=True)))


part_two()
