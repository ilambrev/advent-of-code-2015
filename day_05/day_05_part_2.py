def matches_pair_of_two_letters(text):
    for i in range(len(text) - 3):
        counter = 1
        pair = text[i:i+2]
        for j in range(i + 2, len(text) - 1):
            if text[j:j+2] == pair:
                counter += 1
        if counter > 1:
            return True

    return False

def matches_repeat_letter(text):
    for i in range(len(text) - 2):
        l1, l2, l3 = text[i:i+3]
        if l1 == l3 and not l2 == l1:
            return True

    return False

file_path = "day_05_sample_data.txt"

file = open(file_path, "r")
text_rows = file.read().split()
file.close()

nice_strings = 0

for row in text_rows:
    is_nice = matches_pair_of_two_letters(row) and matches_repeat_letter(row)
    if is_nice:
        nice_strings += 1

print(nice_strings)