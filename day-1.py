values = [
    1028,
    1987,
    1938,
    1136,
    1503,
    1456,
    1107,
    1535,
    1946,
    1986,
    855,
    1587,
    1632,
    1548,
    1384,
    1894,
    1092,
    1876,
    1914,
    1974,
    1662,
    1608,
    2004,
    1464,
    1557,
    1485,
    1267,
    1582,
    1307,
    1903,
    1102,
    1578,
    1421,
    1184,
    1290,
    1786,
    1295,
    1930,
    1131,
    1802,
    1685,
    1735,
    1498,
    1052,
    1688,
    990,
    1805,
    1768,
    1922,
    1781,
    1897,
    1545,
    1591,
    1393,
    1186,
    149,
    1619,
    1813,
    1708,
    1119,
    1214,
    1705,
    1942,
    1684,
    1460,
    1123,
    1439,
    1672,
    1980,
    1337,
    1731,
    1203,
    1481,
    2009,
    1110,
    1116,
    1443,
    1957,
    1891,
    1595,
    1951,
    1883,
    1733,
    1697,
    1321,
    1689,
    1103,
    1300,
    1262,
    1190,
    1667,
    1843,
    1544,
    1877,
    1718,
    1866,
    1929,
    1169,
    1693,
    1518,
    1375,
    1477,
    1222,
    1791,
    1612,
    1373,
    1253,
    1087,
    1959,
    1970,
    1112,
    1778,
    1412,
    1127,
    1767,
    1091,
    1653,
    1609,
    1810,
    1912,
    1917,
    935,
    1499,
    1878,
    1452,
    1935,
    1937,
    968,
    1905,
    1077,
    1701,
    1789,
    1506,
    1451,
    1125,
    1686,
    1117,
    1991,
    1215,
    1776,
    1976,
    846,
    1923,
    1945,
    1888,
    1193,
    1146,
    1583,
    1315,
    1372,
    1963,
    1491,
    1777,
    1799,
    1363,
    1579,
    1367,
    1863,
    1983,
    1679,
    1944,
    1654,
    1953,
    1297,
    530,
    1502,
    1738,
    1934,
    1185,
    1998,
    1764,
    1856,
    1207,
    1181,
    1494,
    1676,
    1900,
    1057,
    339,
    1994,
    2006,
    1536,
    2007,
    644,
    1173,
    1692,
    1493,
    1756,
    1916,
    1890,
    1908,
    1887,
    1241,
    1447,
    1997,
    1967,
    1098,
    1287,
    1392,
    1932,
]


target = 2020

# part one
# def find_sum_target(values, target):
#     for first in values:
#         for second in values:
#             if first + second == target:
#                 return first * second


# print(find_sum_target(values, target))


# part two
from itertools import combinations
from math import prod


def find_sum_target(values, target, combo_num):
    for x in combinations(values, combo_num):
        if sum(x) == target:
            return prod(x)

# find_sum_target(values, target, 3)
# print(find_sum_target(values, target, 3))

# part to refined
def find_sum_target_next(values, target, combo_num):
    return next(prod(x) for x in combinations(values, r=combo_num) if sum(x) == target)



# values_list = [1, 2, 2, 3]
# values_set = set(values_list)

# print("values_list", values_list)
# print("values_set", values_set)

# list_combinations = set(combinations(values_list, 2))
# set_combinations = set(combinations(values_set, 2))

# print("list_combinations", list_combinations)
# print("set_combinations", set_combinations)

# assert list_combinations == set_combinations, "missing combinations detected"






# from itertools import product, combinations

# values_list = [1, 2, 2, 3]
# values_set = set(values_list)

# # print("values_list", values_list)
# # print("values_set", values_set)

# # product_list = set(product(values_list, values_list))
# product_set = set(product(values_set, values_set))
# list_combinations = set((combinations(values_list, 2)))

# print("product_set", product_set)
# print("list_combinations", list_combinations)
