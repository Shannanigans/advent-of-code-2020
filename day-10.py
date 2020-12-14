from math import prod
from pprint import pprint


def get_data(filename="day-10-data.txt"):
    with open(filename) as f:
        data = list(map(lambda x: int(x), f.readlines()))
        data.sort()
        return data


test_data_small = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]
test_data_small.sort()

test_data = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]
test_data.sort()


def process(data, counts={"1": 1}):
    data.sort()
    print("start", data)
    for index, item in enumerate(data):
        if index < len(data) - 1:
            diff = -(item - data[index + 1])
            counts[str(diff)] = int(counts[str(diff)]) + 1 if str(diff) in counts else 1
        else:
            counts["3"] = counts["3"] + 1
            print("end", index, item)
        print("item: ", item, " counts: ", counts)
    return counts


# part 1
# print(process(test_data))
# print(prod([*process(get_data())]))
# print(prod([int(x) for x in process(get_data()).values()]))

# part 2


def is_valid_option(prospect, current_value):
    return prospect > current_value and prospect <= current_value + 3


def get_combination(
    data, index, combination, debug=False, output={"count": 0, "full_combinations": []}
):
    matches = [x for x in data if is_valid_option(x, combination[index])]
    if len(matches) > 0:
        for match in matches:
            get_combination(data, index + 1, [*combination, match], debug, output)
    else:
        if debug:
            output["full_combinations"].append([*combination, combination[-1] + 3])
        output["count"] += 1

    return output


# pprint(get_combination(test_data_small, index=0, combination=[0], debug=True))
# print(
#     "result: ",
#     get_combination(test_data, index=0, combination=[0]),
# )
print("result: ", get_combination(get_data(), index=0, combination=[0]))
