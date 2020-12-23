with open("day_5_data.txt", "r") as file:
    raw = file.read().strip()

print("raw", raw)

clean = (
    raw.replace("F", "0")
    .replace("B", "1")
    .replace("L", "0")
    .replace("R", "1")
    .split("\n")
)

print("CLEAN", clean)

seats = [int(s, 2) for s in clean]
print("SEATS", seats)
print(max(seats))
seats.sort()
me = [s - 1 for i, s in enumerate(seats[1:]) if seats[i] < s - 1]
print(me)
