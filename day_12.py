# data
# ----------------------


def get_data(filename="day_12_data.txt"):
    for line in open(filename, "r"):
        yield line.strip()


test_data = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]

code_splitter = lambda x: (x[0], int(x[1:]))

# actions
# ----------------------
north = "N"
east = "E"
south = "S"
west = "W"
forward = "F"
right = "R"
left = "L"

# state keys
orientation = "orientation"
x = "x"
y = "y"

# reducer
# ----------------------
initial_state = {
    north: 0,
    east: 0,
    south: 0,
    west: 0,
    orientation: 90,  # start east facing
}


def reducer(action=(None, None), state=initial_state):

    action_type, payload = action

    if (
        action_type == north
        or action_type == east
        or action_type == south
        or action_type == west
    ):
        state[action_type] += payload

    if action_type == forward:
        state[orientation_to_cardinal(state[orientation])] += payload

    if action_type == right:
        state[orientation] += payload

    if action_type == left:
        state[orientation] -= payload

    return state


# helpers
# ----------------------
def is_orientation_match(orientation, value):
    if orientation == 0:
        orientation = 360
    return (orientation / 90) % 4 == value


def orientation_to_cardinal(orientation):
    cardinal = None
    if is_orientation_match(orientation, 0):  # 0
        cardinal = north
    if is_orientation_match(orientation, 1):  # 90
        cardinal = east
    if is_orientation_match(orientation, 2):  # 180
        cardinal = south
    if is_orientation_match(orientation, 3):  # 270
        cardinal = west
    return cardinal


def get_manhattan_distance(state):
    horizontal = max(state[west], state[east]) - min(state[west], state[east])
    vertical = max(state[north], state[south]) - min(state[north], state[south])
    return horizontal + vertical


# implemention
# ----------------------


def process_data(data, reducer=reducer, log=False):
    state = reducer()
    for item in data:
        code, value = code_splitter(item)
        new_state = reducer((code, value), state)
        if log:
            print(code, value, state, new_state)
        state = new_state
    return state


# test
# assert get_manhattan_distance(process_data(test_data)) == 25

# part 1
def part_one():
    print(get_manhattan_distance(process_data(get_data())))
