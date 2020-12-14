def get_data(filename="day-9-data.txt"):
    with open(filename) as f:
        return list(map(lambda x: int(x), f.readlines()))


test_data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]

preable_num = 25
test_preable_num = 5


def is_valid_value(range_slice, value):
    for x in range_slice:
        for y in range_slice:
            if x != y and x + y == value:
                return True
    return False


def find_invalid(data, preable_num, index):
    range_slice = data[index - preable_num : index + 1]
    value = data[index + 1]
    is_valid = is_valid_value(range_slice, value)
    if not is_valid:
        return is_valid, value

    is_valid, value = find_invalid(data, preable_num, index + 1)

    return is_valid, value


# Test
# is_valid, value = find_invalid(test_data, test_preable_num, test_preable_num)

# Part 1
is_valid, result_part_1 = find_invalid(get_data(), preable_num, preable_num)
print("part_1: ", result_part_1)

# Part 2
def sum_walk(range_slice, target_value):
    for index, value in enumerate(range_slice):
        contiguous_range = range_slice[0:index]
        range_sum = sum(contiguous_range)
        if range_sum == target_value:
            return contiguous_range


def find_invalid_value_sum_slice(data, target_value):
    for index, item in enumerate(data):
        sum_value = sum_walk(data[index::], target_value)
        if sum_value:
            return min(sum_value) + max(sum_value)


result_part_2 = find_invalid_value_sum_slice(
    get_data(), find_invalid(get_data(), preable_num, preable_num)[1]
)
print("part_2: ", result_part_2)
