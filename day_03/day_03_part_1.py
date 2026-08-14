file_path = "day_03_sample_data.txt"

file = open(file_path, "r")
directions = file.read()
file.close()

row = 0
col = 0
houses = {"0:0": 1}

for direction in directions:
    if direction == "^":
        row -= 1
    elif direction == ">":
        col += 1
    elif direction == "v":
        row += 1
    elif direction == "<":
        col -= 1

    coordinates = f"{row}:{col}"
    houses[coordinates] = houses.get(coordinates, 0) + 1

print(len(houses))