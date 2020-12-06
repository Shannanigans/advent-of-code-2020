from functools import reduce


def get_collection_string(filename="day-6-data.txt"):
    collection = ""
    for line in open(filename, "r"):
        if line == "\n":
            yield collection.strip().replace("\n", " ")
            collection = ""
        else:
            collection += line
    yield collection.strip().replace("\n", " ")


def get_collection_sets(collection):
    return [set(x) for x in collection.split(" ")]


def get_collection_union(collection_list_of_sets):
    return set().union(*collection_list_of_sets)


def get_collection_intersection(collection_list_of_sets):
    return set.intersection(*collection_list_of_sets)


def get_collection_union_num_ans(collection):
    return len(get_collection_union(get_collection_sets(collection)))


def get_collection_intersection_num_ans(collection):
    return len(get_collection_intersection(get_collection_sets(collection)))


def get_unique_ans_sum():
    return reduce(
        lambda result, item: result + get_collection_union_num_ans(item),
        get_collection_string(),
        0,
    )


def get_intersection_ans_sum():
    return reduce(
        lambda result, item: result + get_collection_intersection_num_ans(item),
        get_collection_string(),
        0,
    )


print(get_intersection_ans_sum())
