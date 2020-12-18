from pprint import pprint
from functools import reduce, partial
import copy

test_data = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]

test_final_world = [
    "#.#L.L#.##",
    "#LLL#LL.L#",
    "L.#.L..#..",
    "#L##.##.L#",
    "#.#L.LL.LL",
    "#.#L#L#.##",
    "..L.L.....",
    "#L#L##L#L#",
    "#.LLLLLL.L",
    "#.#L#L#.##",
]


def get_data(filename="day-11-data.txt"):
    with open(filename) as f:
        return preprocess(f.readlines())


# ensure data list of lists
def preprocess(x):
    return list(map(list, x))


# Walk/view functions
# -----------------------------------------

# find world limits (should be cached)
def get_limits(world):
    y_limit = len(world)
    x_limit = len(world[0])
    return x_limit, y_limit


# moves
move_up = lambda x, y: (x, y - 1)
move_down = lambda x, y: (x, y + 1)
move_right = lambda x, y: (x + 1, y)
move_left = lambda x, y: (x - 1, y)

# can moves
can_up = lambda x, y: y - 1 >= 0
can_down = lambda x, y, y_limit: y + 1 < y_limit
can_right = lambda x, y, x_limit: x + 1 < x_limit
can_left = lambda x, y: x - 1 >= 0
get_can_down = lambda y_limit: partial(can_down, y_limit=y_limit)
get_can_right = lambda x_limit: partial(can_right, x_limit=x_limit)


# performs non safe moves
def direction_compose(world, x, y, moves):
    x, y = reduce(lambda result, func: func(result[0], result[1]), moves, (x, y))
    return world[y][x], x, y


# performs safe walk via `cans` in `moves` directions
def walk(world, x, y, cans, moves):
    can_pass = reduce(
        lambda result, can: False if not result or not can(x, y) else True, cans, True
    )
    if can_pass:
        char, next_x, next_y = direction_compose(world, x, y, moves)
    else:
        return None

    if char == "#" or char == "L":
        return char
    else:
        return walk(world, next_x, next_y, cans, moves)


# get all relevant view characters for a given position
def get_views(world, x, y):
    x_limit, y_limit = get_limits(world)
    views = []
    can_down = get_can_down(y_limit)
    can_right = get_can_right(x_limit)

    views.append(walk(world, x, y, [can_up], [move_up]))
    views.append(walk(world, x, y, [can_right], [move_right]))
    views.append(walk(world, x, y, [can_down], [move_down]))
    views.append(walk(world, x, y, [can_left], [move_left]))
    views.append(walk(world, x, y, [can_up, can_right], [move_up, move_right]))
    views.append(walk(world, x, y, [can_up, can_left], [move_up, move_left]))
    views.append(walk(world, x, y, [can_down, can_right], [move_down, move_right]))
    views.append(walk(world, x, y, [can_down, can_left], [move_down, move_left]))

    return views


# get all relevant adjacent characters for a given position
def get_adjacent(world, x, y):
    x_limit, y_limit = get_limits(world)
    adjacent = []
    can_down = get_can_down(y_limit)
    can_right = get_can_right(x_limit)

    if can_up(x, y):
        adjacent.append(direction_compose(world, x, y, [move_up])[0])
    if can_down(x, y):
        adjacent.append(direction_compose(world, x, y, [move_down])[0])
    if can_right(x, y):
        adjacent.append(direction_compose(world, x, y, [move_right])[0])
    if can_left(x, y):
        adjacent.append(direction_compose(world, x, y, [move_left])[0])
    if can_up(x, y) and can_right(x, y):
        adjacent.append(direction_compose(world, x, y, [move_up, move_right])[0])
    if can_up(x, y) and can_left(x, y):
        adjacent.append(direction_compose(world, x, y, [move_up, move_left])[0])
    if can_down(x, y) and can_right(x, y):
        adjacent.append(direction_compose(world, x, y, [move_down, move_right])[0])
    if can_down(x, y) and can_left(x, y):
        adjacent.append(direction_compose(world, x, y, [move_down, move_left])[0])
    return adjacent


# World char composable functions
# -----------------------------------------

# Every seat in the example layout becomes occupied
def init(world, x, y):
    char = world[y][x]
    return "#" if char == "L" else char


def vacate_or_occupy(
    world, x, y, view_func=get_adjacent, vacate_limit=4, occupy_limit=0
):
    char = world[y][x]
    if char == "#":
        """vacate"""
        char = "L" if view_func(world, x, y).count("#") >= vacate_limit else char
    if char == "L":
        """occupy"""
        char = "#" if view_func(world, x, y).count("#") == occupy_limit else char
    return char


views_vacate_or_occupy_partial = partial(
    vacate_or_occupy, view_func=get_views, vacate_limit=5
)


def log_char(target_x, target_y):
    """ Usage example: partial(process_world, process_func=log_char(8, 0))"""

    def _log_char(world, x, y):
        if x == target_x and y == target_y:
            print("log_char", x, y, world[y][x], get_adjacent(world, x, y))
        return world[y][x]

    return _log_char


# World composable functions
# -----------------------------------------
def get_occupied(world):
    return len([char for row in world for char in row if char == "#"])


def log_occupied(world):
    print("occupied seats", get_occupied(world))
    return world


def get_stabilized_gate(world):
    state = dict(last_occupied=0)

    def stabilized_gate(world):
        # not returning world ends execution
        occupied = get_occupied(world)
        if occupied != state["last_occupied"]:
            state["last_occupied"] = occupied
            return world

    return stabilized_gate


def log_world(world):
    print("===")
    pprint(world)
    return world


# World processing functions
# -----------------------------------------
def process_world(world, process_func):
    new_world = copy.deepcopy(world)
    for y, row in enumerate(world):
        for x, char in enumerate(row):
            new_world[y][x] = process_func(world, x, y)
    return new_world


def multi_process_world(world, operations):
    return reduce(lambda result, func: func(result), operations, world)


# composable operation partial helpers
process_init = partial(process_world, process_func=init)
process_vacate_or_occupy = partial(process_world, process_func=vacate_or_occupy)
process_vacate_or_occupy_view = partial(
    process_world, process_func=views_vacate_or_occupy_partial
)

# Implementation
# -----------------------------------------

# TEST DATA
# world = preprocess(test_data)
# final_world = multi_process_world(
#     world,
#     [
#         process_init,
#         log_world,
#         process_vacate_or_occupy,
#         log_world,
#         process_vacate_or_occupy,
#         log_world,
#         process_vacate_or_occupy,
#         log_world,
#         process_vacate_or_occupy,
#         log_world,
#         log_occupied,
#         process_vacate_or_occupy,
#         log_world,
#         log_occupied,
#     ],
# )
# assert final_world == preprocess(test_final_world)


def find_stabilization(process_func=process_vacate_or_occupy):
    world = process_init(get_data())
    stabilized_gate = get_stabilized_gate(world)
    while world:
        world = process_func(world)
        log_occupied(world)
        world = stabilized_gate(world)


# PART ONE
# find_stabilization()  # 2152


# PART TWO
find_stabilization(process_vacate_or_occupy_view)  # 1937

