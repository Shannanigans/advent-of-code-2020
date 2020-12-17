from pprint import pprint
from functools import reduce, partial
import copy


def get_data(filename="day-11-data.txt"):
    with open(filename) as f:
        return preprocess(f.readlines())


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


def preprocess(x):
    return list(map(list, x))


def get_limits(world):
    y_limit = len(world)
    x_limit = len(world[0])
    return x_limit, y_limit


move_down = lambda x, y: (x, y + 1)
move_up = lambda x, y: (x, y - 1)
move_right = lambda x, y: (x + 1, y)
move_left = lambda x, y: (x - 1, y)


def direction_compose(world, x, y, directions):
    x, y = reduce(lambda result, func: func(result[0], result[1]), directions, (x, y))
    return world[y][x]


def get_adjacent(world, x, y):
    x_limit, y_limit = get_limits(world)
    adjacent = []
    down = y + 1 < y_limit
    up = y - 1 >= 0
    right = x + 1 < x_limit
    left = x - 1 >= 0
    # print("x_limit, y_limit", x_limit, y_limit, x, y)
    # print(up, right, down, left)

    if up:
        adjacent.append(direction_compose(world, x, y, [move_up]))
    if down:
        adjacent.append(direction_compose(world, x, y, [move_down]))
    if right:
        adjacent.append(direction_compose(world, x, y, [move_right]))
    if left:
        adjacent.append(direction_compose(world, x, y, [move_left]))
    if up and right:
        adjacent.append(direction_compose(world, x, y, [move_up, move_right]))
    if up and left:
        adjacent.append(direction_compose(world, x, y, [move_up, move_left]))
    if down and right:
        adjacent.append(direction_compose(world, x, y, [move_down, move_right]))
    if down and left:
        adjacent.append(direction_compose(world, x, y, [move_down, move_left]))

    return adjacent


def init(world, x, y):
    """
    After one round of these rules, every seat in the example layout becomes occupied
    """
    char = world[y][x]
    return "#" if char == "L" else char


def vacate_or_occupy(world, x, y):
    char = world[y][x]
    if char == "#":
        """
        vacate
        If a seat is occupied (#) and four or more seats adjacent to it are also
        occupied, the seat becomes empty. Otherwise, the seat's state does not change.
        """
        char = "L" if get_adjacent(world, x, y).count("#") >= 4 else char
    if char == "L":
        """
        occupy
        If a seat is empty (L) and there are no occupied seats adjacent to it, the
        seat becomes occupied.
        """
        char = "#" if get_adjacent(world, x, y).count("#") == 0 else char
    return char


def log_char(target_x, target_y):
    """ Usage example: partial(process_world, process_func=log_char(8, 0))"""

    def _log_char(world, x, y):
        if x == target_x and y == target_y:
            print("log_char", x, y, world[y][x], get_adjacent(world, x, y))
        return world[y][x]

    return _log_char


def process_world(world, process_func):
    new_world = copy.deepcopy(world)
    for y, row in enumerate(world):
        for x, char in enumerate(row):
            new_world[y][x] = process_func(world, x, y)
    return new_world


def get_occupied(world):
    return len([char for row in world for char in row if char == "#"])


def log_occupied(world):
    print("occupied seats", get_occupied(world))
    return world


def stabilized_gate(world):
    state = dict(last_occupied=0)

    def _stabilized_gate(world):
        # not returning world ends execution
        occupied = get_occupied(world)
        # print("_stabilized_gate", occupied, state["last_occupied"])
        if occupied != state["last_occupied"]:
            state["last_occupied"] = occupied
            return world

    return _stabilized_gate


def log_world(world):
    print("===")
    pprint(world)
    return world


def multi_process_world(world, operations):
    return reduce(lambda result, func: func(result), operations, world)


process_init = partial(process_world, process_func=init)
process_vacate_or_occupy = partial(process_world, process_func=vacate_or_occupy)

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


# PART ONE
def part_one():
    world = process_init(get_data())
    _stabilized_gate = stabilized_gate(world)
    while world:
        world = process_vacate_or_occupy(world)
        log_occupied(world)
        world = _stabilized_gate(world)


part_one()
