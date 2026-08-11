file_path = "day_01_sample_data.txt"

file = open(file_path, "r")
directions = file.read()
file.close()

final_floor = sum([1 if d == "(" else -1 for d in directions])

print(final_floor)