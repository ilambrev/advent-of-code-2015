import hashlib

file_path = "day_04_sample_data.txt"

file = open(file_path, "r")
key = file.read()
file.close()

i = 0

while True:
    s = f"{key}{i}"
    res = hashlib.md5(s.encode())

    if res.hexdigest()[:5] == "00000":
        break
    else:
        i += 1
        
print(i)