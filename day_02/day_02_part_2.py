file_path = "day_02_sample_data.txt"

file = open(file_path, "r")
boxes = file.read().split()
file.close()

ribbon_needed = 0

for box in boxes:
    l, w, h = [int(d) for d in box.split("x")]
    box_volume = l * w * h

    ribbon_needed += box_volume + 2 * (sum(sorted([l, w, h])[:2]))

print(ribbon_needed)