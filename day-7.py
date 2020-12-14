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


def build_graph(edge_map, key, target="shiny gold"):
    """Debug tool"""

    def _build_graph(edge_map, key, result={}):
        result[key] = edge_map[key]
        for child in result[key]:
            if child:
                result[key][child] = _build_graph(edge_map, child, result[key])
        return result[key]

    return {key: _build_graph(edge_map, key)}


def search(edge_map, key, target, result=False):
    result = result if result else key == target
    for child in edge_map[key]:
        if child:
            child_result = search(edge_map, child, target, result)
            result = result if result else child_result
    return result


def get_product_count(edge_map, key, result=0):
    for child in edge_map[key]:
        if child:
            result += edge_map[key][child] * get_product_count(edge_map, child, 1)
    return result


def get_target_count(edge_map, target):
    target_set = {item for item in edge_map if search(edge_map, item, target)}
    return len(target_set) - 1


# debug
# pprint(build_graph(get_edge_map(), "light salmon"))

# Part 1
print(get_target_count(get_edge_map(), "shiny gold"))

# Part 2
print(get_product_count(get_edge_map(), "shiny gold"))
