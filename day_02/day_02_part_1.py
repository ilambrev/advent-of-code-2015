file_path = "day_02_sample_data.txt"

file = open(file_path, "r")
boxes = file.read().split()
file.close()

papaer_needed = 0

for box in boxes:
    l, w, h = [int(d) for d in box.split("x")]
    side_a = l * w
    side_b = w * h
    side_c = h * l

    papaer_needed += 2 * (side_a + side_b + side_c) + min([side_a, side_b, side_c]) 

print(papaer_needed)