"""
Part 1

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc


Determine
    min
    max
    letter
    text

How many are valid
"""


def extract_line_values(line):
    # Remove useless chars
    line = line.replace(":", "").strip()

    # split by space to get major sections
    min_max, target_char, text = line.split(" ")

    # get min max limits
    min_max = min_max.split("-")
    min_limit = int(min_max[0])
    max_limit = int(min_max[1])

    return min_limit, max_limit, target_char, text


def part_one_get_valid_count(filename="day_2_data.txt"):
    valid_count = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            # extract values from line
            min_limit, max_limit, target_char, text = extract_line_values(line)

            # determine target_char occurrences
            occurrence_count = text.count(target_char)

            # determine if valid and increment valid count
            if (min_limit <= occurrence_count) and (occurrence_count <= max_limit):
                valid_count = valid_count + 1

            line = f.readline()

    return valid_count


# print(part_one_get_valid_count())


"""
Part 2
"""


def is_present_at_location(text, target_char, index):
    return text[index - 1] == target_char


def is_valid(first_location_present, second_location_present):
    return (first_location_present and not second_location_present) or (
        not first_location_present and second_location_present
    )


def part_two_get_valid_count(filename="day_2_data.txt"):
    valid_count = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            # extract values from line
            first_index, second_index, target_char, text = extract_line_values(line)

            # determine if valid and increment valid count
            if is_valid(
                is_present_at_location(text, target_char, first_index),
                is_present_at_location(text, target_char, second_index),
            ):
                valid_count = valid_count + 1

            line = f.readline()

    return valid_count


print(part_two_get_valid_count())
