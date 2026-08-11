file_path = "day_01_sample_data.txt"

file = open(file_path, "r")
directions = file.read()
file.close()

current_floor = 0
current_char_position = 1

for direction in directions:
    current_floor += 1 if direction == "(" else -1
    if current_floor < 0:
        break
    current_char_position += 1

print(current_char_position)