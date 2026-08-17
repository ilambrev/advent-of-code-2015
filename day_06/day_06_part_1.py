def generate_grid(n):
    return [[False] * n for _ in range(n)]

def count_lights(grid):
    light_counter = 0
    for row in grid:
        light_counter += len([l for l in row if l])

    return light_counter

def change_lights_state(grid, begin_coordinates, end_coordinates, command):
    for i in range(begin_coordinates[0], end_coordinates[0] + 1):
        for j in range(begin_coordinates[1], end_coordinates[1] + 1):
            if command == "toggle":
                grid[i][j] = not grid[i][j]
            elif command == "turn on":
                grid[i][j] = True
            elif command == "turn off":
                grid[i][j] = False

file_path = "day_06_sample_data.txt"

file = open(file_path, "r")
instructions = file.read().split("\n")
file.close()

grid = generate_grid(1000)

for instruction in instructions:
    parts = instruction.split()

    begin_coordinates = [int(c) for c in parts[-3].split(",")]
    end_coordinates = [int(c) for c in parts[-1].split(",")]
    command = ""

    if len(parts) == 5:
        command = " ".join(parts[:2])
    else:
        command = parts[0]

    change_lights_state(grid, begin_coordinates, end_coordinates, command)

print(count_lights(grid))