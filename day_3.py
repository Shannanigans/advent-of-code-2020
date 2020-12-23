def get_world(filename="day_3_data.txt"):
    with open(filename) as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def get_new_x(x, x_step, x_limit):
    x += x_step
    return x - x_limit if x >= x_limit else x


def get_new_y(y, y_step):
    return y + y_step


def get_new_collisions(end_step_location, collisions, collision_char="#"):
    return collisions + 1 if end_step_location == collision_char else collisions


def is_traversal_complete(y, y_limit):
    return y >= (y_limit)


def step(world, x_limit, y_limit, x=0, y=0, x_step=3, y_step=1, collisions=0):
    def _step(x=0, y=0, collisions=0):
        x = get_new_x(x, x_step, x_limit)
        y = get_new_y(y, y_step)

        if is_traversal_complete(y, y_limit):
            return collisions

        collisions = get_new_collisions(world[y][x], collisions)
        return _step(x, y, collisions)

    return _step(x, y, collisions)


world = get_world()
# print(
#     step(
#         world=world,
#         x_limit=len(world[0]),
#         y_limit=len(world),
#         x_step=3,
#         y_step=1,
#     )
# )


from math import prod

print(
    prod(
        [
            step(
                world=world,
                x_limit=len(world[0]),
                y_limit=len(world),
                x_step=1,
                y_step=1,
            ),
            step(
                world=world,
                x_limit=len(world[0]),
                y_limit=len(world),
                x_step=3,
                y_step=1,
            ),
            step(
                world=world,
                x_limit=len(world[0]),
                y_limit=len(world),
                x_step=5,
                y_step=1,
            ),
            step(
                world=world,
                x_limit=len(world[0]),
                y_limit=len(world),
                x_step=7,
                y_step=1,
            ),
            step(
                world=world,
                x_limit=len(world[0]),
                y_limit=len(world),
                x_step=1,
                y_step=2,
            ),
        ]
    )
)
