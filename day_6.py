from functools import reduce


def get_collection_string(filename="day_6_data.txt"):
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


def get_collection_sum(set_operation):
    return reduce(
        lambda result, item: result + len(set_operation(*get_collection_sets(item))),
        get_collection_string(),
        0,
    )


print(get_collection_sum(set.union))
print(get_collection_sum(set.intersection))
