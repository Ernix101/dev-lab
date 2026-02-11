file_path = r"C:\\Users\\Administrator\\Desktop\\raw_patients.txt"



clean_patients = {}

with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()

        if "," not in line:
            continue 

        name, age = line.split(",")

        name = name.strip()
        age = age.strip()

        if name == "":
            continue


        if not name or not age.isdigit():
            continue
        print("Processing", name, age)

    clean_patients[name] = int(age)

print(clean_patients)
try:
    with open('clean_patients.txt', 'w') as f:
        for name, age in clean_patients.items():
            f.write(f"{name} : {age}\n")
except ValueError:
    print("Not Enough values to unpack")

import os
print(os.getcwd())