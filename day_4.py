from functools import reduce
import re


def get_collection_string(filename="day_4_data.txt"):
    collection = ""
    for line in open(filename, "r"):
        if line == "\n":
            yield collection.strip().replace("\n", " ")
            collection = ""
        else:
            collection += line
    yield collection.strip().replace("\n", " ")


def collection_string_to_dict(collection_string):
    return {a: b for a, b in (item.split(":") for item in collection_string.split(" "))}


def is_collection_valid(collection_dict):
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    collection_keys = set(collection_dict.keys())
    if not (required_keys - collection_keys) == set():
        return False

    if not is_valid_byr(collection_dict["byr"]):
        return False

    if not is_valid_iyr(collection_dict["iyr"]):
        return False

    if not is_valid_eyr(collection_dict["eyr"]):
        return False

    if not is_valid_hgt(collection_dict["hgt"]):
        return False

    if not is_valid_hcl(collection_dict["hcl"]):
        return False

    if not is_valid_ecl(collection_dict["ecl"]):
        return False

    if not is_valid_pid(collection_dict["pid"]):
        return False

    return True


def is_valid_byr(value):
    return len(value) == 4 and (1920 <= int(value) <= 2002)


def is_valid_iyr(value):
    return len(value) == 4 and (2010 <= int(value) <= 2020)


def is_valid_eyr(value):
    return len(value) == 4 and (2020 <= int(value) <= 2030)


def is_valid_hgt(value):
    unit_index = max(value.find("cm"), value.find("in"))
    number = value[0:unit_index]
    unit = value[unit_index::]
    upper = 193 if unit == "cm" else 76
    lower = 150 if unit == "cm" else 59
    return lower <= int(number) <= upper


def is_valid_hcl(value):
    return re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", value)


def is_valid_ecl(value):
    valid_options = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    set_value = {value}
    return set_value - valid_options == set()


def is_valid_pid(value):
    return len(value) == 9 and value.isnumeric()


total_valid = reduce(
    lambda result, item: result + 1
    if is_collection_valid(collection_string_to_dict(item))
    else result,
    get_collection_string(),
    0,
)

print(total_valid)
