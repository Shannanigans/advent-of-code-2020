from math import ceil
from functools import reduce


def search(lower, upper, address, lower_char, upper_char):
    char = address[0]
    lower = lower if char == lower_char else ceil((lower + upper) / 2)
    upper = upper if char == upper_char else (lower + upper) // 2
    if len(address) > 1:
        return search(lower, upper, address[1:], lower_char, upper_char)
    else:
        return lower if char == lower_char else upper


def get_row_address(full_address):
    return full_address[0:7]


def get_col_address(full_address):
    return full_address[7:]


def resolve_address(full_address):
    return (
        search(
            lower=0,
            upper=127,
            address=get_row_address(full_address),
            lower_char="F",
            upper_char="B",
        ),
        search(
            lower=0,
            upper=7,
            address=get_col_address(full_address),
            lower_char="L",
            upper_char="R",
        ),
    )


def get_seat_id(full_address):
    row, col = resolve_address(full_address)
    return row * 8 + col


def get_address(filename="day_5_data.txt"):
    for line in open(filename, "r"):
        yield line.strip()


def find_max_seat_id():
    return reduce(lambda result, item: max(result, get_seat_id(item)), get_address(), 0)


def get_seats():
    return [get_seat_id(full_address) for full_address in get_address()]


def find_gap(seats):
    seats.sort()
    for seat in seats:
        if seat != seats[-1] and seat != seats[0] and seat + 1 not in seats:
            return seat + 1


print("FBFBBFFRLR", resolve_address("FBFBBFFRLR"), get_seat_id("FBFBBFFRLR"))
print("BFFFBBFRRR", resolve_address("BFFFBBFRRR"), get_seat_id("BFFFBBFRRR"))
print("FFFBBBFRRR", resolve_address("FFFBBBFRRR"), get_seat_id("FFFBBBFRRR"))
print("BBFFBBFRLL", resolve_address("BBFFBBFRLL"), get_seat_id("BBFFBBFRLL"))

print("max_seat_id: ", find_max_seat_id())

print("gap seat: ", find_gap(get_seats()))
