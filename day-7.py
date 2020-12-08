from functools import reduce


def get_data_string(filename="day-7-data.txt"):
    for line in open(filename, "r"):
        yield line.strip()


split_index = lambda string, index: (string[index + 1 :], string[:index])
clean_string = lambda string: multi_replace(
    string, ["bags", "bag", ".", "no other"]
).strip()
multi_replace = lambda string, char_list: reduce(
    lambda result, item: result.replace(item, ""), char_list, string
)

for x in get_data_string():
    key, values_string = x.split("contain")
    key = clean_string(key)
    full_dict = {
        clean_string(key): {
            k: int(v) if v.isnumeric() else 0
            for child in values_string.split(", ")
            for (k, v) in [split_index(clean_string(child), 1)]
        }
    }
    print(full_dict)
