def matches_vowel_count(text):
    vowels = "aeiou"

    return len([v for v in text if v in vowels]) >= 3

def matches_repeat_letter_count(text):
    is_repeated = False
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            is_repeated = True
            break

    return is_repeated

def matches_substrings_content(text):
    substrings = ["ab", "cd", "pq", "xy"]

    return len([s for s in substrings if s in text]) == 0

file_path = "day_05_sample_data.txt"

file = open(file_path, "r")
text_rows = file.read().split()
file.close()

nice_strings = 0

for row in text_rows:
    is_nice = matches_vowel_count(row) and matches_repeat_letter_count(row) and matches_substrings_content(row)
    if is_nice:
        nice_strings += 1

print(nice_strings)