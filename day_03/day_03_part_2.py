file_path = "day_03_sample_data.txt"

file = open(file_path, "r")
directions = file.read()
file.close()

row_santa = 0
col_santa = 0
row_robo = 0
col_robo = 0
houses = {"0:0": 2}
is_santa_turn = True

for direction in directions:
    row = row_santa if is_santa_turn else row_robo
    col = col_santa if is_santa_turn else col_robo

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

    if is_santa_turn:
        row_santa = row
        col_santa = col
    else:
        row_robo = row
        col_robo = col

    is_santa_turn = not (is_santa_turn)

print(len(houses))