from functools import reduce
from pprint import pprint


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


def get_edge_map():
    all_maps = {}
    for x in get_data_string():
        key, values_string = x.split("contain")
        all_maps[clean_string(key)] = {
            k: int(v) if v.isnumeric() else 0
            for child in values_string.split(", ")
            for (k, v) in [split_index(clean_string(child), 1)]
        }
    return all_maps


def search(edge_map, key, target="shiny gold"):
    def _search(edge_map, key, result={}):
        result[key] = edge_map[key]
        for child in result[key]:
            if child:
                result[key][child] = _search(edge_map, child, result[key])
            else:
                result[key] = None
        return result[key]

    return {key: _search(edge_map, key)}


# search(get_edge_map(), "light salmon")
# pprint(search(get_edge_map(), "light salmon"))

edge_map = get_edge_map()

for item in edge_map:
    # search(edge_map, item)
    # print(search(edge_map, item))
    pprint(search(edge_map, item))
